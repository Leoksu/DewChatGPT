## Dewdrop
<p align="center">
  <img src="./src/ghouls.jpeg" alt="Ghouls">
</p>

<p align="center">
  <b> Telegram chat bot with OpenAI API using GPT-3 engine based on pyorgram</b>
</p>

<p align="center">
<a href="https://t.me/TheGhostOrg" alt="Telegram"> <img src="https://aleen42.github.io/badges/src/telegram.svg" /> </a>
<a href="https://github.com/Leoksu" alt="Leoksu"> <img src="https://img.shields.io/badge/Built%20by-Leoksu-blue.svg" /> </a>
<a href="https://t.me/aethersghoul" alt="Contact"> <img src="https://aleen42.github.io/badges/src/telegram.svg" /> </a>
<a href="https://www.python.org/" alt="made-with-python"> <img src="https://img.shields.io/badge/Written%20in-Python-1f425f.svg?style=flat&logo=python&color=blue" /> </a>
<a href="https://github.com/Leoksu/DewChatGPT/blob/main/LICENSE" alt="AGPLv3 license"> <img src="https://img.shields.io/badge/License-AGPL-blue.svg" /> </a>
</p>

## Features

- [x] Interact to ChatGPT within telegram bot.
- [x] Support custom engine model, see [model list](https://beta.openai.com/docs/models/gpt-3).
- [x] Set custom start, help, info text.
- [x] Easy deployable

## List to-do

- [ ] Use normal AI chat bot for main and `/ask` command for ChatGPT.
- [ ] Add jokes, story, weather, and some fun modules.
- [ ] Image recognition.

## Deployment
- Run locally `VPS`:
1. Always update before do anything
```
apt-get update && apt-get upgrade -y
```
2. Install python and git module
```
apt-get install python3 git
```
3. Clone this repository 
```
git clone https://github.com/Leoksu/DewChatGPT && cd DewChatGPT
```
4. install all required python package
```
pip3 install requirements.txt
```
5. Copy sample.env to .env
```
cp sample.env .env
```
6. Fill all variables in .env file with your favorite text editor 
   - or just use nano, `nano .env`
7. 
