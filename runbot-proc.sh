#!/bin/bash

# crontab -e
# add: 30 * * * * $PATH_TO_THIS_FOLDER/runbot-proc.sh
# How to check CRON log:
# grep CRON /var/log/syslog

ps -aux | grep -v grep | grep start_bot_service.py
if [ $? -eq 0 ]; then
  echo "Process is already running."
else
  echo "Process is not running. Let's start it!"
  nohup python3.7 ./exchange-telegram-bot/src/start_bot_service.py 1026738267:AAHmqP-Qzo8H1bC6M93o6PSgqFg8qsCNQyo > bot-nohup.out &
fi
