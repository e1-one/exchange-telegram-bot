#!/bin/bash

# How to start the process with the bot
# 1) chmod 755 runbot-proc.sh
# 2) crontab -e
# 3) add: 30 * * * * $PATH_TO_THIS_FOLDER/runbot-proc.sh
# How to check CRON log:
# grep CRON /var/log/syslog

# script expects BOT_TOKEN as env variable.

THIS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"

ps -aux | grep -v grep | grep start_bot_service.py
if [ $? -eq 0 ]; then
  echo "Process is already running."
else
  echo "Process is not running. Let's start it!"
  nohup python "$THIS_DIR/src/start_bot_service.py" "$BOT_TOKEN" > bot-nohup.out &
fi
