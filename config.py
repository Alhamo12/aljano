## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgCIFdBn4ZlusnJhz8y7YMnUGTgA6CrGR7NGJKBMzjOz11uNqYcw7B1cI6KwmnaVJn5XkvvOgWhOj780p47ehbYSgMzLcHYaecsud6LBhEQAF1bHXgCPygYwI3cxuRIOtQ4tFiFHmlh5A2t293HtCfb2ad7My4yIblPXhkeMoK0P7mtpSXUPOU4IJSVLaLMnWj006TkUKwvDz5IeAfD_Uto_Sl7x3TzX2rftCPg9vGP3PBAml2ulVsbjwp94qTPgqgZl-8ijORokH-iZA4svWICghXZvKkkT1QcpmBITKaB9Wk5UcfNjcVPyww2qKoZ0b2gMroWcrEyybljmna74aajhAAAAATqRNTEA")
BOT_TOKEN = getenv("BOT_TOKEN", "5592707723:AAExbnJ_oFY09mkJJPpdx5_IbpvtNX6w6NI")
BOT_NAME = getenv("BOT_NAME", "music")
API_ID = int(getenv("API_ID", "13124829"))
API_HASH = getenv("API_HASH", "03ed39256d133866b23b2d37ee7f3d67")
OWNER_NAME = getenv("OWNER_NAME", "jano")
OWNER_USERNAME = getenv("OWNER_USERNAME", "J_A_N_U_O_1")
ALIVE_NAME = getenv("ALIVE_NAME", "jano")
BOT_USERNAME = getenv("BOT_USERNAME", "lllll_M_lllll_BOT")
OWNER_ID = getenv("OWNER_ID", "5411694700")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "ljl_a_lnl")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "akd444s")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "akd444s")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "# / ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/466de30ee0f9383c8e09e.jpg")
START_PIC = getenv("START_PIC", "")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://telegra.ph/file/6e2e0559f154fbe12735c.jpg")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/6e2e0559f154fbe12735c.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6e2e0559f154fbe12735c.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/6e2e0559f154fbe12735c.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/6e2e0559f154fbe12735c.jpg")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/6e2e0559f154fbe12735c.jpg")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/6e2e0559f154fbe12735c.jpg")
