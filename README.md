# DiscoDino - Bot de Música para Discord

DiscoDino es un proyecto de un bot para Discord diseñado para la reproducción de música, desarrollado en Python.

<div align="center">
  <a href="https://github.com/Eduu64/Discord-music-bot/assets/64559740/87b90a3b-f284-40c7-8649-f7f8d50b1a84">
    <img src="https://github.com/Eduu64/Discord-music-bot/assets/64559740/87b90a3b-f284-40c7-8649-f7f8d50b1a84" alt="banner" height="auto" width="200" style="border-radius: 50%" />
  </a>
</div>

## Ventajas

- Permite reproducir canciones o listas de reproducción desde YouTube.
- Gestiona colas de reproducción para una experiencia continua de reproducción.
- Código fácil de entender y modificar.
- Instalación compacta y sencilla.

## Dependencias

- PyNaCl
- Asyncio
- FFmpeg (se requiere seguir un tutorial de instalación)
- Discord.py
- pytube

## Librerías

- discord
- asyncio
- pytube 
- datetime
- random
- re
- os

## Comandos (PREFIJO '!')

### `!cola`

Muestra la cola de reproducción actual.

<div align="center">
  <a href="https://github.com/Eduu64/Discord-music-bot/assets/64559740/b8fea4da-3794-4911-acee-d5a31608e005">
    <img src="https://github.com/Eduu64/Discord-music-bot/assets/64559740/b8fea4da-3794-4911-acee-d5a31608e005" alt="cola" height="auto" width="200" style="border-radius: 50%;" />
  </a>
</div>

### `!help`

Muestra este mensaje de ayuda.

<div align="center">
  <a href="https://github.com/Eduu64/Discord-music-bot/assets/64559740/ec6d470e-b91b-46be-a3df-38a93e05ac70">
    <img src="https://github.com/Eduu64/Discord-music-bot/assets/64559740/ec6d470e-b91b-46be-a3df-38a93e05ac70" alt="help" height="auto" width="200" style="border-radius: 50%;" />
  </a>
</div>

### `!info`

Obtén información sobre el bot.

<div align="center">
  <a href="https://github.com/Eduu64/Discord-music-bot/assets/64559740/d8b31260-022d-47d6-b7b9-f95776282da1">
    <img src="https://github.com/Eduu64/Discord-music-bot/assets/64559740/d8b31260-022d-47d6-b7b9-f95776282da1" alt="info" height="auto" width="200" style="border-radius: 50%;" />
  </a>
</div>

### `!play`

Añade una canción a la cola de reproducción.

- Reproduce canciones de YouTube (ya sea una URL de playlist o una canción individual) y también permite la búsqueda por nombre.

<div align="center">
  <a href="https://github.com/Eduu64/Discord-music-bot/assets/64559740/4dd58840-6d45-42a9-9765-0c9a006d9b8d">
    <img src="https://github.com/Eduu64/Discord-music-bot/assets/64559740/4dd58840-6d45-42a9-9765-0c9a006d9b8d" alt="play1" height="auto" width="200" style="border-radius: 50%;" />
  </a>
</div>

<div align="center">
  <a href="https://github.com/Eduu64/Discord-music-bot/assets/64559740/f4c7c4a2-4541-424e-80ee-6fae8d686824">
    <img src="https://github.com/Eduu64/Discord-music-bot/assets/64559740/f4c7c4a2-4541-424e-80ee-6fae8d686824" alt="play2" height="auto" width="200" style="border-radius: 50%;" />
  </a>
</div>

### `!skip`

Salta la canción actual en reproducción.

<div align="center">
  <a href="https://github.com/Eduu64/Discord-music-bot/assets/64559740/80abb290-cfd9-4e9b-87f9-0da29c1d17d7">
    <img src="https://github.com/Eduu64/Discord-music-bot/assets/64559740/80abb290-cfd9-4e9b-87f9-0da29c1d17d7" alt="skip" height="auto" width="200" style="border-radius: 50%;" />
  </a>
</div>

### `!join`

Indica al bot unirse al canal de voz.

### `!leave`

Indica al bot abandonar el canal de voz.
