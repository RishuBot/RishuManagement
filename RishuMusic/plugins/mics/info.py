import asyncio, os, time, aiohttp
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from asyncio import sleep
from RishuMusic import app
from pyrogram import filters, Client, enums
from pyrogram.enums import ParseMode
from pyrogram.types import *
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton
from typing import Union, Optional

EVAA = [
    [
        InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/DikshaChatBot?startgroup=true"),
    ],
]

get_font = lambda font_size, font_path: ImageFont.truetype(font_path, font_size)
resize_text = (
    lambda text_size, text: (text[:text_size] + "...").upper()
    if len(text) > text_size
    else text.upper()
)

# --------------------------------------------------------------------------------- #


async def get_userinfo_img(
    bg_path: str,
    font_path: str,
    user_id: Union[int, str],    
    profile_path: Optional[str] = None
):
    bg = Image.open(bg_path)

    if profile_path:
        img = Image.open(profile_path)
        mask = Image.new("L", img.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.pieslice([(0, 0), img.size], 0, 360, fill=255)

        circular_img = Image.new("RGBA", img.size, (0, 0, 0, 0))
        circular_img.paste(img, (0, 0), mask)
        resized = circular_img.resize((534, 534))
        bg.paste(resized, (607, 86), resized)

    img_draw = ImageDraw.Draw(bg)

    

    path = f"./userinfo_img_{user_id}.png"
    bg.save(path)
    return path
   

# --------------------------------------------------------------------------------- #

bg_path = "RishuMusic/assets/RISHUINFO.png"
font_path = "RishuMusic/assets/hiroko.ttf"

#
# --------------------------------------------------------------------------------- #


INFO_TEXT = """
ㅤ◦•●◉✿ ᴜsᴇʀ ɪɴғᴏʀᴍᴀᴛɪᴏɴ  ✿◉●•◦
▬▭▬▭▬▭▬▭▬▭▬▭▬▭

❍ ᴜsᴇʀ ɪᴅ ɴᴏ. ▷ `{}`
❍ ᴜsᴇʀɴᴇᴍᴇ ▷ @{} 
❍ ᴍᴇɴᴛɪᴏɴ ▷ {}
❍ sᴛᴀᴛᴜs ▷ `{}`
❍ ᴅᴄ ɪᴅ ▷ {}
❍ ʙɪᴏ ▷ {}

❖ ᴍᴀᴅᴇ ʙʏ  ➛ [Ꝛɪsʜυ ₰](https://t.me/ur_rishu_143)
▬▭▬▭▬▭▬▭▬▭▬▭▬▭

"""

# --------------------------------------------------------------------------------- #

async def userstatus(user_id):
   try:
      user = await app.get_users(user_id)
      x = user.status
      if x == enums.UserStatus.RECENTLY:
         return "User was seen recently."
      elif x == enums.UserStatus.LAST_WEEK:
          return "User was seen last week."
      elif x == enums.UserStatus.LONG_AGO:
          return "User was seen long ago."
      elif x == enums.UserStatus.OFFLINE:
          return "User is offline."
      elif x == enums.UserStatus.ONLINE:
         return "User is online."
   except:
        return "**✦ sᴏᴍᴇᴛʜɪɴɢ ᴡʀᴏɴɢ ʜᴀᴘᴘᴇɴᴇᴅ !**"
    

# --------------------------------------------------------------------------------- #

@app.on_message(filters.command(["info", "information", "userinfo"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def userinfo(_, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    
    if not message.reply_to_message and len(message.command) == 2:
        try:
            user_id = message.text.split(None, 1)[1]
            user_info = await app.get_chat(user_id)
            user = await app.get_users(user_id)
            status = await userstatus(user.id)
            id = user_info.id
            dc_id = user.dc_id
            name = user_info.first_name
            username = user_info.username
            mention = user.mention
            bio = user_info.bio
            photo = await app.download_media(user.photo.big_file_id)
            welcome_photo = await get_userinfo_img(
                bg_path=bg_path,
                font_path=font_path,
                user_id=user_id,
                profile_path=photo,
            )
            await app.send_photo(chat_id, photo=welcome_photo, caption=INFO_TEXT.format(
                id, username, mention, status, dc_id, bio), reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(EVAA),)
        except Exception as e:
            await message.reply_text(str(e))        
      
    elif not message.reply_to_message:
        try:
            user_info = await app.get_chat(user_id)
            user = await app.get_users(user_id)
            status = await userstatus(user.id)
            id = user_info.id
            dc_id = user.dc_id
            name = user_info.first_name
            username = user_info.username
            mention = user.mention
            bio = user_info.bio
            photo = await app.download_media(user.photo.big_file_id)
            welcome_photo = await get_userinfo_img(
                bg_path=bg_path,
                font_path=font_path,
                user_id=user_id,
                profile_path=photo,
            )
            await app.send_photo(chat_id, photo=welcome_photo, caption=INFO_TEXT.format(
                id, username, mention, status, dc_id, bio), reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(EVAA),)
        except Exception as e:
            await message.reply_text(str(e))

            
    elif message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        try:
            user_info = await app.get_chat(user_id)
            user = await app.get_users(user_id)
            status = await userstatus(user.id)
            id = user_info.id
            dc_id = user.dc_id
            name = user_info.first_name
            username = user_info.username
            mention = user.mention
            bio = user_info.bio
            photo = await app.download_media(message.reply_to_message.from_user.photo.big_file_id)
            welcome_photo = await get_userinfo_img(
                bg_path=bg_path,
                font_path=font_path,
                user_id=user_id,
                profile_path=photo,
            )
            await app.send_photo(chat_id, photo=welcome_photo, caption=INFO_TEXT.format(
                id, username, mention, status, dc_id, bio), reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(EVAA),)
        except Exception as e:
            await message.reply_text(str(e))

####
