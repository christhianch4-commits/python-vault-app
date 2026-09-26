# Python Vault · Pedidos

App web de recepción de pedidos. Se publica como un solo archivo: `index.html`.

## Cómo editar la app
- **El código fuente es `src/app.html`** (pantallas + lógica). No edites `index.html` a mano: es un paquete generado que incluye React, fuentes e imágenes.
- Después de cambiar `src/app.html`, regenera el paquete:
  ```
  python3 build.py
  ```
- Para probar en tu computador: `python3 -m http.server 8765` y abre http://localhost:8765
- **Colores:** están como variables al inicio del segundo `<style>` de `src/app.html`
  (`[data-theme="dark"]` y `[data-theme="light"]`). Cambiando esos valores se recolorea toda la app.
- `manifest.webmanifest` e `icon-*.png` son el icono y el nombre al "Agregar a pantalla de inicio".

## Publicar en Vercel (sin programar)
1. Crea cuenta en https://vercel.com (entra con GitHub o email).
2. Opción A — terminal: instala Node.js, abre una terminal en esta carpeta y ejecuta `npx vercel --prod`.
3. Opción B — GitHub: sube el repositorio y en Vercel: Add New → Project → Import → Deploy (Framework: Other, sin build).
4. Abre el link en el celular → Compartir → "Agregar a pantalla de inicio".

## Importante
- Los datos (clientes, pedidos, stock) se guardan en el navegador de cada dispositivo y no se comparten entre equipos.
  Usa **Ajustes (engranaje en el Resumen) → Respaldo de datos → Exportar respaldo** con frecuencia y guarda el archivo en Drive o en tu correo.
  Con **Importar** recuperas todo o lo pasas a otro celular.
- Usa la app en un solo dispositivo a la vez: la numeración de pedidos (PV-0001…) es local y se repetiría entre equipos.
- La confirmación se prepara como mensaje y se envía por WhatsApp (si el cliente tiene celular 09…) o por mail desde tu app de correo.
  El envío automático requiere un servicio (ej. Resend) y un backend.
