import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    TOKEN = os.getenv("DISCORD_TOKEN")


settings: Settings = Settings()
