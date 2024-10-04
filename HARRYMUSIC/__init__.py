from HARRYMUSIC.core.bot import HARRY
from HARRYMUSIC.core.dir import dirr
from HARRYMUSIC.core.git import git
from HARRYMUSIC.core.userbot import Userbot
from HARRYMUSIC.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = HARRY()
api = SafoneAPI()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()