import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

TEST_MESSAGES = int(os.getenv("TEST_CHANNEL"))

#SERVERS
BOT_TESTER = int(os.getenv("BOT_TESTER"))
FRESH = int(os.getenv("FRESH"))