#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ..utils.log_utils import XXXModel_LOGGER


LOGGER = XXXModel_LOGGER


class XXXModel():
    def __init__(self):
        LOGGER.info('Initializing XXX Model ...')

        LOGGER.info('XXX Model Initialized.')

    def hello(self, name:str) -> str:
        return 'Hello, {name}!'.format(name=name)
