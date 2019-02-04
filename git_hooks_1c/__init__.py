# -*- coding: utf-8 -*-
import logging

# noinspection PyUnresolvedReferences
from git_hooks_1c.__about__ import __version__

# noinspection PyUnresolvedReferences
logging.getLogger().setLevel(logging.DEBUG)
logger: logging.Logger = logging.getLogger(__name__)
