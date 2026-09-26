# Python Vault · Pedidos

App web de recepción de pedidos. Se publica como un solo archivo: `index.html`.

## Cómo editar la app
- **El código fuente es `src/app.html`** (pantallas + lógica). No edites `index.html` a mano: es un paquete generado que incluye React, fuentes e imágenes.
- Después de cambiar `src/app.html`, regenera el paquete:
  ```
  python3 build.py
  ```
- Para probar en tu computador: `python3 -m http.server 8765` y abre http://localhost:8765

## Publicar en Vercel (sin programar)
1. Crea cuenta en https://vercel.com (entra con GitHub o email).
2. Opción A — terminal: instala Node.js, abre una terminal en esta carpeta y ejecuta `npx vercel --prod`.
3. Opción B — GitHub: sube el repositorio y en Vercel: Add New → Project → Import → Deploy (Framework: Other, sin build).
4. Abre el link en el celular → Compartir → "Agregar a pantalla de inicio".

## Importante
- Los datos (clientes, pedidos, stock) se guardan en el navegador de cada dispositivo y no se comparten entre equipos.
  Usa **Stock → Respaldo de datos → Exportar respaldo** con frecuencia y guarda el archivo en Drive o en tu correo.
  Con **Importar** recuperas todo o lo pasas a otro celular.
- Usa la app en un solo dispositivo a la vez: la numeración de pedidos (PV-0001…) es local y se repetiría entre equipos.
- El mail de confirmación se prepara como borrador y se envía desde tu app de correo con el botón "Enviar mail al cliente".
  El envío automático requiere un servicio (ej. Resend) y un backend.
