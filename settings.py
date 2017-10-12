import os
import configparser


config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'project.ini'))

# Telegram

TELEGRAM_BOT_TOKEN = config.get('telegram', 'token')

TELEGRAM_REPORTER_ID = config.get('telegram', 'reporter_id')


# Verbix

VERBIX_CONJUGATION_URL = config.get('verbix', 'conjugation_url') 


# Misc

AVAILABLE_LANGUAGES = ['swedish', 'japanese']
