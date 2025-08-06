# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['interfaz_gui.py'],
    pathex=[],
    binaries=[],
    datas=[('D:/Python311/Lib/site-packages/trafilatura', 'trafilatura'), ('D:/Python311/Lib/site-packages/dateparser/data/dateparser_tz_cache.pkl', 'dateparser/data'), ('D:/ffmpeg-7.1.1-essentials_build', 'ffmpeg')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='interfaz_gui',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
