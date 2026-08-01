# Stalkify

A Discord bot that "stalks" a chosen server member's Spotify activity and automatically plays whatever track they're currently listening to on your local Spotify desktop app.

## How it works

- You add the bot to a Discord server and tell it which member to watch (`st join @user`).
- Every second, the bot checks that member's Discord presence for Spotify activity.
- When it detects a new track, it kills the local Spotify process and relaunches it directly on that track via the `spotify:track:<id>` URI.

## Requirements

- **Windows** — the bot shells out to `powershell` and `taskkill`/`start spotify:...`, so it only works on a Windows machine (wherever the bot process itself runs).
- **Python 3.9+**
- **Spotify desktop app** installed and set up to handle `spotify:` URIs.
- A **Discord bot application** with a bot token.

## Setup

### 1. Create a Discord bot

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications) and create a new application.
2. Under **Bot**, create a bot user and copy its **token**.
3. Enable all **Privileged Gateway Intents** (Presence Intent, Server Members Intent, Message Content Intent) — the bot requests `Intents().all()` and reads presence data.
4. Under **OAuth2 > URL Generator**, select the `bot` scope with permissions to read messages/send messages, and use the generated URL to invite the bot to your server.

### 2. Install dependencies

```bash
pip install discord.py
```

### 3. Configure the bot token

Open `main.py` and replace the placeholder on the last line:

```python
client.run(BOT_TOKEN_HERE)
```

with your actual bot token as a string, e.g.:

```python
client.run("your-bot-token-here")
```

(Recommended: load it from an environment variable instead of hardcoding it, e.g. `client.run(os.environ["DISCORD_BOT_TOKEN"])`, so you don't accidentally commit your token.)

### 4. Run the bot

```bash
python main.py
```

If it started correctly, you'll see:

```
im alive and working!!(logged in as YourBotName#0000)
```

## Usage

In any channel the bot can see, run:

```
st join @username
```

The bot will start watching that member's Spotify activity and mirror it on your local Spotify app.

## Notes / limitations

- The bot only tracks one member at a time (the most recent `st join` target).
- Track switching relies on killing and restarting the Spotify process, so playback will briefly interrupt on every song change.
- Only tested/works on Windows due to the `powershell`/`taskkill` calls in `player()`.
