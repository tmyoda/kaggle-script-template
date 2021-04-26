#!/usr/bin/env python3
import base64
import gzip
from pathlib import Path
import json
import setup


def encode_file(path: Path) -> str:
    compressed = gzip.compress(path.read_bytes(), compresslevel=9)
    return base64.b64encode(compressed).decode('utf-8')


def build_script():
    to_encode = list(Path(setup.project_name).glob('*.py')) + \
                list(Path(setup.project_name).glob('**/*.py')) + \
                list(Path(setup.project_name).glob('**/*.yaml')) + \
                [Path('setup.py')]
    file_data = {str(path): encode_file(path) for path in to_encode}
    template = Path('script_template.py').read_text('utf8')
    template = template.replace('{file_data}', json.dumps(file_data, indent=4))
    template = template.replace('{project_name}', setup.project_name)
    Path('build/script.py').write_text(template, encoding='utf8')


if __name__ == '__main__':
    build_script()
