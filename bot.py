import discord

from GPT35 import ChatGPT_conversation

BOT_TOKEN = 'MTEwMTUyNTk0NTMyNTczMTk4Mw.Gp32n2.xKmfV3P0JtU4uF8qUNopf71OEAKVcTiyEHGC6E'

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user.name} is ready to go!')
    print(f'Bot ID: {client.user.id}')


@client.event
async def on_ready():
    print(f'{client.user.name} is ready to go!')
    print(f'Bot ID: {client.user.id}')

@client.event
async def on_message(message):
    # Ignore messages sent by the bot itself to avoid potential infinite loops
    if message.author == client.user:
        return
    conversation = []

    # Check if the message starts with '!' and is not from a bot
    print("input from discord :  " + message.content)
    if message.content == '!Daijin':
        await message.channel.send("Your question is empty! Please try again")

    elif message.content.startswith('!Daijin') and not message.author.bot:
        # Remove the '!' from the message content
        await message.channel.send("Please Waiting........")
        command = message.content[7:].lower()
        if command:
            print("Question from user :  " + command)

            prompt = '''Now you are Daijin, the AI that make by Punnawat and u will use this role to answer this command:''' + command

            conversation.append({'role': 'user', 'content': prompt})
            conversation = ChatGPT_conversation(conversation)
            print("\n=================================================================")
            print('{0} : {1}\n'.format(conversation[-1]['role'].strip(), conversation[-1]['content'].strip()))
            await message.channel.send("Daijin : " + conversation[-1]['content'].strip())
    else:
         await message.channel.send("Please type ' !Daijin ' followed by your question")
            
client.run(BOT_TOKEN)