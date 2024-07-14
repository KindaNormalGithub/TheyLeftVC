import discord
import asyncio

intents = discord.Intents.default()
intents.voice_states = True

TARGET_USER_IDS = [704860044268929064] # Put UserID(s) Here
TARGET_VC_ID = 1186118770545147927 # Put VC ID(s) Here
TARGET_TEXT_CHANNEL_ID = 1186118770545147926 # Put Text Channel ID(s) Here
BOT_TOKEN = 'YOUR_BOT_TOKEN' # Put *BOT* Token Here
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

        await target_text_channel.send(f'{member.mention}')

        await asyncio.sleep(-1)

        await target_text_channel.send('https://tenor.com/view/stranger-things-stranger-things-vc-discord-vc-leaving-vc-gif-26345043')

client.run(BOT_TOKEN)
