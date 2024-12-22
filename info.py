import re, logging
from os import environ
from Script import script

def is_enabled(type, value):
    data = environ.get(type, str(value))
    if data.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif data.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        print(f'Error - {type} is invalid, exiting now')
        exit()

def is_valid_ip(ip):
    ip_pattern = r'\b(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b'
    return re.match(ip_pattern, ip) is not None

# Bot information
API_ID = environ.get('API_ID', '22549633')  #api id of your telegram id
if len(API_ID) == 0:
    print('Error - API_ID is missing, exiting now')
    exit()
else:
    API_ID = int(API_ID)
API_HASH = environ.get('API_HASH', '34d8c9887fe445c1dac2228cbdf9ab48') #api hash of your telegram id
if len(API_HASH) == 0:
    print('Error - API_HASH is missing, exiting now')
    exit()
BOT_TOKEN = environ.get('BOT_TOKEN', '7614100178:AAHkWNBVGwz_KHTsHVtPN9S36ZhU73DiFJ8') #bot token from botfather
if len(BOT_TOKEN) == 0:
    print('Error - BOT_TOKEN is missing, exiting now')
    exit()
PORT = int(environ.get('PORT', '80')) #don't change anything 

# Bot pics
PICS = (environ.get('PICS', 'https://graph.org/file/3e5e98a78417b7701b550-3ac486fdf6bb7eb340.jpg https://graph.org/file/4aa13337155a29b932ffd-7ab703a89aeeeca896.jpg https://graph.org/file/50db43d87e203f4b63238-e33bba9c2996d23a21.jpg https://graph.org/file/647d1e6bd00d45cff21e0-d7d9fac281143b464d.jpg https://graph.org/file/5d400388bd8b187c9cd1e-3087fb954f07febbe3.jpg https://graph.org/file/28fd50a92459df899e8ec-2b279a1e4af85dc54a.jpg')).split()

# Bot Admins
ADMINS = environ.get('ADMINS', '2057170163 6835418766 7802198323') #apni tg id daalo
if len(ADMINS) == 0:
    print('Error - ADMINS is missing, exiting now')
    exit()
else:
    ADMINS = [int(admins) for admins in ADMINS.split()]

# Channels
INDEX_CHANNELS = [int(index_channels) if index_channels.startswith("-") else index_channels for index_channels in environ.get('INDEX_CHANNELS', '-1001850355982').split()]
if len(INDEX_CHANNELS) == 0:
    print('Info - INDEX_CHANNELS is empty')
AUTH_CHANNEL = [int(auth_channels) for auth_channels in environ.get('AUTH_CHANNEL', '-1002224811479').split()]
if len(AUTH_CHANNEL) == 0:
    print('Info - AUTH_CHANNEL is empty')
LOG_CHANNEL = environ.get('LOG_CHANNEL', '-1001995831309') #bot log channel -1005293546253
if len(LOG_CHANNEL) == 0:
    print('Error - LOG_CHANNEL is missing, exiting now')
    exit()
else:
    LOG_CHANNEL = int(LOG_CHANNEL)
IS_FSUB = is_enabled('IS_FSUB', True)

# support group
SUPPORT_GROUP = environ.get('SUPPORT_GROUP', 'https://t.me/+KNZcFUERE9RhN2E9') #support group id ex:  -1002936246860
if len(SUPPORT_GROUP) == 0:
    print('Error - SUPPORT_GROUP is missing, exiting now')
    exit()

# MongoDB information
DATABASE_URL = environ.get('DATABASE_URL', "mongodb+srv://V2Premium:LLdf8Z2nIr48bzTi@v2premium.ryila.mongodb.net/?retryWrites=true&w=majority&appName=V2Premium") #mongo db url
if len(DATABASE_URL) == 0:
    print('Error - DATABASE_URL is missing, exiting now')
    exit()
DATABASE_NAME = environ.get('DATABASE_NAME', "V2_PREMIUM")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Files')

# Links
SUPPORT_LINK = environ.get('SUPPORT_LINK', 'https://t.me/+KNZcFUERE9RhN2E9')
UPDATES_LINK = environ.get('UPDATES_LINK', 'https://t.me/V2_PREMIUM')
FILMS_LINK = environ.get('FILMS_LINK', 'https://t.me/VIRUS_STUDIOS_MOVIES')
TUTORIAL = environ.get("TUTORIAL", "https://t.me/Virus_Botz/55")
VERIFY_TUTORIAL = environ.get("VERIFY_TUTORIAL", "https://t.me/Virus_Botz/52")

# Bot settings
DELETE_TIME = int(environ.get('DELETE_TIME', 3600)) # Add time in seconds 
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
MAX_BTN = int(environ.get('MAX_BTN', 10)) #don't change anything in Language 
LANGUAGES = [language.lower() for language in environ.get('LANGUAGES', 'english hindi telugu tamil kannada malayalam').split()]
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", script.IMDB_TEMPLATE)
FILE_CAPTION = environ.get("FILE_CAPTION", script.FILE_CAPTION)
SHORTLINK_URL = environ.get("SHORTLINK_URL", "instantearn.in")
SHORTLINK_API = environ.get("SHORTLINK_API", "390b93d6cc4c6843fdaa7db0eff92f8c3819dacb")
VERIFY_EXPIRE = int(environ.get('VERIFY_EXPIRE', 86400)) # Add time in seconds
WELCOME_TEXT = environ.get("WELCOME_TEXT", script.WELCOME_TEXT)
INDEX_EXTENSIONS = [extensions.lower() for extensions in environ.get('INDEX_EXTENSIONS', 'mp4 mkv').split()]
STICKERS_IDS = (
    "CAACAgUAAxkBAAIq4GcLuVcGzLFjzmuLAim3O8SR7-QeAAJiFAACNUZgVGUa8UCdFTy-NAQ"
).split()

# boolean settings 
GROUP_FSUB = is_enabled('GROUP_FSUB', True) 
PM_SEARCH = is_enabled('PM_SEARCH', True) #switch True or False for searching results in bot pm😃
IS_VERIFY = is_enabled('IS_VERIFY', False)
AUTO_DELETE = is_enabled('AUTO_DELETE', True)
WELCOME = is_enabled('WELCOME', True)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)
LONG_IMDB_DESCRIPTION = is_enabled("LONG_IMDB_DESCRIPTION", False)
LINK_MODE = is_enabled("LINK_MODE", True)
AUTO_FILTER = is_enabled('AUTO_FILTER', True)
IMDB = is_enabled('IMDB', True)
SPELL_CHECK = is_enabled("SPELL_CHECK", True)
SHORTLINK = is_enabled('SHORTLINK', False)


PAYMENT_QR = environ.get('PAYMENT_QR', 'https://graph.org/file/571b4b689b6f0d8ab279e-e715961e20edeb0d61.jpg') #telegraph link of your QR code 
UPI_ID = environ.get('UPI_ID', 'gsiegsue@axl') # Add your upi id here
# for stream
IS_STREAM = is_enabled('IS_STREAM', True) #true if you want stream feature active in your bot
BIN_CHANNEL = environ.get("BIN_CHANNEL", "-1001995831309") #if is_stream = true then add a channel id ex: -10026393639
if len(BIN_CHANNEL) == 0:
    print('Error - BIN_CHANNEL is missing, exiting now')
    exit()
else:
    BIN_CHANNEL = int(BIN_CHANNEL)
URL = environ.get("URL", "") #if heroku then paste the app link here ex: https://heroku......./
if len(URL) == 0:
    print('Error - URL is missing, exiting now')
    exit()
else:
    if URL.startswith(('https://', 'http://')):
        if not URL.endswith("/"):
            URL += '/'
    elif is_valid_ip(URL):
        URL = f'http://{URL}/'
    else:
        print('Error - URL is not valid, exiting now')
        exit()
