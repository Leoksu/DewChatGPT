# Dewdrop
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
<a href="https://github.com/Leoksu/DewChatGPT/blob/main/LICENSE" alt="AGPLv3 license"> <img src="https://img.shields.io/badge/License-AGPLv3-blue.svg" /> </a>
</p>

<p align="center">
  A simple version of <a href="https://github.com/Leoksu/Dewdrop">Dewdrop</a>, bcz I lazy to finish that
<p/>

# Features

- [x] Interact to ChatGPT within telegram bot.
- [x] Support [custom engine model](#custom-models), see [model list](https://beta.openai.com/docs/models/gpt-3).
- [x] Set custom start, help, info text.
- [x] Easy deployable

# List to-do

- [ ] Use normal AI chat bot for main and `/ask` command for ChatGPT.
- [ ] Add jokes, story, weather, and some fun modules.
- [ ] Image recognition.

# Variables
- `API_ID` & `API_HASH` - Get this from my.telegram.org
- `BOT_TOKEN` - Visit [@BotFather](https://t.me/BotFather) and send `/newbot`. You will see instructions to create a new bot.
- `API_KEY` - First you need to create [OpenAI](https://beta.openai.com) account, and click [this](https://beta.openai.com/account/api-keys) to create new api key.
- `USERNAME` - Your bot username without @. 
> Bcz I getting confused with Client.get_me(), so you need to put bot username manually, will very thanks if someone want to help me.

# Deployment
- Run locally `VPS`:
1. Always update before do anything
```sh
apt-get update && apt-get upgrade -y
```
2. Install python and git module
```sh
apt-get install python3 git
```
3. Clone this repository 
```sh
git clone https://github.com/Leoksu/DewChatGPT && cd DewChatGPT
```
4. install all required python package
```sh
pip3 install -r requirements.txt
```
5. Copy sample.env to .env
```sh
cp sample.env .env
```
6. Fill all [variables](#variables) in .env file with your favorite text editor 
   - or just use nano, `nano .env`
7. See [Here](#custom-text) to customize bot text
8. Use screen or tmux to keep your bot running in background
```sh
screen -S dew
```
9. Finnaly run the bot
```sh
python3 dew.py
```
- Then use `CTRL+A` and `CTRL+D` to close screen
- If you want to stop the bot or check logs run `screen -r dew`
---

# Custom models

- Default model is `text-ada-001` which is faster and cheaper to avoid token limit.
- See model list and more info in [OpenAi](https://beta.openai.com/docs/models/overview) site.
- Go to [dew.py](https://github.com/Leoksu/DewChatGPT/blob/main/dew.py) file.
```sh
def generate_text(prompt):
    data = {
        'prompt': prompt,
        'model': 'text-ada-001', # edit this value to model you want
        'temperature': 0.5,
        'max_tokens': 1024, # you can also change max token in one msg
        'n': 1,
        'stop': None,
        'temperature': 0.9,
        'top_p': 0.3,
        'frequency_penalty': 0.5,
    }
```
- That's it, keep in mind that every engine models have different cost, choose the one that suits your needs.
---

# Custom text

- Set your own start text, help text, and more
- Simply go to [this](https://github.com/Leoksu/DewChatGPT/blob/main/stuff/string.py) file and edit it to your desired text
---
