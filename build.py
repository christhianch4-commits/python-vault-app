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
bundle.write_text('\n'.join(lines), encoding='utf-8')
print('index.html actualizado desde src/app.html')
