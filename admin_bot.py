import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Send a message to the group
    await context.bot.send_message(chat_id=GROUP_CHAT_ID, text="Hello, everyone!")

async def send_results(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Send a message to the group
    await context.bot.send_message(chat_id=GROUP_CHAT_ID, text="Hello, everyone!")
# GROUP chat ID
GROUP_CHAT_ID =-1002190225722
TOKEN = os.environ['TOKEN']

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("sendResults", send_results))
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("hello", hello))

app.run_polling()