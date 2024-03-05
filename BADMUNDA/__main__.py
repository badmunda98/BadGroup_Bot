import uvloop  # Comment it out if using on windows
from BADMUNDA.bot_class import BAD
import asyncio
import importlib
from pyrogram import idle
from BADMUNDA.plugins import ALL_MODULES

 

loop = asyncio.get_event_loop()


async def BAD_boot():
    for all_module in ALL_MODULES:
        importlib.import_module("BADMUNDA.plugins." + all_module)
    print("»»»» ʜᴇʀᴏᴋᴏ ʀᴏʙᴏᴛ ᴅᴇᴘʟᴏʏ sᴜᴄᴄᴇssғᴜʟʟʏ ✨ 🎉")
    await idle()
    print("»» ɢᴏᴏᴅ ʙʏᴇ ! sᴛᴏᴘᴘɪɴɢ ʙᴏᴛ.")

    
if __name__ == "__main__":
    uvloop.install() # Comment it out if using on windows
    BAD().run()
    
    
