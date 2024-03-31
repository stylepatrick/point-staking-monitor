# point-staking-monitor
The provided Project is designed to monitor Cosmos Point staking rewards.
It accomplishes this through web scraping of a designated staking node webpage using Selenium and BeautifulSoup libraries.
The script continuously checks for staking rewards information at a specified interval. When new rewards information is detected, it sends a notification message via Telegram to a specified chat.

## Set up environment variables:
- `ENVIRONMENT`: Set to "PROD" for production. Required for Docker as chromdriver is in different directory!
- `STAKING_NODE`: The staking node URL.
- `BOT_TOKEN`: Your Telegram bot token.
- `CHAT_ID`: Your Telegram chat ID.
