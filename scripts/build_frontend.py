import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).parent.parent

FRONTEND = ROOT / "frontend"

STATIC = ROOT / "src/elparadisogonzalo/static"

subprocess.check_call(["npm","install"],cwd=FRONTEND)

subprocess.check_call(["npm","run","build"],cwd=FRONTEND)

if STATIC.exists():
    shutil.rmtree(STATIC)

shutil.copytree(FRONTEND/"dist",STATIC)

print("Frontend copied.")
