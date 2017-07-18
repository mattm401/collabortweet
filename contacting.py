
# Includes
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import pafy
import csv
import sys
import pandas
from matplotlib.cbook import Null

# Settings
reload(sys)
sys.setdefaultencoding('utf8')
DEVELOPER_KEY = "AIzaSyDAnNIvp8BWDMKEiyjp2PxUPlycKhmTAAI"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
pafy.set_api_key(DEVELOPER_KEY)
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)


