from telethon import events

from uniborg.util import admin_cmd

import asyncio





@borg.on(admin_cmd(pattern="undo del"))

async def _(event):

    if event.fwd_from:

        return

    c = await event.get_chat()

    if c.admin_rights or c.creator:

        a = await borg.get_admin_log(event.chat_id,limit=1, search="", edit=False, delete=True)

        for i in a:

          await event.reply(i.original.action.message)

    else:

        await event.edit("You need administrative permissions in order to do this command")

        await asyncio.sleep(3)

        await event.delete()
