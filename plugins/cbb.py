# (©)LordMuda_ID
# Recode by @LordMuda_ID
# t.me/BadHuman18 & t.me/BadHumanReborn

from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from bot import Bot
from config import OWNER


@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text=f"<b>Tentang Bot ini:\n\n@{client.username} adalah Bot Telegram untuk menyimpan Postingan atau File yang dapat Diakses melalui Link Khusus.\n\n • Creator: @{OWNER}\n • Source Code: <a href='https://github.com/LordMudaID/fileuload-2'>fileuload-2</a>\n • Owner Repo: @LordMuda_ID\n\n👨‍💻 Develoved by @LordMuda_ID</b>\n",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("• ᴛᴜᴛᴜᴘ •", callback_data="close")]]
            ),
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except BaseException:
            pass
