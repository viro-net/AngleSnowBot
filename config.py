#-------------------------------------- https://github.com/Snowball-0/AngleSnowBot ------------------------------------------#
import os

class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6592197417:AAG263QISu8hTU8sLf6Hp065xdnOy5TwkCw")
    APP_ID = int(os.environ.get("APP_ID", "21288218"))
    API_HASH = os.environ.get("API_HASH", "dd47d5c4fbc31534aa764ef9918b3acd")
    ADMIN = int(os.environ.get("ADMIN", "6065594762"))
