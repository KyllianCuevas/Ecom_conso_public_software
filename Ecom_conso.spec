# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['Ecom_conso.py'],
    pathex=[],
    binaries=[],
    datas=[('Logo', 'Logo'), ('image_meteo', 'image_meteo'), ('client_secret_259806932371-36t2t4d0b0pnu0694mpnja4bt7bjea7t.apps.googleusercontent.com.json', '.'), ('credentials.json', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Ecom_conso',
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
