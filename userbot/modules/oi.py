from time import sleep
from userbot.events import register


@register(outgoing=True, pattern='^.kyy(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Hai Perkenalkan Namaku Kyy`")
    sleep(3)
    await typew.edit("`19 Tahun`")
    sleep(1)
    await typew.edit("`Tinggal Dibatam, Salam Kenal:)`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.sayang(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Cuma Mau Bilang`")
    sleep(3)
    await typew.edit("`Aku Sayang Kamu`")
    sleep(1)
    await typew.edit("`I LOVE YOU 💞`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.semangat(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Ngapain semangat`")
    sleep(3)
    await typew.edit("`Udah Nyerah saja`")
    sleep(1)
    await typew.edit("`Syukurin apa yang ada`")
# Create by myself @localheart
