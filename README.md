Discord AI Chat Bot

This script allows you to set up a Discord bot that can interact with users in two main modes: sending inspirational quotes or acting as a chill and adaptive AI buddy using OpenAI's GPT model. Perfect for automating casual chats or spreading good vibes in your Discord server!

Features

Quote Mode: Sends random inspirational quotes in the channel.

AI Chat Mode: Responds to the latest message in the channel with a casual, adaptive reply.

Message Deletion: Optionally delete bot messages after a specified time.

Customizable Delay: Set intervals between actions.

Flexible Configuration: Manage tokens, channel IDs, and settings through config.yaml.

Requirements

Python 3.7+

Libraries:

requests

pyyaml

openai

A Discord bot token.

An OpenAI API key.

Installation

Clone this repository or download the script.

Install dependencies:

pip install requests pyyaml openai

edit a config.yaml file in the same directory as the script with the following structure:

BOT_TOKEN:
  - "your_discord_bot_token"

CHANNEL_ID:
  - "your_channel_id"

OPENAI_API_KEY: "your_openai_api_key"

MODE: "ai_chat"  # Options: "quote" or "ai_chat"
DELAY: 10         # Delay in seconds between actions
DEL_AFTER: false  # Delete bot messages after sending (true/false)
REPLY: true       # Reply to the last message in the channel (true/false)

Usage

Run the script:

python bot.py

The bot will start performing actions based on the mode specified in config.yaml:

Quote Mode: Sends random inspirational quotes.

AI Chat Mode: Fetches the latest message in the channel and responds casually.

Customization

To adjust the AI's tone, modify the gpt_reply function's prompt to fit your desired personality or language style.

You can enable or disable message deletion and reply behavior in config.yaml.

Example config.yaml

BOT_TOKEN:
  - OTYzMjxxx

CHANNEL_ID:
  - 123456xxxx

OPENAI_API_KEY: sk-xxxxxxxx

MODE: ai_chat
DELAY: 5
DEL_AFTER: true
REPLY: true

Troubleshooting

Invalid Token or Permissions: Ensure the bot token and channel ID are correct. Make sure the bot has permission to send messages in the specified channel.

Rate Limits: The bot might get rate-limited if performing too many actions. Increase the DELAY value if needed.

API Errors: Verify your OpenAI API key and ensure it's active.

License

This script is open-source and free to use. Modify it as needed to suit your requirements.

Enjoy your AI-powered Discord bot! 🎉