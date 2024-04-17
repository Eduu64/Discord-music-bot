# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 20:18:45 2024
@author: Eduar
"""

import discord
from discord.ext import commands
import asyncio
from discord import FFmpegPCMAudio
from pytube import YouTube
import datetime
import random
from pytube import Search
import re
from pytube import Playlist
import os


intents = discord.Intents.all()


help_command = commands.DefaultHelpCommand(
  no_category = 'Comandos',
  sort_commands = True,
)

bot = commands.Bot(command_prefix='!', 
                   intents=intents, 
                   help_command = help_command, 
                   )
queue = []
cols = [0x32a852, 0x3296a8, 0xb700ff, 0x9232a8, 0xa8326f, 0xf25207, 0x3efa00, 0xfa0000]
foto = [1,2,3,4]

@bot.command(name='join', help='Indica al bot que se una al canal de voz')
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("{} no está conectado a un canal de voz".format(ctx.message.author.name))
        return
    else:
        channel = ctx.message.author.voice.channel
    await channel.connect()

@bot.command(name='leave', help='Para que el bot abandone el canal de voz')
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect()
    else:
        await ctx.send("El bot no está conectado a un canal de voz.")



@bot.command(name='play', help='Para añadir una canción a la cola')
async def play(ctx, *, url):
          youtube_regex = r'(https?://)?(www\.)?(youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]{11})'
          playlist_regex = r'https?://(?:www\.)?youtube\.com/.*list=([a-zA-Z0-9_-]+)'

          titulo = ''

          p = []
          url_playlist = []
          playlist = False
          voice_client = ctx.guild.voice_client

          if not ctx.message.author.voice:
              await ctx.send("Debes estar en un canal de voz para utilizar este comando.")
              return
          # Verificar si el bot está conectado a un canal de voz
          if not voice_client:
              # Si el bot no está en un canal de voz, unirse al canal del autor del mensaje
              await ctx.author.voice.channel.connect()
              voice_client = ctx.guild.voice_client
          

          #link youtube playlist
          if re.match(playlist_regex, url):
            p = Playlist(url)
            for url1 in p.video_urls:
              url_playlist.append(url1)
            playlist = True
            #mensaje especial para playlist
            embed_length = discord.Embed(
              title="Añadida playlist a la cola",
              description=p.title,
              color=0xecff00,
              timestamp = datetime.datetime.now(),
              url = url,
            )
            #elige una foto random
            numero = random.choice(foto)
            nombre_archivo = f"disc{numero}.png"


            file = discord.File(f"Img/{nombre_archivo}", filename=nombre_archivo)
            gif = discord.File("tenor-ezgif.com-resize.gif")
            embed_length.set_image(url=f"attachment://{nombre_archivo}")
            embed_length.set_thumbnail(url="attachment://tenor-ezgif.com-resize.gif")
            await ctx.send(files=[file, gif], embed=embed_length)



          #link youtube normal
          elif re.match(youtube_regex, url):
            video_titulo = YouTube(url)
            titulo = video_titulo.title
            
          #busqueda por nombre
          else:
            s = Search(url)
            searchResults = s.results
            if searchResults:
              primer_resultado = searchResults[0]
              id = primer_resultado.video_id
              url = f"https://youtu.be/{id}"
              video_titulo = YouTube(url)
              titulo = video_titulo.title
              
            else:
               await ctx.send("No se encontraron resultados para la canción:", url)

        
          #mensaje para busquedas de canciones (no playlists)
          if playlist is False:
            embed_length = discord.Embed(
              title="Añadida canción a la cola",
              description=titulo,
              color=0xe67e80,
              timestamp = datetime.datetime.now(),
              url = url,
            )

            numeros_aleatorios = random.choice(foto)
            nombre_archivo = f"disc{numeros_aleatorios}.png"


            file = discord.File(f"Img/{nombre_archivo}", filename=nombre_archivo)
            gif = discord.File("tenor-ezgif.com-resize.gif")
            embed_length.set_image(url=f"attachment://{nombre_archivo}")
            embed_length.set_thumbnail(url="attachment://tenor-ezgif.com-resize.gif")
            await ctx.send(files=[file, gif], embed=embed_length)

          #añade a la cola las canciones y ejecuta la primera si es playlist y no esta ejecutando
          if playlist is True and not voice_client.is_playing():
            for cancion in url_playlist:
              #await ctx.send(cancion)
              queue.append(cancion)
            await play_next_song(ctx, voice_client)  
          #añade a la cola las canciones de la playlist 
          elif playlist is True and voice_client.is_playing():
            for cancion in url_playlist:
              queue.append(cancion)
          #añade a la cola la cancion y ejecuta la primera si no esta ejecutando
          elif len(queue) == 0 and not voice_client.is_playing():
            queue.append(url)
            await play_next_song(ctx, voice_client)  
          #añade a la cola la cancion en el resto de casos(esta ejectuando por lo tanto no ejecuta siguiente cancion)
          else:
            queue.append(url)
            


async def play_next_song(ctx, voice_client):
  if queue:
      next_url = queue.pop(0) #se guarda la cancion siguiente y se borra de la cola

      video = YouTube(next_url)
      best_audio = video.streams.get_audio_only() #obtiene audio
      song_title = video.title #titulo cancion

      audio_source = discord.FFmpegPCMAudio(
          best_audio.url,
          before_options="-reconnect 1 -reconnect_at_eof 1 -reconnect_streamed 1 -reconnect_delay_max 5"
      )

      foto_video=video.thumbnail_url #foto cancion

      embed  = discord.Embed(
        title="Reproduciendo ahora:",
        description=song_title,
        color=random.choice(cols),
        timestamp = datetime.datetime.now(),
        url = next_url,
      )
      embed.set_image(url=foto_video)
      #embed.set_thumbnail(url="https://media.tenor.com/lQ7ow7M095wAAAAi/toothless-dancing.gif")

      await ctx.send(embed=embed)

      voice_client.play(audio_source) #ejecuta el audio

      # Esperar hasta que la canción actual haya terminado de reproducirse
      while voice_client.is_playing():
          await asyncio.sleep(1)
        
      if not voice_client.is_playing():
          await play_next_song(ctx, voice_client)

@bot.command(name='skip', help='Para saltar la canción actual')
async def skip(ctx):
          voice_client = ctx.voice_client
          if voice_client and voice_client.is_playing():
              voice_client.stop()
              await ctx.send('Canción saltada.')

@bot.command(name='cola', help='Este comando muestra la cola de canciones')
async def cola(ctx):
  if len(queue) > 0:
    msg_cola = discord.Embed(
      title="Cola:",
      color=0x581845,
      timestamp = datetime.datetime.now(),
    )
    for url in queue:
      video = YouTube(url)
      song_title = video.title
      
      msg_cola.add_field(name=song_title, value="", inline=False)
    
    nombre_archivo = "banner.png"

    file = discord.File("Img/banner.png", filename=nombre_archivo)
    msg_cola.set_image(url="attachment://banner.png")
    msg_cola.set_thumbnail(url="https://media.discordapp.net/attachments/347254691966615552/1038066021300453436/maxwell.gif?ex=662b9cd1&is=661927d1&hm=9ba74602685d2dd9796d6b11160897c43b89cf3f11c35c302f9bc25ff344b10c&")
    
    await ctx.send(file=file, embed=msg_cola)
  else:
    await ctx.send('No hay canciones en la cola.')


@bot.event
async def on_ready():
    for guild in bot.guilds:
       print(f'Bot conectado a {guild.name}')
        
              
@bot.command(name='info', help='Obtén información')
async def info(ctx):
    text = "¡Mi nombre es DiscoDino!\ndescubre más escribiendo !help\n:)"

    await ctx.send(text)
  
my_secret = os.environ['TOKEN']
bot.run(my_secret) # se puede cambiar directamente por el token y quitar la varible my_secret
