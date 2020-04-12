from cx_Freeze import setup, Executable


base = "Win32GUI"
executable = [Executable("main.py ", targetName='crc.exe', base=base)]

setup(name='CRC',
      version='1.0',
      description="Cyclic Redundancy Check",
      executables=executable)
