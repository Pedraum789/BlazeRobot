# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:/Users/pedra/PycharmProjects/pythonProject/MainScreen.py'],
    pathex=[],
    binaries=[],
    datas=[('C:/Users/pedra/PycharmProjects/pythonProject/Strategies/StrategyOneFiles/StrategyOne.py', '.'), ('C:/Users/pedra/PycharmProjects/pythonProject/Strategies/StrategyOneFiles/ViewStrategyOne.py', '.'), ('C:/Users/pedra/PycharmProjects/pythonProject/Strategies/StrategyTwoFiles/StrategyTwo.py', '.'), ('C:/Users/pedra/PycharmProjects/pythonProject/Strategies/StrategyTwoFiles/ViewStrategyTwo.py', '.'), ('C:/Users/pedra/PycharmProjects/pythonProject/SearchHistory.py', '.'), ('C:/Users/pedra/PycharmProjects/pythonProject/SearchImage.py', '.'), ('C:/Users/pedra/PycharmProjects/pythonProject/ThreadProgramStop.py', '.'), ('C:/Users/pedra/PycharmProjects/pythonProject/imagens.detection/captura.png', '.'), ('C:/Users/pedra/PycharmProjects/pythonProject/imagens.detection/crashed.png', '.'), ('C:/Users/pedra/PycharmProjects/pythonProject/imagens.detection/crashed_2.png', '.'), ('C:/Users/pedra/PycharmProjects/pythonProject/imagens.detection/esperando.png', '.'), ('C:/Users/pedra/PycharmProjects/pythonProject/imagens.detection/quantia.png', '.'), ('C:/Users/pedra/PycharmProjects/pythonProject/imagens.detection/start_game.png', '.'), ('C:/Users/pedra/PycharmProjects/pythonProject/imagens.detection/start_game_2.png', '.'), ('C:/Users/pedra/PycharmProjects/pythonProject/imagens.detection/start_game_3.png', '.'), ('C:/Users/pedra/PycharmProjects/pythonProject/imagens.detection/wait_line.png', '.'), ('C:/Users/pedra/PycharmProjects/pythonProject/imagens.detection/wallet.png', '.'), ('C:/Users/pedra/PycharmProjects/pythonProject/icons/logo.ico', '.'), ('C:/Users/pedra/PycharmProjects/pythonProject/credentials/AccessCredentials.py', '.'), ('C:/Users/pedra/PycharmProjects/pythonProject/credentials/AccessEduzz.py', '.'), ('C:/Users/pedra/PycharmProjects/pythonProject/credentials/AccessHotmart.py', '.'), ('C:/Users/pedra/PycharmProjects/pythonProject/credentials/UserControl.py', '.'), ('C:/Users/pedra/PycharmProjects/pythonProject/Strategies', 'Strategies/'), ('C:/Users/pedra/PycharmProjects/pythonProject/imagens.detection', 'imagens.detection/'), ('C:/Users/pedra/PycharmProjects/pythonProject/icons', 'icons/'), ('C:/Users/pedra/PycharmProjects/pythonProject/credentials', 'credentials/'), ('C:/Free/BLAZE_DETECTION/Lib/site-packages/CTkMessagebox', 'CTkMessagebox/')],
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
    name='MainScreen',
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
    icon=['C:\\Users\\pedra\\PycharmProjects\\pythonProject\\icons\\logo.ico'],
)
