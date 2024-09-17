from AvishaRobot import pbot as app 
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

spam_chats = []

EMOJI = [ "🦋🦋🦋🦋🦋",
          "🧚🌸🧋🍬🫖",
          "🥀🌷🌹🌺💐",
          "🌸🌿💮🌱🌵",
          "❤️💚💙💜🖤",
          "💓💕💞💗💖",
          "🌸💐🌺🌹🦋",
          "🍔🦪🍛🍲🥗",
          "🍎🍓🍒🍑🌶️",
          "🧋🥤🧋🥛🍷",
          "🍬🍭🧁🎂🍡",
          "🍨🧉🍺☕🍻",
          "🥪🥧🍦🍥🍚",
          "🫖☕🍹🍷🥛",
          "☕🧃🍩🍦🍙",
          "🍁🌾💮🍂🌿",
          "🌨️🌥️⛈️🌩️🌧️",
          "🌷🏵️🌸🌺💐",
          "💮🌼🌻🍀🍁",
          "🧟🦸🦹🧙👸",
          "🧅🍠🥕🌽🥦",
          "🐷🐹🐭🐨🐻‍❄️",
          "🦋🐇🐀🐈🐈‍⬛",
          "🌼🌳🌲🌴🌵",
          "🥩🍋🍐🍈🍇",
          "🍴🍽️🔪🍶🥃",
          "🕌🏰🏩⛩️🏩",
          "🎉🎊🎈🎂🎀",
          "🪴🌵🌴🌳🌲",
          "🎄🎋🎍🎑🎎",
          "🦅🦜🕊️🦤🦢",
          "🦤🦩🦚🦃🦆",
          "🐬🦭🦈🐋🐳",
          "🐔🐟🐠🐡🦐",
          "🦩🦀🦑🐙🦪",
          "🐦🦂🕷️🕸️🐚",
          "🥪🍰🥧🍨🍨",
          " 🥬🍉🧁🧇",
        ]

TAGMES = [ " ᴏʏʏ ᴛᴇʀᴇ ʙᴀʟᴇ ᴋᴏ ᴊᴀᴋᴀʀ ʙᴀᴛᴀᴛᴀ ʜᴜ ᴛᴜ ʏʜᴀ sᴇᴛᴛɪɴɢ ᴋᴀʀ ʀʜɪ ʜᴀɪ🥱 ",
           " ᴀᴘᴋɪ ᴇᴋ ᴘɪᴄ ᴍɪʟᴇɢɪ ᴋʏᴀ ɪᴍᴀɢɪɴᴇ ᴋᴀʀ ᴋᴇ ᴍ*ᴛʜ ᴋᴀʀɴᴀ ʜɪ ",
           " ᴠᴄ ᴄʜᴀʟᴏ ʀᴏᴍᴀɴᴛɪᴄ ʙᴀᴛᴇɴ ᴋᴀʀᴛᴇ ʜᴀɪɴ ᴋᴜᴄʜ ᴋᴜᴄʜ😃 ",
           " ᴛʜᴀɴᴅɪ ᴍᴇ ᴛᴜᴍʜᴀʀᴀ ᴋʜᴀᴅᴀ ʜᴏᴛᴀ ʜᴀɪ ᴋʏᴀ 😁🥲 ",
           " ᴜғғ ᴋʏᴀ ᴍᴀᴀʟ ʜᴀɪ ʏᴀᴀʀ 😁😂🥺 ",
           " ᴘᴛᴀ ʜᴀɪ ʙᴏʜᴏᴛ ᴍɪss ᴋᴀʀ ʀʜᴀ ᴛʜᴀ ᴀᴀᴘᴋᴏ ʙᴀᴛʜʀᴏᴏᴍ ᴍᴇ 🤭 ",
           " ᴏʏᴇ ᴅᴍ ᴋᴀʀᴏ ᴀᴘᴋᴀ ᴍᴏᴏᴅ ʙɴᴀ ᴅᴇᴛɪ ʜᴜ 😅😅 ",
           " ᴍᴇʀɪ ʙʜɪ sᴇᴛᴛɪɴɢ ᴋᴀʀʙᴀ ᴅᴏɢᴇ.ʜɪʟʟᴀ ʜɪʟʟᴀ ᴋᴇ ᴛʜᴀᴋ ɢʏᴀ ʜᴜ ??🙂 ",
           " ᴏʏʏ ᴛᴇʀᴇ ʙᴀʟᴇ ᴋᴏ ᴊᴀᴋᴀʀ ʙᴀᴛᴀᴛᴀ ʜᴜ ᴛᴜ ʏʜᴀ sᴇᴛᴛɪɴɢ ᴋᴀʀ ʀʜɪ ʜᴀɪ🥲 ",
           " ᴋᴀ ʜᴏ ᴋᴀʀᴇᴊᴀ 1 ᴄʜᴜᴍᴍᴀ ɴᴀ ᴅᴇʙᴜ 😅😋 ",
           " ᴏʏʏ ᴍᴇʀᴇ ᴋᴏ ᴀᴘɴᴇ ʙᴇᴅʀᴏᴏᴍ ᴍᴇ ᴋɪᴅɴᴇᴘ ᴋᴀʀ ʟᴏ😅😅  ",
           " ᴀᴀᴘᴋɪ ᴘᴀʀᴛɴᴇʀ ᴀᴀᴘᴋᴏ ᴅʜᴜɴᴅ ʀʜᴇ ʜᴀɪɴ ᴊʟᴅɪ ᴏɴʟɪɴᴇ ᴀʏɪᴀᴇ😅😅 ",
           " ʜᴀᴍ ᴅᴏsᴛ ʙᴀɴ sᴀᴋᴛᴇ ʜᴀɪ...?🥰 ᴍᴀsᴛᴇʀʙᴀᴛɪɴɢ ᴋᴀʀɴᴇ ᴍᴇ ʜᴇʟᴘ ʜᴏ ᴊᴀʏᴇɢɪ ᴍᴇʀɪ 😁🤔 ",
           " sᴏɴᴇ ᴄʜᴀʟ ɢʏᴇ ᴋʏᴀ ᴊᴀɴᴇᴍᴀɴ 🙄🙄 ",
           " ʜᴀᴍ ᴅᴏsᴛ ʙᴀɴ sᴀᴋᴛᴇ ʜᴀɪ...?🥰 ᴍᴀsᴛᴇʀʙᴀᴛɪɴɢ ᴋᴀʀɴᴇ ᴍᴇ ʜᴇʟᴘ ʜᴏ ᴊᴀʏᴇɢɪ ᴍᴇʀɪ 😁 😁😕 ",
           " ʏᴏᴜʀ ғᴀᴠᴏᴜʀɪᴛᴇ ᴀᴄᴛʀᴇss (sᴜɴɴʏ ʟᴇᴏɴᴇ, ᴏʀ ᴍɪʏᴀ ᴋʜᴀʟɪғᴀ)🙃 ",
           " ᴏʏʏ ᴘʀɪʏᴀ ʙʜᴀʙʜɪ ᴋᴀ ᴋʏᴀ ʜᴀɪ 😁😁😛 ",
           " ʜᴇʟʟᴏ ʙᴀʙʏ ᴋᴋʀʜ..?🤔 ",
           " ᴏʏʏ sᴜɴᴏ ᴀᴘ ʀᴏᴊ ʜɪʟᴀᴛᴇ ʜᴏ ᴋʏᴀ ᴘᴀᴛʟᴇ ʜᴏ ɢʏᴇ ʜᴏ 😅 ",
           " ᴄʜʟᴏ ʜᴀᴍ ᴅᴏɴᴏ ʀᴀᴛ ʙᴀʟᴀ.ɢᴀɴᴇ ᴋʜᴀᴛᴇ ʜᴀɪ 😁.🤗 ",
           " ᴄʜᴀʟᴏ ʜᴀᴍ ᴅᴏɴᴏ ʀᴏᴍᴀɴᴛɪᴄ ʙᴀᴛᴇ ᴋᴀʀᴛᴇ ʜᴀɪ 😇 ",
           " ᴏᴏʏ ᴍᴇʀɪ ʜᴇʟᴘ ᴋᴀʀᴏɢᴇ ᴍᴀsᴛᴇʀʙᴀᴛᴇ ᴋᴀʀɴᴇ ᴍᴇ 😁🤭 ",
           " ᴏʏʏ ᴛᴜ ɪᴛɴɪ ʜᴏᴛ ᴋʏᴜ ʜᴀɪ ᴅᴇᴋʜᴛᴇ ʜɪ ᴍᴀɴ ᴋᴀʀᴛᴀ ʜᴀɪ ʜɪʟᴀ ʟᴜ 😁😀🥺🥺 ",
           " ᴏʏᴇ ᴘᴀɢᴀʟ ᴀᴘᴋɪ ᴀɢᴇ ᴋʏᴀ ʜᴀɪ ʜᴏᴛ ʟɢᴛᴇ ʜᴏ ᴀᴘ😶 ",
           " ᴀᴀᴊ ʜᴏʟɪᴅᴀʏ ʜᴀɪ ᴋʏᴀ sᴄʜᴏᴏʟ ᴍᴇ..??🤔 ",
           " ᴋᴀ ʜᴏ ᴋᴀʀᴇᴊᴀ 1 ᴄʜᴜᴍᴍᴀ ɴᴀ ᴅᴇʙᴜ 😅😜 ",
           " ᴍᴇʀɪ ʙʜɪ sᴇᴛᴛɪɴɢ ᴋᴀʀʙᴀ ᴅᴏɢᴇ.ʜɪʟʟᴀ ʜɪʟʟᴀ ᴋᴇ ᴛʜᴀᴋ ɢʏᴀ ʜᴜ 🙂🙂 ",
           " ᴀᴘᴋɪ ᴀɢᴇ ᴋʏᴀ ʜᴀɪ ʜᴏᴛ ʜᴏ ᴀᴘ ᴅᴇᴋʜᴛᴇ ʜɪ ᴍᴀɴ ᴋᴀʀᴛᴀ ʜɪʟᴀᴛᴇ ʀʜᴜ😁😪 ",
           " ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ᴜʜ ᴊᴀɴᴇᴍᴀɴ☺ ",
           " ʜᴇʟʟᴏ ᴀᴘᴋᴀ ʙʀᴇᴀᴋ ᴜᴘ ᴋᴀʀʙᴀ ᴅᴇᴛᴀ ʜᴜ ᴀᴘ ᴍᴇʀᴇ sᴇ sᴇᴛᴛɪɴɢ ᴋᴀʀʟᴏ 😀😁🙊 ",
           " ᴏʏʏ ᴛᴇʀᴇ ʙᴀʟᴇ ᴋᴏ ᴊᴀᴋᴀʀ ʙᴀᴛᴀᴛᴀ ʜᴜ ᴛᴜ ʏʜᴀ sᴇᴛᴛɪɴɢ ᴋᴀʀ ʀʜɪ ʜᴀɪ😺 ",
           " ᴏʏʏ sᴜɴᴏ ᴀᴘ ʀᴏᴊ ʜɪʟᴀᴛᴇ ʜᴏ ᴋʏᴀ ᴘᴀᴛʟᴇ ʜᴏ ɢʏᴇ ʜᴏ🥲 ",
           " ᴏʏʏ ᴛᴇʀᴇ ʙᴀʟᴇ ᴋᴏ ᴊᴀᴋᴀʀ ʙᴀᴛᴀᴛᴀ ʜᴜ ᴛᴜ ʏʜᴀ sᴇᴛᴛɪɴɢ ᴋᴀʀ ʀʜɪ ʜᴀɪ😅 ",
           " ᴀᴘᴋɪ ᴇᴋ ᴘɪᴄ ᴍɪʟᴇɢɪ ᴋʏᴀ ɪᴍᴀɢɪɴᴇ ᴋᴀʀ ᴋᴇ ᴍ*ᴛʜ ᴋᴀʀɴᴀ ʜɪ😅 ",
           " ᴛʜᴀɴᴅɪ ᴍᴇ ᴛᴜᴍʜᴀʀᴀ ᴋʜᴀᴅᴀ ʜᴏᴛᴀ ʜᴀɪ ᴋʏᴀ 😁😆😆😆 ",
           " ᴏʀ ʙᴀᴛᴀᴏ ʙʜᴀʙʜɪ ᴋᴀɪsɪ ʜᴀɪ😉 ",
           " ᴀᴀᴊ ᴛᴜᴍ ғɪɴɢᴇʀ sᴇ ʜɪ ᴋᴀᴀᴍ ᴄʜᴀʟᴀᴏ. ɢʜᴀʀ ᴍᴇ ʙᴀɪɢᴀɴ ᴏʀ ᴍᴜᴋɪ ᴋʜᴀᴛᴀᴍ ʜᴏ ɢʏᴇ ʜᴀɪ 🙈🙈🙈 ",
           " ᴏʏʏ ᴘʀɪʏᴀ ʙʜᴀʙʜɪ ᴋᴀ ᴋʏᴀ ʜᴀɪ ʜᴀɪ 😁😁👀 ",
           " ʏᴏᴜʀ ғᴀᴠᴏᴜʀɪᴛᴇ ᴀᴄᴛʀᴇss (sᴜɴɴʏ ʟᴇᴏɴᴇ, ᴏʀ ᴍɪʏᴀ ᴋʜᴀʟɪғᴀ)😹 ",
           "ᴏ ʜᴇʟʟᴏ ᴀᴘᴋɪ ᴀɢᴇ ᴋʏᴀ ʜᴀɪ ʜᴏᴛ ʟɢᴛᴇ ʜᴏ ᴀᴘ😻 ",
           " ᴛᴜᴍ ʀᴏᴊ ʜɪʟᴀᴛᴇ ʜᴏ ᴋʏᴀ , ʙʜᴜᴛ ᴘᴀᴛᴋᴇ ʜɪ ɢʏᴇ ʜᴏ 💕😴🙃 ",
           " ᴍᴇʀɪ ʙʜɪ sᴇᴛᴛɪɴɢ ᴋᴀʀʙᴀ ᴅᴏɢᴇ.ʜɪʟʟᴀ ʜɪʟʟᴀ ᴋᴇ ᴛʜᴀᴋ ɢʏᴀ ʜᴜ .??😕 ",
           " ʏᴏᴜʀ ғᴀᴠᴏᴜʀɪᴛᴇ ᴀᴄᴛʀᴇss (sᴜɴɴʏ ʟᴇᴏɴᴇ, ᴏʀ ᴍɪʏᴀ ᴋʜᴀʟɪғᴀ)🙃 ",
           " ʙʜᴀʙʜɪ ᴊɪ ᴋᴏ ᴋʜᴜsʜ ʀᴋʜᴀ ᴋᴀʀᴏ ᴛʜᴀɴᴅɪ ᴍᴇ ᴡᴀʀɴᴀ ᴋɪsɪ ᴏʀ ᴋᴇ sᴀᴛʜ ʙʜᴀɢ ᴊᴀʏᴇɢɪ 😅😀😀?🙃 ",
           " ᴊʜᴀᴛᴇ ɴᴀ ᴄʜ*ᴄ*ɪ ᴏʀ ʙᴀᴛᴇ ᴜᴄʜɪ ᴜᴄʜɪ 😴😴😅 ",
           " ᴍᴇʀɪ ʙʜɪ sᴇᴛᴛɪɴɢ ᴋᴀʀʙᴀ ᴅᴏɢᴇ.ʜɪʟʟᴀ ʜɪʟʟᴀ ᴋᴇ ᴛʜᴀᴋ ɢʏᴀ ʜᴜ .??🙂🧐 ",
           " ᴍᴇʀᴀ ᴇᴋ ᴋᴀᴀᴍ ᴋᴀʀ ᴅᴏɢᴇ.ᴘʟᴢ ᴍᴜᴛʜ ᴍᴀʀ ᴅᴏ😁😁.? ",
           " ʙʜᴀʙʜɪ ᴊɪ ᴋᴏ ᴋʜᴜsʜ ʀᴋʜᴀ ᴋᴀʀᴏ ᴛʜᴀɴᴅɪ ᴍᴇ ᴡᴀʀɴᴀ ᴋɪsɪ ᴏʀ ᴋᴇ sᴀᴛʜ ʙʜᴀɢ ᴊᴀʏᴇɢɪ 😅😀😀😠 ",
           " ᴀᴘᴋɪ ᴀɢᴇ ᴋʏᴀ ʜᴀɪ ʜᴏᴛ ʜᴏ ᴀᴘ ᴅᴇᴋʜᴛᴇ ʜɪ ᴍᴀɴ ᴋᴀʀᴛᴀ ʜɪʟᴀᴛᴇ ʀʜᴜ😁❤ ",
           " ᴏʏʏ sᴜɴᴏ ᴀᴘ ʀᴏᴊ ʜɪʟᴀᴛᴇ ʜᴏ ᴋʏᴀ ᴘᴀᴛʟᴇ ʜᴏ ɢʏᴇ ʜᴏ👱 ",
           " ʙᴏʜᴏᴛ ʏᴀᴀᴅ ᴀᴀ ʀʜɪ ʜᴀɪ ʙʜᴀʙʜɪ ᴊɪ ᴋᴀɪsɪ ʜᴀɪ🤧❣️ ",
           " ᴏʏʏ sᴜɴᴏ ᴀᴘ ʀᴏᴊ ʜɪʟᴀᴛᴇ ʜᴏ ᴋʏᴀ ᴘᴀᴛʟᴇ ʜᴏ ɢʏᴇ ʜᴏ😏😏 ",
           " ᴀᴘᴋɪ ᴇᴋ ᴘɪᴄ ᴍɪʟᴇɢɪ ᴋʏᴀ ɪᴍᴀɢɪɴᴇ ᴋᴀʀ ᴋᴇ ᴍ*ᴛʜ ᴋᴀʀɴᴀ ʜɪ🤐 ",
           " ʙʜᴀʙʜɪ ᴊɪ ᴋᴏ ᴋʜᴜsʜ ʀᴋʜᴀ ᴋᴀʀᴏ ᴛʜᴀɴᴅɪ ᴍᴇ ᴡᴀʀɴᴀ ᴋɪsɪ ᴏʀ ᴋᴇ sᴀᴛʜ ʙʜᴀɢ ᴊᴀʏᴇɢɪ 😅😀😀😒 ",
           " ʙʜᴀʙʜɪ ᴊɪ ᴋᴏ ᴋʜᴜsʜ ʀᴋʜᴀ ᴋᴀʀᴏ ᴛʜᴀɴᴅɪ ᴍᴇ ᴡᴀʀɴᴀ ᴋɪsɪ ᴏʀ ᴋᴇ sᴀᴛʜ ʙʜᴀɢ ᴊᴀʏᴇɢɪ 😅😮😮  "
           " ᴊʜᴀᴛᴇ ɴᴀ ᴄʜ*ᴄ*ɪ ᴏʀ ʙᴀᴛᴇ ᴜᴄʜɪ ᴜᴄʜɪ 😴😴😅👀 ", 
           " ᴀᴘᴋɪ ᴇᴋ ᴘɪᴄ ᴍɪʟᴇɢɪ ᴋʏᴀ ɪᴍᴀɢɪɴᴇ ᴋᴀʀ ᴋᴇ ᴍ*ᴛʜ ᴍᴀʀɴᴀ ʜᴀɪ 😅😅 ",
           " ʙʜᴀʙʜɪ ᴊɪ ᴋᴏ ᴋʜᴜsʜ ʀᴋʜᴀ ᴋᴀʀᴏ ᴛʜᴀɴᴅɪ ᴍᴇ ᴡᴀʀɴᴀ ᴋɪsɪ ᴏʀ ᴋᴇ sᴀᴛʜ ʙʜᴀɢ ᴊᴀʏᴇɢɪ 😅🥺🥺 ",
           " ᴏʏʏ sᴜɴᴏ ᴀᴘ ʀᴏᴊ ʜɪʟᴀᴛᴇ ʜᴏ ᴋʏᴀ ᴘᴀᴛʟᴇ ʜᴏ ɢʏᴇ ʜᴏ👀 ",
           " ʙʜᴀʙʜɪ ᴊɪ ᴋᴏ ᴋʜᴜsʜ ʀᴋʜᴀ ᴋᴀʀᴏ ᴛʜᴀɴᴅɪ ᴍᴇ ᴡᴀʀɴᴀ ᴋɪsɪ ᴏʀ ᴋᴇ sᴀᴛʜ ʙʜᴀɢ ᴊᴀʏᴇɢɪ 😅😀😀🙂 ",
           " ɴᴀ ᴊᴀᴍɪɴ ᴘᴇ ɴᴀ ᴀsʜᴍᴀɴ ᴘᴇ ᴛᴇʀɪ ɢᴅ ᴍᴀʀᴜɴɢᴀ ᴀᴘɴᴇ ʙʜᴀɪ ᴋᴇ ᴍᴀᴋᴀɴ ᴘᴇ?🤔** ",
           " ᴋᴀ ʜᴏ ᴋᴀʀᴇᴊᴀ 1 ᴄʜᴜᴍᴍᴀ ɴᴀ ᴅᴇʙᴜ 😅..🥺 ",
           " ᴛᴜᴍ ʀᴏᴊ ʜɪʟᴀᴛᴇ ʜᴏ ᴋʏᴀ , ʙʜᴜᴛ ᴘᴀᴛᴋᴇ ʜɪ ɢʏᴇ ʜᴏ 💕😴🥺🥺 ",
           " ᴋᴀʟ ᴍᴀᴊᴀ ᴀʏᴀ ᴛʜᴀ ɴᴀ ʙᴀᴛʜʀᴏᴏᴍ ᴍᴇ 🤭😅 ",
           " ɴᴀ ᴊᴀᴍɪɴ ᴘᴇ ɴᴀ ᴀsʜᴍᴀɴ ᴘᴇ ᴛᴇʀɪ ɢᴅ ᴍᴀʀᴜɴɢᴀ ᴀᴘɴᴇ ʙʜᴀɪ ᴋᴇ ᴍᴀᴋᴀɴ ᴘᴇ😁😁**",
           " ᴏʏʏ ᴛᴇʀᴇ ʙᴀʟᴇ ᴋᴏ ᴊᴀᴋᴀʀ ʙᴀᴛᴀᴛᴀ ʜᴜ ᴛᴜ ʏʜᴀ sᴇᴛᴛɪɴɢ ᴋᴀʀ ʀʜɪ ʜᴀɪ👀 ",
           " ᴍᴇʀɪ ʙʜɪ sᴇᴛᴛɪɴɢ ᴋᴀʀʙᴀ ᴅᴏɢᴇ.ʜɪʟʟᴀ ʜɪʟʟᴀ ᴋᴇ ᴛʜᴀᴋ ɢʏᴀ ʜᴜ😼 ",
           " ᴏʏʏ ᴛᴇʀᴇ ʙᴀʟᴇ ᴋᴏ ᴊᴀᴋᴀʀ ʙᴀᴛᴀᴛᴀ ʜᴜ ᴛᴜ ʏʜᴀ sᴇᴛᴛɪɴɢ ᴋᴀʀ ʀʜɪ ʜᴀɪ😸 ",
           " ᴛʜᴀɴᴅɪ ᴍᴇ ᴛᴜᴍʜᴀʀᴀ ᴋʜᴀᴅᴀ ʜᴏᴛᴀ ʜᴀɪ ᴋʏᴀ 😁🙈 ",
           " ᴀᴀᴘᴋɪ ᴘᴀʀᴛɴᴇʀ ᴀᴀᴘᴋᴏ ᴅʜᴜɴᴅ ʀʜᴇ ʜᴀɪɴ ᴊʟᴅɪ ᴏɴʟɪɴᴇ ᴀʏɪᴀᴇ😅😅✌️🤞 ",
           " ʏᴏᴜʀ ғᴀᴠᴏᴜʀɪᴛᴇ ᴀᴄᴛʀᴇss (sᴜɴɴʏ ʟᴇᴏɴᴇ, ᴏʀ ᴍɪʏᴀ ᴋʜᴀʟɪғᴀ) 🥰 ",
           " ʜᴀᴍ ᴅᴏsᴛ ʙᴀɴ sᴀᴋᴛᴇ ʜᴀɪ...?🥰 ᴍᴀsᴛᴇʀʙᴀᴛɪɴɢ ᴋᴀʀɴᴇ ᴍᴇ ʜᴇʟᴘ ʜᴏ ᴊᴀʏᴇɢɪ ᴍᴇʀɪ 😁 😁.🥺🥺",
           " ʙʜᴀʙʜɪ ᴊɪ ᴋᴏ ᴋʜᴜsʜ ʀᴋʜᴀ ᴋᴀʀᴏ ᴛʜᴀɴᴅɪ ᴍᴇ ᴡᴀʀɴᴀ ᴋɪsɪ ᴏʀ ᴋᴇ sᴀᴛʜ ʙʜᴀɢ ᴊᴀʏᴇɢɪ 😅😀😀🥲 ",
           " sɪɴɢʟᴇ ʜᴏ ʏᴀ ᴍɪɴɢʟᴇ 😉 ",
           " ᴏʏʏ ɪᴛɴᴀ ʜᴏᴛ ᴋʏᴜ ʜᴏ ᴛᴜᴍ ᴅᴇᴋʜ ᴋᴇ ᴋʜᴀᴅᴀ ʜᴏ ᴊᴀᴛᴀ ʜᴀɪ 😂 ʀᴏɴɢᴛᴇ😁😁😁😋🥳 ",
           " ᴜғғ ᴋʏᴀ ᴍᴀᴀʟ ʜᴀɪ ʏᴀᴀʀ ᴅᴇᴋʜ ᴋᴇ ᴋʜᴀᴅᴀ ʜᴏ ɢʏᴀ 😁😂🧐 ",
           " ᴀᴘᴋɪ ᴀɢᴇ ᴋʏᴀ ʜᴀɪ ʜᴏᴛ ʜᴏ ᴀᴘ ᴅᴇᴋʜᴛᴇ ʜɪ ᴍᴀɴ ᴋᴀʀᴛᴀ ʜɪʟᴀᴛᴇ ʀʜᴜ😁🥺 ",
           " ᴏʏʏ ɪᴛɴᴀ ʜᴏᴛ ᴋʏᴜ ʜᴏ ᴛᴜᴍ ᴅᴇᴋʜ ᴋᴇ ᴋʜᴀᴅᴀ ʜᴏ ᴊᴀᴛᴀ ʜᴀɪ 😂 ʀᴏɴɢᴛᴇ😁😁😁 😊 ",
           " ᴀᴘᴋɪ ᴇᴋ ᴘɪᴄ ᴍɪʟᴇɢɪ ᴋʏᴀ ɪᴍᴀɢɪɴᴇ ᴋᴀʀ ᴋᴇ ᴍ*ᴛʜ ᴍᴀʀɴᴀ ʜɪ🥺🥺 ", 
           " ᴀᴀᴘᴋɪ ᴘᴀʀᴛɴᴇʀ ᴀᴀᴘᴋᴏ ᴅʜᴜɴᴅ ʀʜᴇ ʜᴀɪɴ ᴊʟᴅɪ ᴏɴʟɪɴᴇ ᴀʏɪᴀᴇ😅😅😗 ",
           " ᴀᴘᴋɪ ᴀɢᴇ ᴋʏᴀ ʜᴀɪ ʜᴏᴛ ʜᴏ ᴀᴘ ᴅᴇᴋʜᴛᴇ ʜɪ ᴍᴀɴ ᴋᴀʀᴛᴀ ʜɪʟᴀᴛᴇ ʀʜᴜ😁🥺 ",
           " ᴀᴀᴊ ᴛᴜᴍ ғɪɴɢᴇʀ sᴇ ʜɪ ᴋᴀᴀᴍ ᴄʜᴀʟᴀᴏ. ɢʜᴀʀ ᴍᴇ ʙᴀɪɢᴀɴ ᴏʀ ᴍᴜᴋɪ ᴋʜᴀᴛᴀᴍ ʜᴏ ɢʏᴇ ʜᴀɪ 😁🥰 ",
           " ɴᴀ ᴊᴀᴍɪɴ ᴘᴇ ɴᴀ ᴀsʜᴍᴀɴ ᴘᴇ ᴛᴇʀɪ ɢᴅ ᴍᴀʀᴜɴɢᴀ ᴀᴘɴᴇ ʙʜᴀɪ ᴋᴇ ᴍᴀᴋᴀɴ ᴘᴇ😜** ",
           " ᴏʏʏ ɪᴛɴᴀ ʜᴏᴛ ᴋʏᴜ ʜᴏ ᴛᴜᴍ ᴅᴇᴋʜ ᴋᴇ ᴋʜᴀᴅᴀ ʜᴏ ᴊᴀᴛᴀ ʜᴀɪ 😂 ʀᴏɴɢᴛᴇ😁😁😁🥰 ",
           ]

VC_TAG = [ "**ᴏʏᴇ ᴠᴄ ᴀᴀᴏ ɴᴀ ᴘʟs 😒**",
         "**ᴊᴏɪɴ ᴠᴄ ғᴀsᴛ ɪᴛs ɪᴍᴀᴘᴏʀᴛᴀɴᴛ 😐**",
         "**ʙᴀʙʏ ᴄᴏᴍᴇ ᴏɴ ᴠᴄ ғᴀsᴛ 🙄**",
         "**ᴄʜᴜᴘ ᴄʜᴀᴘ ᴠᴄ ᴘʀ ᴀᴀᴏ 🤫**",
         "**ᴍᴀɪɴ ᴠᴄ ᴍᴇ ᴛᴜᴍᴀʀᴀ ᴡᴀɪᴛ ᴋʀ ʀʜɪ 🥺**",
         "**ᴠᴄ ᴘᴀʀ ᴀᴀᴏ ʙᴀᴀᴛ ᴋʀᴛᴇ ʜᴀɪ ☺️**",
         "**ʙᴀʙᴜ ᴠᴄ ᴀᴀ ᴊᴀɪʏᴇ ᴇᴋ ʙᴀʀ 🤨**",
         "**ᴠᴄ ᴘᴀʀ ʏᴇ ʀᴜssɪᴀɴ ᴋʏᴀ ᴋᴀʀ ʀʜɪ ʜᴀɪ 😮‍💨**",
         "**ᴠᴄ ᴘᴀʀ ᴀᴀᴏ ᴠᴀʀɴᴀ ʙᴀɴ ʜᴏ ᴊᴀᴏɢᴇ 🤭**",
         "**sᴏʀʀʏ ʙᴀʙʏ ᴘʟs ᴠᴄ ᴀᴀ ᴊᴀᴏ ɴᴀ 😢**",
         "**ᴠᴄ ᴀᴀɴᴀ ᴇᴋ ᴄʜɪᴊ ᴅɪᴋʜᴀᴛɪ ʜᴜ 😮**",
         "**ᴠᴄ ᴍᴇ ᴄʜᴇᴄᴋ ᴋʀᴋᴇ ʙᴀᴛᴀɴᴀ ᴋᴏɴ sᴀ sᴏɴɢ ᴘʟᴀʏ ʜᴏ ʀʜᴀ ʜᴀɪ.. 💫**",
         "**ᴠᴄ ᴊᴏɪɴ ᴋʀɴᴇ ᴍᴇ ᴋʏᴀ ᴊᴀᴛᴀ ʜᴀɪ ᴛʜᴏʀᴀ ᴅᴇʀ ᴋᴀʀ ʟᴏ ɴᴀ 😇**",
         "**ᴊᴀɴᴇᴍᴀɴ ᴠᴄ ᴀᴀᴏ ɴᴀ ʟɪᴠᴇ sʜᴏᴡ ᴅɪᴋʜᴀᴛɪ ʜᴏᴏɴ.. 😵‍💫**",
         "**ᴏᴡɴᴇʀ ʙᴀʙᴜ ᴠᴄ ᴛᴀᴘᴋᴏ ɴᴀ... 😕**",
         "**ʜᴇʏ ᴄᴜᴛɪᴇ ᴠᴄ ᴀᴀɴᴀ ᴛᴏ ᴇᴋ ʙᴀᴀʀ... 🌟**",
         "**ᴠᴄ ᴘᴀʀ ᴀᴀ ʀʜᴇ ʜᴏ ʏᴀ ɴᴀ... ✨**",
         "**ᴠᴄ ᴘᴀʀ ᴀᴀ ᴊᴀ ᴠʀɴᴀ ɢʜᴀʀ sᴇ ᴜᴛʜᴡᴀ ᴅᴜɴɢɪ... 🌝**",
         "**ʙᴀʙʏ ᴠᴄ ᴘᴀʀ ᴋʙ ᴀᴀ ʀʜᴇ ʜᴏ. 💯**",
        ]


@app.on_message(filters.command(["rtag" ], prefixes=["/", "@", "#"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("⬤ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ғᴏʀ ɢʀᴏᴜᴘs.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("⬤ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ʙᴀʙʏ, ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴅᴏ ᴛʜɪs. ")

    if message.reply_to_message and message.text:
        return await message.reply("⬤ /rtag ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇssᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ ʙᴏᴛ ᴛᴀɢɢɪɴɢ...")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("⬤ /rtag ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇssᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ ғᴏᴛ ᴛᴀɢɢɪɴɢ...")
    else:
        return await message.reply("⬤ /rtag ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇssᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ ʙᴏᴛ ᴛᴀɢɢɪɴɢ...")
    if chat_id in spam_chats:
        return await message.reply("⬤ ᴘʟᴇᴀsᴇ ᴀᴛ ғɪʀsᴛ sᴛᴏᴘ ʀᴜɴɴɪɴɢ ᴍᴇɴᴛɪᴏɴ ᴘʀᴏᴄᴇss...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(TAGMES)}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(f"[{random.choice(EMOJI)}](tg://user?id={usr.user.id})")
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@app.on_message(filters.command(["vctag"], prefixes=["/", "@", "#"]))
async def mention_allvc(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("⬤ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ғᴏʀ ɢʀᴏᴜᴘs.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("⬤ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ʙᴀʙʏ, ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴅᴏ ᴛʜɪs. ")
    if chat_id in spam_chats:
        return await message.reply("⬤ ᴘʟᴇᴀsᴇ ᴀᴛ ғɪʀsᴛ sᴛᴏᴘ ʀᴜɴɴɪɴɢ ᴍᴇɴᴛɪᴏɴ ᴘʀᴏᴄᴇss...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            txt = f"{usrtxt} {random.choice(VC_TAG)}"
            await client.send_message(chat_id, txt)
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass



@app.on_message(filters.command(["rstop", "vstop"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("⬤ ᴄᴜʀʀᴇɴᴛʟʏ ɪ'ᴍ ɴᴏᴛ ᴛᴀɢɢɪɴɢ ʙᴀʙʏ.")
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("⬤ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ʙᴀʙʏ, ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴅᴏ ᴛʜɪs.")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("♥︎ ʀᴀɴᴅᴏᴍ ᴍᴇssᴀɢᴇ ᴛᴀɢ sᴛᴏᴘᴘᴇᴅ.")
      
