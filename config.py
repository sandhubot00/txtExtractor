#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7586059269:AAEJW34z5_EA4ZMkfTc3ObN9HKyJY-Mcdmo")
    API_ID = int(os.environ.get("API_ID", "25471015"))
    API_HASH = os.environ.get("API_HASH", "0ab2955ad5b1a913e220800b5fc5db36")
    AUTH_USERS = os.environ.get("AUTH_USERS", "7459282233")
