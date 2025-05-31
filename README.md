# 🐍 Python Discord Bot

A modular and extensible Discord bot built with [discord.py](https://github.com/Rapptz/discord.py) and MongoDB.

## 🚀 Features

- 🧩 **Modular Structure:** Easily add and manage commands and events.
- 🐢 **Turtle System:** Users can create and list their own turtles.
- 🛡️ **Advanced Error Handling:** User-friendly error messages and auto-deletion.
- 📦 **MongoDB Integration:** Persistent data storage support.
- ⚡ **Easy Setup & Run:** Quick start with Makefile and .env support.

## 📦 Installation

```bash
git clone https://github.com/Xjectro/python-discord-bot.git
cd python-discord-bot
python -m venv venv
venv\Scripts\activate  # For Windows
# or
source venv/bin/activate  # For Linux/macOS
pip install -r requirements.txt
```

Create a `.env` file and fill it as follows:

```env
BOT_TOKEN="YOUR_DISCORD_BOT_TOKEN"
PREFIX="!"
MONGODB_URI="mongodb://localhost:27017/python-discord-bot"
```

## ⚙️ Usage

```bash
python main.py
```
or
```bash
make run
```

## 📁 Commands

- `!create_turtle <name>` — Creates a new turtle.
- `!list_turtles` — Lists all turtles.

For more commands, check the code or look in the `cogs/` folder.

## 🤝 Contributing

Pull requests and suggestions are welcome! Please open an issue first to discuss what you would like to change.

## 📝 License

MIT License © 2025 Xjectro
