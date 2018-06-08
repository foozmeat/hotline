# -*- mode: python -*-

block_cipher = None


a = Analysis(['fivecalls/main.py'],
             pathex=['/Users/james/Developer/fivecalls'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=['_tkinter', 'Tkinter', 'enchant'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='fivecalls',
          debug=False,
          strip=False,
          upx=True,
          console=False )

coll = COLLECT(exe,
               Tree('/Users/james/Developer/fivecalls/fivecalls'),
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='fivecalls')

app = BUNDLE(coll,
             name='fivecalls.app',
             icon=None,
             bundle_identifier='me.jmoore.fivecalls')
