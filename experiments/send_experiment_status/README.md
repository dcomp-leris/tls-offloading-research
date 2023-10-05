# Experiment Status Notifier

This script allows you to send experiment status updates to both Discord and Telegram using API webhooks. It's useful for monitoring and receiving notifications about your ongoing experiments.

## Prerequisites

Before using this script, make sure you have the following:

- API tokens and chat IDs for both Discord and Telegram.
- `curl` installed on your system for making HTTP requests.

## Usage

1. Clone or download this repository to your local machine.

2. Modify the script to include your API tokens and chat IDs:
   - `TELEGRAM_API_TOKEN` for your Telegram bot.
   - `TELEGRAM_CHAT_ID` for your Telegram chat or user ID.
   - `DISCORD_WEBHOOK_URL` for your Discord webhook URL.

3. Run the script with a status message as an argument to send updates to both Discord and Telegram. For example:

   ```bash
   ./send_experiment_status.sh "Experiment XYZ completed successfully!"
   ```

   Replace `"Experiment XYZ completed successfully!"` with your desired status message.

## License

This software is released under the [BSD-3 License](https://opensource.org/license/bsd-3-clause/). You are free to use, modify, and distribute this software, provided that you include the original copyright notice and disclaimers. The BSD-3 License is a permissive open-source license that encourages collaboration and innovation. It grants you the freedom to adapt this software to your needs while respecting the original author's contributions. Feel free to contribute to the project or build upon it for your own projects. Please review the LICENSE file on the root of this repo for the full terms and conditions of this license.
