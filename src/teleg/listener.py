from telegram import ParseMode


class UpdateListener:
    def __init__(self, context, chat_id):
        self.context = context
        self.chat_id = chat_id

    def send_message(self, message):
        self.context.bot.send_message(chat_id=self.chat_id, parse_mode=ParseMode.MARKDOWN, text=message)
