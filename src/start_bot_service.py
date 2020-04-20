import sys
import logging

# configure logging before other modules are loaded
logging.getLogger().setLevel(logging.INFO)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

from teleg.telegram_events_handlers import configure_updater


def read_config_file():
    with open('./config.json', 'r') as f:
        import json
        return json.load(f)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        bot_token = sys.argv[1]
    else:
        bot_token = read_config_file()['token']
    configure_updater(bot_token)
    logging.info("bot is started.")
