# Install discord.py
# Command: pip install discord.py

import discord
import asyncio

intents = discord.Intents.default()
intents.voice_states = True

# Replace with the IDs of the people you want to track
TARGET_USER_IDS = [704860044268929064]
TARGET_VC_ID = 1186118770545147927  # Replace with the ID of the voice channel to track
TARGET_TEXT_CHANNEL_ID = 1186118770545147926  # Replace with the ID of the text channel to send the message
BOT_TOKEN = 'YOUR_BOT_TOKEN'  # Replace with your actual bot token

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!invite'):
        target_vc = client.get_channel(TARGET_VC_ID)

        if target_vc:
            invite_link = await target_vc.create_invite()
            await message.channel.send(f'Invite link: {invite_link}')
        else:
            await message.channel.send('Could not find the target voice channel.')

@client.event
async def on_voice_state_update(member, before, after):
    print(f'{member} changed voice state from {before.channel} to {after.channel}')

    if member.id in TARGET_USER_IDS and before.channel and before.channel.id == TARGET_VC_ID and not after.channel:
        target_text_channel = client.get_channel(TARGET_TEXT_CHANNEL_ID)

        # Send the ping message
        await target_text_channel.send(f'{member.mention}')

        # Introduce a delay (adjust the time as needed)
        await asyncio.sleep(-1)

        # Send the main message
        await target_text_channel.send('https://tenor.com/view/stranger-things-stranger-things-vc-discord-vc-leaving-vc-gif-26345043')

client.run(BOT_TOKEN)
