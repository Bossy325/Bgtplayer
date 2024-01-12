import os
import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

if os.path.exists("Internal"):
  load_dotenv("Internal")

API_ID = int(getenv("API_ID","26744258"))
API_HASH = getenv("API_HASH","7c7dbcb9e6654389d112b418e10583fa")
BOT_TOKEN = getenv("BOT_TOKEN","6516362701:AAFwYh-zvb8dtdn_trPMJXJ6uYmfj3E_S4M")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
MONGO_DB_URI = getenv("MONGO_DB_URI","mongodb+srv://Saib:saib2005@cluster0.1l0w1wa.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID","-1002023679721"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "Url shortner bot ")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6696466266").split()))
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/BikashHalderNew/Bgtplayer")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "bikash")
GIT_TOKEN = getenv("GIT_TOKEN", None)
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/holaien")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/holaien")
SUPPORT_HEHE = SUPPORT_GROUP.split("me/")[1]
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "180"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", False)
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")
PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)
YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "3"))
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)
VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))
CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "12"))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
SET_CMDS = getenv("SET_CMDS", False)
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION","BQGYFcIAjVetK2ocLWlu_obBa174JBZdmPdaSyCOYeT4yGDg4TgkiSCV6EXLuQZadXOzWgOP8mjHX5wjzdMRQ6Pd5x70pFf_3QlrY9LDt-_Tv25bG4aAOQkdSLJBsJAA9IlyvJYbpBg-vLI8ms4YODBCyA7EvHG34rKEM2KO6Ykj4B9qpBw81X3z8e47D2luVWcGcU0VZ-yj2T-Vi0zoTDGSwNB820Xdf_K-kw8XVmzme6iflEJws9gTS3C8N39OMRHIDQVw_EAnDV2cquqwtGViOJYIx1I9XDeN2lzB05OKMYWfYaXgXVKFXesd0XK1w5xlqwWgydPqtoxDsyiBlg6pH_EPLgAAAAGPI_daAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

############################
COMMAND_PREFIXES.append('')
OWNER_ID.append(6696466266)
############################
BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []
############################

START_IMG_URL = getenv("START_IMG_URL", "https://telegra.ph/God-01-09-9")
PING_IMG_URL = getenv("PING_IMG_URL", "https://te.legra.ph/file/3127b3484676bd2254e97.jpg")

PLAYLIST_IMG_URL = "https://telegra.ph/Joke-01-09"
GLOBAL_IMG_URL = "https://telegra.ph/Hi-01-05-162"
STATS_IMG_URL = "https://telegra.ph/God-01-09-9"
TELEGRAM_AUDIO_URL = "https://telegra.ph/Hi-01-05-162"
TELEGRAM_VIDEO_URL = "https://telegra.ph/Hi-01-05-162"
STREAM_IMG_URL = "https://telegra.ph/God-01-09-9"
SOUNCLOUD_IMG_URL = "https://telegra.ph/Hi-01-05-162"
YOUTUBE_IMG_URL = "https://telegra.ph/Joke-01-09"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/Hi-01-05-162"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/Joke-01-09"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/God-01-09-9"


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)

if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "resources/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            PING_IMG_URL = "https://te.legra.ph/file/3127b3484676bd2254e97.jpg"

if START_IMG_URL:
    if START_IMG_URL != "resources/Ping.jpeg":
        if not re.match("(?:http|https)://", START_IMG_URL):
            START_IMG_URL = "https://telegra.ph/God-01-09-9"
