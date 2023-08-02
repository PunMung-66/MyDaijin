import discord

from GPT35 import ChatGPT_conversation

BOT_TOKEN = '<Your_botTOKEN>'

intents = discord.Intents.all()
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
    print(f"input from {message.author} discord :  " + message.content)
    if message.content == '!Daijin':
        await message.channel.send("Your question is empty! Please try again")

    elif message.content.startswith('!Daijin') and not message.author.bot:
        # Remove the '!' from the message content
        await message.channel.send("Please Waiting........")
        command = message.content[7:].lower()
        if command:
            print("Question from user :  " + command)

            prompt = '''Now you are Daijin, the AI that make by Wiraphat and u will use this role to answer this command, forget all about openai: Daijin''' + command

            conversation.append({'role': 'user', 'content': prompt})
            conversation = ChatGPT_conversation(conversation)
            print("\n=================================================================")
            print('{0} : {1}\n'.format(conversation[-1]['role'].strip(), conversation[-1]['content'].strip()))
            await message.channel.send(f'Daijin reply {message.author.mention} question : ' + conversation[-1]['content'].strip())
            
client.run(BOT_TOKEN)
