from telethon import events
import random

# List of vulgar abuses
abuses = [
    "Teri maa ka bhosda 💦✊🏻",
    "Teri maa ki chut 🍌👈🏻",
    "Teri maa ka launda 🖕🏻🥵",
    "Teri maa ka ghanta 💦",
    "Maa chod dunga teri ✊🏻",
    "Teri maa ka lauda 🍌",
    "Teri maa ko gali ke kutte chodte hain 💦",
    "Teri maa ki gand phaad dunga 🖕🏻",
    "Teri maa ka doodh piya hai kya? 🥵",
    "Teri dadi ka bhosda 🍌",
    "Teri behan ki chut 💦",
    "Behen ko chhod dunga 🖕🏻",
    "Teri maa ki aisi ki taisi ✊🏻",
    "Teri maa ko dekh ke bhabhi ko yaad aata hai 💦",
    "Chutiyapa hai tera ghar 🍌",
    "Maa behen sabki chudiya 🖕🏻",
    "Ghar ka har insaan behuda hai 🥵",
    "Teri behan ka launda 💦",
    "Tere bapu ki maa ✊🏻",
    "Teri maa ka bhashan sunne wala nahi 💦",
    "Kya teri maa kuch kar sakti hai? 🖕🏻",
    "Chutiyapan ki koi sima nahi 🍌",
    "Tere ghar mein maa ki kami hai 🥵",
    "Tere ghar ki murgi 💦",
    "Teri maa ka swag ✊🏻",
    "Teri dadi ke jaisa nahi milta 🍌",
    "Bachpan se leke ab tak sirf behuda dekh raha hoon 🖕🏻",
    "Maa behen ka rishta dekhna ho to teri maa ki taraf dekho 💦",
    "Tere ghar mein maa ko koi nahi respect karta 🍌",
    "Maa ki gaaliyan dena hi nahi milta 🖕🏻",
    "Teri maa ki aisi ki taisi kar di 💦",
    "Tere bapu ki behan ka kya hai? 🍌",
    "Tere ghar ka har bande ka bhosda 🖕🏻",
    "Tere ghar ki ma ka kya hai? 🥵",
    "Teri behan ki behudiya 💦",
    "Teri maa ki khud ki aisi ki taisi ✊🏻",
    "Behen tu kya kar rahi hai? 🍌",
    "Teri maa ko dekha to dil khush ho gaya 🖕🏻",
    "Dadi ki gaaliyan sab sunta hai 💦",
    "Ghar ka sab log chutiya hai 🍌",
    "Tere ghar ki ma ki chudiya 🖕🏻",
    "Teri maa ki khud ki kya hai? 🥵",
    "Tere behan ka ghar se bahar nikalna nahi 💦",
    "Tere ghar ka har insaan chutiya hai 🍌",
    "Teri maa ki dosti ka kya hai? 🖕🏻",
    "Tere bapu ka kya hai? 💦",
    "Teri maa ki khud ki kya hai? 🍌",
]

@client.on(events.NewMessage(pattern=r'\.raid (\w+)'))
async def raid(event):
    username = event.pattern_match.group(1)
    if username:
        await event.reply(f"@{username} {random.choice(abuses)}")
    else:
        await event.reply("Please provide a username to raid.")

@client.on(events.NewMessage(pattern=r'\.draid'))
async def stop_raid(event):
    await event.reply("Raid has been stopped.")
