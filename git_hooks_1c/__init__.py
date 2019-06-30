# -*- coding: utf-8 -*-
# noinspection PyUnresolvedReferences
from pathlib import Path

# noinspection PyUnresolvedReferences
from loguru import logger
import re

here = Path(__file__).parent.parent

__version__ = '0.0.0'
with Path(here, 'pyproject.toml').open() as f:
    version_match = re.search(r'version = "(?P<version>\d+\.\d+\.\d+)"', f.read())
    if version_match:
        __version__ = version_match.group('version')
