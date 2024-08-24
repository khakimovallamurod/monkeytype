import os
from telegram import Update
from telegram.ext import ContextTypes, CallbackContext
from main import get_user_info,get_users_wpm_accuracy, get_users_html_convert
import keyboards
GROUP_CHAT_ID =-1002190225722

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    first_name = update.message.chat.first_name
    chat_id = update.effective_chat.id
    await context.bot.send_message(chat_id=chat_id, text=f"Assalomu aleykum {first_name}. Siz bu bot orqali typingdan natijalarni olishingiz mumkin!!!")


async def results_type(update: Update, context: CallbackContext):
    await update.message.reply_text(text='Monketypedan natija turini tanlang?', reply_markup=keyboards.inline_keyboard)

async def send_results_to_image(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    time = update.callback_query.data.split(":")[1]
    users = get_user_info('monkeytype.csv')
    users_wpm_accuracy = get_users_wpm_accuracy(users,time)
    image_path = 'monkeytype_results.jpg'
    users_total_convert_image = get_users_html_convert(users_wpm_accuracy, image_path, time)
    await context.bot.send_photo(chat_id=GROUP_CHAT_ID, photo=image_path, message_thread_id=2)


async def send_results(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    users = get_user_info('monkeytype.csv')

    users_wpm_accuracy = get_users_wpm_accuracy(users,15)
    results=''
    for idx,user in enumerate(users_wpm_accuracy):
        if idx==0:
            results+=f'🥇 {user["full_name"]}\t WPM: {user["wpm"]} Accuracy: {user["accuracy"]}\n'
        elif idx==1:
            results+=f'🥈 {user["full_name"]}\t WPM: {user["wpm"]} Accuracy: {user["accuracy"]}\n'
        elif idx==2:
            results+=f'🥉 {user["full_name"]}\t WPM: {user["wpm"]} Accuracy: {user["accuracy"]}\n'
        else:
            results+=f'{idx+1}. {user["full_name"]}\t WPM: {user["wpm"]} Accuracy: {user["accuracy"]}\n'
        
    # Send a message to the group
    await context.bot.send_message(chat_id=GROUP_CHAT_ID, text=results)

