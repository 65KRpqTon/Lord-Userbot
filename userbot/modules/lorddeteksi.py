# Ported From Cat Userbot For Lord Userbot By Alvin/LiuAlvinas # Jangan Hapus # Jangan Ubah
# Based On Plugins
# Alvin Ganteng

from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\.deteksi(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = "".join(event.text.split(maxsplit=1)[1:])
    reply_message = await event.get_reply_message()
    if not input_str and not reply_message:
        await edit_delete(
            event,
            "`Lord, Mohon Balas Ke Pesan Pengguna atau ketik .deteksi (ID/Username) Yang mau Anda deteksi`",
        )
    if input_str:
        try:
            uid = int(input_str)
        except ValueError:
            try:
                u = await event.client.get_entity(input_str)
            except ValueError:
                await edit_delete(
                    event, "`Lord, Mohon Berikan ID/Username untuk menemukan Riwayat`"
                )
            uid = u.id
    else:
        uid = reply_message.sender_id
    chat = "@tgscanrobot"
    event = await edit_or_reply(event, "`Memproses...`")
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message(f"{uid}")
        except YouBlockedUserError:
            await steal.reply(
                "```Lord Mohon Unblock @tgscanrobot Dan Coba Lagi```"
            )
        response = await conv.get_response()
        await event.client.send_read_acknowledge(conv.chat_id)
        await event.edit(response.text)


def inline_mention(user):
    full_name = user_full_name(user) or "No Name"
    return f"[{full_name}](tg://user?id={user.id})"


def user_full_name(user):
    names = [user.first_name, user.last_name]
    names = [i for i in list(names) if i]
    return " ".join(names)


# Alvin Ganteng
CMD_HELP.update({
    "deteksi":
        "`.deteksi`\
          \nPenjelasan: Melihat Riwayat Grup Yang Pernah/Sedang dimasuki."
})
