from telethon import TelegramClient, events
import os
from dotenv import load_dotenv
import importlib

load_dotenv()

API_ID = os.environ.get('API_ID', '29264175')  # Your actual API ID
API_HASH = os.environ.get('API_HASH', '0a3e78a4cd29529769faf5fe588f6de7')  # Your actual API hash
SESSION_STRING = os.environ.get('SESSION_STRING', '1BVtsOMMBu3xe1ZW0g9EiC24eZzCPmnX14nRc4s51_U8J5BO0DKYQNzaFgVGiFnApvFHQ4FxFcjfQ-_ZWFTtGTte7f77uPS12qYd7cqUtPs0DkgO9bzHN1LQy64GxaX1Jw4k_5rwwOiNm_PmK2MDV09-e1OMKTeyzvptOA6_O1xtHUE_w8ANai1NjrlJTVeQ04paoK8QiV0lGmDIubYucl7extnM1hozkNd5D0fqiapEoSeON7Y0I7LkalcY8-0EOQGa87hD8tSzd3xD2d7nPS4CJEDqOav7dIFZ8tZ4Pg13ZFaNPpMJ-owRECP8mmGcr-kPE6Q7y300BlSpFlsQYfiaw5xXa07o=')  # Your actual session string

client = TelegramClient('user_bot', API_ID, API_HASH).start()

# Import all plugins
for filename in os.listdir('plugin'):
    if filename.endswith('.py'):
        importlib.import_module(f'plugin.{filename[:-3]}')

@client.on(events.NewMessage)
async def handler(event):
    await client.process_event(event)

client.run_until_disconnected()
