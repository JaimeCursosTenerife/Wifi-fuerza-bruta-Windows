# Fuerza Bruta WiFi (Windows)

Este script en Python intenta conectarse a una red WiFi generando combinaciones posibles de contraseñas.  
Está diseñado para funcionar en sistemas **Windows** usando el comando `netsh`.

## ⚠️ Advertencia

Este proyecto es **solo para fines educativos**.  
El uso indebido de este código puede ser **ilegal**.  
El autor **no se hace responsable** del uso que se le dé a este programa.

## ⚙️ Notas

- Funciona en Windows con permisos de administrador.
- El rendimiento es lento debido a las limitaciones de `netsh`.
- Se recomienda desconectarse manualmente de la red antes de iniciar el ataque.
- La red debe tener el **WiFi encendido** y el SSID debe estar **visible**.

## ▶️ Cómo usar

1. Edita la variable `ssid` en el script y pon el nombre de tu red WiFi.
2. Ejecuta el script como administrador en Windows:

```bash
python fuerza_bruta_wifi.py
