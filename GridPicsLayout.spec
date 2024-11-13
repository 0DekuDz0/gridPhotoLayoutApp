# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['GridPicsLayout.py'],
    pathex=[],
    binaries=[],
    datas=[('images/buttonLayout1.jpg', 'images'), ('images/buttonLayout2.jpg', 'images'), ('images/buttonLayout3.png', 'images'), ('images/buttonLayout4.png', 'images'), ('images/buttonLayout6.png', 'images'), ('images/buttonLayout8.png', 'images'), ('images/buttonLayout9.png', 'images')],
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
    name='GridPicsLayout',
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
    icon=['menu.ico'],
)
