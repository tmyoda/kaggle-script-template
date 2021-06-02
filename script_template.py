import gzip
import base64
import subprocess
from subprocess import PIPE
from pathlib import Path
from typing import Dict


# this is base64 encoded source code
file_data: Dict = {file_data}


for path, encoded in file_data.items():
    print(path)
    path = Path(path)
    path.parent.mkdir(exist_ok=True)
    path.write_bytes(gzip.decompress(base64.b64decode(encoded)))


def run(command):
    proc = subprocess.run('export PYTHONPATH=${PYTHONPATH}:/kaggle/working && ' + command, shell=True, stdout=PIPE, stderr=PIPE, text=True)
    print(proc.stdout)
    print(proc.stderr)


run('python setup.py develop --install-dir /kaggle/working')
run('python {project_name}/main.py')
