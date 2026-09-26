# Python Vault · Pedidos

App web de recepción de pedidos (un solo archivo: index.html).

## Publicar en Vercel (sin programar)
1. Crea cuenta en https://vercel.com (entra con GitHub o email).
2. Opción A — terminal: instala Node.js, abre una terminal en esta carpeta y ejecuta `npx vercel --prod`.
3. Opción B — GitHub: crea un repositorio nuevo en https://github.com/new, pulsa "uploading an existing file", arrastra index.html, vercel.json y este README, y "Commit".
   En Vercel: Add New → Project → Import ese repositorio → Deploy (Framework: Other, sin build).
4. Abre el link en el celular → Compartir → "Agregar a pantalla de inicio".

## Importante
- Los datos se guardan en el navegador de cada dispositivo (no se comparten entre equipos).
- El mail de confirmación se abre en tu app de correo; el envío automático requiere un servicio (ej. Resend) y un backend.
