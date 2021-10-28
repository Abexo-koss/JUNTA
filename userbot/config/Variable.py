
import os
from .vars import Config
ENV = bool(os.environ.get("ENV", False))

if ENV:
    from userbot.Config import Config
else:
    if os.path.exists("exampleconfig.py"):
        from exampleconfig import Development as Config


variable_list = [
    "ALIVE_MSG",
    "ALIVE_PIC",
    "AWAKE_PIC",
    "AWAKE_MSG",
    "BIO_MSG",
    "YOUR_GROUP",
    "PM_MSG",
    "OP_PIC",
    "PMP_PIC",
    "YOUR_CHANNEL",
    "ALIVE_NAME",
]
