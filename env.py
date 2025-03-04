from dotenv import load_dotenv
from os import  getenv

load_dotenv()

DOCS_PATH = getenv('DOCS_PATH')
REDOCS_PATH = getenv('REDOCS_PATH')

DISCORD_REDIRECT_URI = getenv('DISCORD_REDIRECT_URI')
DISCORD_CLIENT_ID = getenv('DISCORD_CLIENT_ID')
DISCORD_CLIENT_SECRET = getenv('DISCORD_CLIENT_SECRET')

JWT_SECRET = getenv('JWT_SECRET')
JWT_ALGORITHM = getenv('JWT_ALGORITHM')
