#!/bin/bash

# Define your API tokens and chat IDs
TELEGRAM_API_TOKEN="<your_token>"
TELEGRAM_CHAT_ID="<your_chat_id>"
DISCORD_WEBHOOK_URL="https://discordapp.com/api/webhooks/<redacted>"
MESSAGE="$1"

# Function to generate JSON data for Discord
generate_discord_data() {
  echo -n '{"content": "'"$MESSAGE"'"}'
}

# Function to send a message to Discord
send_to_discord() {
  local data
  data=$(generate_discord_data)
  
  curl -H "Content-Type: application/json" -X POST -d "$data" "$DISCORD_WEBHOOK_URL"
}

# Function to send a message to Telegram
send_to_telegram() {
  curl -s -X POST "https://api.telegram.org/bot$TELEGRAM_API_TOKEN/sendMessage" \
    -d "chat_id=$TELEGRAM_CHAT_ID" -d "text=$MESSAGE"
}

# Send the message to both Discord and Telegram
send_to_discord
send_to_telegram

