import os
from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from flask import Flask, request
import handlers

app = Flask(__name__)
TOKEN = os.environ['TOKEN']

# Initialize the bot with Updater
updater = Updater(TOKEN)
dispatcher = updater.dispatcher

# Register handlers
dispatcher.add_handler(CommandHandler("start", handlers.start))
dispatcher.add_handler(CommandHandler("sendResults", handlers.results_type))
dispatcher.add_handler(CallbackQueryHandler(handlers.send_results_to_image, pattern='seconds:'))

@app.route(f"/", methods=['POST'])
def webhook():
    """Handle incoming webhook updates from Telegram"""
    update = Update.de_json(request.get_json(force=True), updater.bot)
    dispatcher.process_update(update)
    return "OK"

if __name__ == "__main__":
    app.run(port=8080, debug=True)
