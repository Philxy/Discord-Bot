import discord 
import apis


client = discord.Client()


# https://discord.com/api/oauth2/authorize?client_id=927216138847395840&permissions=84992&scope=bot


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # information
    if message.content == '$uwu':
        await message.channel.send('Hi, ich bin Phil\'s dubioser Bot! \nSchreibe   \"$uwu help\"   für meine commands \nʕ •ᴥ•ʔ')
         
    # inspiration
    if message.content.startswith('$uwu inspire'):
        quote = apis.get_quote()
        await message.channel.send(quote)    
    
    # insult
    if message.content.startswith('$uwu insult'):
        quote = apis.get_insult()
        await message.channel.send(quote)   
        
    # compliment
    if message.content.startswith('$uwu compliment'):
        await message.channel.send(message.author.name + ':  ' + apis.get_compliment())
    
    # ud definition    
    if message.content.startswith('$uwu define'):
        print(type(message.content))
        user_input = message.content.split(' ')
        user_input.pop(0)
        user_input.pop(0)
        awnser = apis.get_urban_awnser(' '.join(user_input))
        await message.channel.send(' '.join(user_input)+ ':  '  + awnser)
        
    # help    
    if message.content.startswith('$uwu help'):
        await message.channel.send('commands:\n  $uwu inspire    - inspiriere dich \n $uwu insult   - lasse dich gnadenlos beleidigen\n $uwu compliment   - wenn du traurig bist :(\n $uwu define   - gib z.B. deinen Namen ein. Findet alle Einträge im urban-dictionary.')
        
        
client.run(TOKEN)
