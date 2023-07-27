
import discord
import openai

openai.api_key = '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'
token = 'MTEzMzU2NTM0Mzg0ODIxNDUyOA.GBY-M1.f61e5MAjzrwRniNGhd0QTQ8a_SqH9pnex03tGA'
class MyClient(discord.Client):
    async def on_ready(self) :
        print (f'Logged on as {self.user}!')


    async def on_message(self,message) :
        print(f'message form {message.author} : {message.content}')
        if self.user!= message.author:
           if self.user in message.mentions :
             response = openai.Completion.create(
               model="text-davinci-003",
               prompt="message.content",
               temperature=1,
               max_tokens=256,
               top_p=1,
               frequency_penalty=0,
               presence_penalty=0 ,
              ) 
             channel = message.channel
             messageTosend = response.choices[0].text
             await channel.send(messageTosend)  

intents= discord.Intents.default()
intents.message_content = True      

client= MyClient(intents=intents)
client.run(token)