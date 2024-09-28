from telethon import events
import requests

@events.register(events.NewMessage(pattern=r'\.trivia'))
async def trivia(event):
    response = requests.get("https://opentdb.com/api.php?amount=1")
    question = response.json()['results'][0]
    await event.reply(f"Question: {question['question']}\nA: {', '.join(question['incorrect_answers'] + [question['correct_answer']])}")
