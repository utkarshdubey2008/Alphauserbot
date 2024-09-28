from telethon import events
import requests

@events.register(events.NewMessage(pattern=r'\.currency (.+) (.+)'))
async def currency(event):
    amount, currency = event.pattern_match.group(1), event.pattern_match.group(2)
    response = requests.get(f"https://api.exchangerate-api.com/v4/latest/{currency}")
    data = response.json()
    if 'rates' in data:
        conversion = float(amount) * data['rates']['USD']  # Assuming conversion to USD
        await event.reply(f"{amount} {currency} is approximately {conversion:.2f} USD.")
    else:
        await event.reply("Invalid currency.")
