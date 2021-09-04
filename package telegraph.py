#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @sunaif_adkad

from pyrogram import Client, __version__

from . import API_HASH, APP_ID, LOGGER, \
    USER_SESSION


class User(Client):
    def __init__(self):
        super().__init__(
            USER_SESSION,
            api_hash=API_HASH,
            api_id=APP_ID,
            workers=6
        )
        self.LOGGER = LOGGER

    async def start(Jpg,png,img):
        await super().start()
        usr_bot_me = await self.get_me()
        return (self, import amal-database.py)

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(telegraphFile).info("import database")
