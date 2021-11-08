import discord
import os
from dotenv import load_dotenv
from datetime import datetime

client = discord.Client()

gone_date = datetime(2021, 5, 28, 17, 3, 11)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'where' in message.content and 'nick' in message.content:
        then = gone_date
        now  = datetime.now()
        duration = now - then
        duration_in_s = duration.total_seconds()

        years = duration.days / 365
        num_years = int(years)
        
        days = duration.days % 365
        months = days / 30.4166666666
        num_months = int(months)

        days = days % 30.4166666666
        num_days = int(days)
 
        hours = (duration.seconds / 3600)
        num_hours = int(hours)

        hours = duration.seconds % 3600
        mins = hours / 60
        num_mins = int(mins)

        out_str = "Nick abandoned his friends! He has been gone for"

        if (num_years > 0):
            if (num_years > 1):
                app = " " + str(num_years) + " years,"
            else:
                app = " " + str(num_years) + " year,"
            out_str+=app
        if (num_months > 0):
            if (num_months > 1):
                app = " " + str(num_months) + " months,"
            else:
                app = " " + str(num_months) +  "month,"
            out_str+=app
        if (num_days > 0):
            if (num_days > 1):
                app = " " + str(num_days) + " days,"
            else:
                app = " " + str(num_days) +  "day,"
            out_str+=app
        if (num_hours > 0):
            if (num_hours > 1):
                app = " " + str(num_hours) + " hours,"
            else:
                app = " " + str(num_hours) +  "hour,"
            out_str+=app
        
        out_str = out_str[:-1]
        if (num_mins != 1):
            out_str+=" and " + str(num_mins) + " minutes."
            await message.channel.send(out_str)
        else:
            out_str+=" and " + str(num_mins) + " minute."
            await message.channel.send(out_str)
        

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client.run(token)

