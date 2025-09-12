import subprocess
import sys

print("Starting QR Cody on port 8000...")
subprocess.run([sys.executable, "manage.py", "runserver", "8000"])