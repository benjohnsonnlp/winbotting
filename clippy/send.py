import json
from os import getenv

import clipboard
import discord
from discord import Message, Member, Guild

import re

TAG_RE = re.compile(r'<[^>]+>')


def remove_tags(text):
    return TAG_RE.sub('', text)


class Client(discord.Client):
    async def on_ready(self):
        print('We have logged in as {0.user}'.format(self))

    async def on_message(self, message: Message):
        print('{}: {}'.format(message.author, message.content))
        author: Member = message.author
        if author.bot:
            return

        if self.user in message.mentions:
            guild: Guild = message.guild
            my_user: Member = guild.get_member(int(config("USER_ID")))

            message_content = remove_tags(message.content).strip()
            clipboard.copy(message_content)

            await message.channel.send("{} has {} in his clipboard now".format(my_user.mention, message_content))

def config(name: str):
    if getenv(name):
        return getenv(name)
    else:
        with open('config.json') as f:
            options = json.load(f)
            return options[name]


def main():
    client = Client()
    client.run(config('BOT_KEY'))


if __name__ == '__main__':
    main()
