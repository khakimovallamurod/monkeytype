import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, Dispatcher
import handlers
from flask import Flask, request

app = Flask(__name__)
TOKEN = os.environ['TOKEN']


bot_app = ApplicationBuilder().token(TOKEN).build()

bot_app.add_handler(CommandHandler("start", handlers.start))
bot_app.add_handler(CommandHandler("sendResults", handlers.results_type))

bot_app.add_handler(CallbackQueryHandler(handlers.send_results_to_image, pattern='seconds:'))

@app.route(f"/", methods=['POST'])
def webhook():
    """Handle incoming webhook updates from Telegram"""
    update = Update.de_json(request.get_json(force=True), bot_app.bot)
    dispatcher = Dispatcher(bot_app.bot, None, workers=0)
    dispatcher.process_update(update)
    return "OK"

if __name__ == "__main__":
    app.run(debug=True)