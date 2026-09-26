#!/usr/bin/env python3
"""Reempaqueta src/app.html dentro de index.html (el bundle que se publica en Vercel).

Uso:  python3 build.py
Edita siempre src/app.html; index.html se regenera con este script.
"""
import json
from pathlib import Path

root = Path(__file__).parent
bundle = root / 'index.html'
src = (root / 'src' / 'app.html').read_text(encoding='utf-8')

lines = bundle.read_text(encoding='utf-8').split('\n')
i = lines.index('  <script type="__bundler/template">') + 1
# "</" se escapa para que el HTML no cierre el <script> contenedor antes de tiempo.
lines[i] = json.dumps(src, ensure_ascii=False).replace('</', '<\\u002F')

# Etiquetas para instalar la app en el celular: iOS/Android las leen del documento inicial.
HEAD_START, HEAD_END = '  <!-- pwa -->', '  <!-- /pwa -->'
pwa = [HEAD_START,
       '  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">',
       '  <meta name="theme-color" content="#0C0B09">',
       '  <meta name="apple-mobile-web-app-capable" content="yes">',
       '  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">',
       '  <meta name="apple-mobile-web-app-title" content="Python Vault">',
       '  <link rel="manifest" href="manifest.webmanifest">',
       '  <link rel="apple-touch-icon" href="icon-180.png">',
       HEAD_END]
if HEAD_START in lines:
    lines[lines.index(HEAD_START):lines.index(HEAD_END) + 1] = pwa
else:
    t = lines.index('  <title>Python Vault</title>') + 1
    lines[t:t] = pwa

bundle.write_text('\n'.join(lines), encoding='utf-8')
print('index.html actualizado desde src/app.html')
