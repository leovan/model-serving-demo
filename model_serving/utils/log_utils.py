#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging.config


logging.config.fileConfig(os.path.join(os.path.dirname(__file__), '../../conf/logging.conf'))
XXXModel_LOGGER = logging.getLogger('XXXModel')
