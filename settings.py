import os
from dotenv import load_dotenv

# securely loading from the .env file
load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

TEST_MESSAGES = int(os.getenv("TEST_CHANNEL"))

# SERVERS
BOT_TESTER = int(os.getenv("BOT_TESTER"))
FRESH = int(os.getenv("FRESH"))

# Servers in list
GUILDS = [BOT_TESTER]