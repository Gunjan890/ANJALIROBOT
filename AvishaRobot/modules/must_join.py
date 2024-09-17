import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from AvishaRobot import pbot as app

#--------------------------
MUST_JOIN = "ANJALIWORLD"
#------------------------

NYKAA = [
    "https://te.legra.ph/file/120248292430d07703a6e.jpg",
]

async def check_user_join_channel(user_id):
    try:
        await app.get_chat_member(MUST_JOIN, user_id)
        return True
    except UserNotParticipant:
        return False

@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(app: Client, msg: Message):
    if not await check_user_join_channel(msg.from_user.id):
        if MUST_JOIN.isalpha():
            link = "https://t.me/" + MUST_JOIN
        else:
            chat_info = await app.get_chat(MUST_JOIN)
            link = chat_info.invite_link
        try:
            await msg.reply_photo(
                random.choice(NYKAA), caption=f"❖ ʜᴇʏ ᴛʜᴇʀᴇ, ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ᴜʜʜ. ♥︎\n\n● ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴜsᴇ ๛ᴀ ᴠ ɪ s ʜ ᴀ ♡゙ ʙᴏᴛ, ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴀɴᴅ ʏᴏᴜ ᴊᴏɪɴ ᴏᴜʀ sᴜᴘᴘᴏʀᴛ ᴀɴᴅ ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ, ᴛʜᴇɴ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴀʟʟ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs.\n\n❖ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➥ [🫧⏤͟͟͞ـﮩ♡︎ ˹Ҩ፝֟፝ɴ ꫝɴᴊᴀʟɪ˼ [🇮🇳] ](https://t.me/AnjaliOwnerBot)",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ", url="https://t.me/ANJALIOFFICIALNETWORK"),
                            InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url=link),
                        ],
                    ]
                )
            )
            await msg.stop_propagation()
        except ChatWriteForbidden:
            pass
        return
      
