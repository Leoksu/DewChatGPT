from decouple import config

API_ID = config("API_ID", default=6, cast=int)
API_HASH = config("API_HASH", default="eb06d4abfb49dc3eeb1aeb98ae0f581e")
BOT_TOKEN = config("BOT_TOKEN", default=None)
API_KEY = config("API_KEY", default=None)
USERNAME= config("USERNAME", default=None)

