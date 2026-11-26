import sys
import subprocess

print(sys.version)
print(sys.executable)
subprocess.run([sys.executable, "-m", "pip", "install", "pgzero"])