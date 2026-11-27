import os

from dotenv import load_dotenv


load_dotenv()

class Settings:
    TOKEN: str = os.getenv('TOKEN')
    CBU_USD_URL: str = os.getenv('CBU_USD_URL')

settings = Settings()
