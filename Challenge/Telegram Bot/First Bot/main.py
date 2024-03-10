from telegram import Update, Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, InlineQueryHandler
from datetime import datetime
import requests

TOKEN = '6332606855:AAGT8fy3H6npQ9x7aKYqEppIM3EhjirwZjE'
BOT_USERNAME = '@nsilabot'
target_group_id = '-1001892665321'

bot = Bot(token=TOKEN)

NAME = 1

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello User!')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Help Service!')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    now = datetime.now()
    date_time = now.strftime('%d/%m/%Y, %H:%M:%S')
    await update.message.reply_text(str(date_time))

async def send_text_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = "Hello, this is a message sent from my bot!"
    params = {
        'chat_id': target_group_id,
        'text': message
    }
    API_URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    response = requests.get(API_URL, params=params)
    print(f'Status code: {response.status_code}')
    print('Response content:', response.text)
    await update.message.reply_text('Successfully sent!')

async def send_photo_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    API_URL = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'
    image_path = 'C:\\Users\\aa\\Downloads\\tanjiro.png'
    params = {'chat_id': target_group_id}
    files = {'photo': open(image_path, 'rb')}
    response = requests.post(API_URL, params=params, files=files)
    await update.message.reply_text('Successfully sent!')

def get_name(update, context):
    options = []
    options.append(InlineKeyboardButton('Enter Name', callback_data='name'))
    options.append(InlineKeyboardButton('Enter Age', callback_data='age'))
    reply_markup = InlineKeyboardMarkup([options])
    context.bot.send_message(chat_id=update.message.chat_id, text='Choose an option', reply_markup=reply_markup)

def handle_response(text: str) -> str:
    processed = text.lower()
    if processed in ('hello', 'hi'):
        return 'Hello user'
    return "I don't understand you?"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type = update.message.chat.type
    text = update.message.text
    print(f'User ({update.message.chat.id} in {message_type}: "{text}")')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text = text.replace(BOT_USERNAME, '').strip()
            response = handle_response(new_text)
        else:
            return
    else:
        response = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

async def handle_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # This function will be called when an image message is received
    message = update.message
    if message.photo:
        # Get the largest available photo
        photo = message.photo[-1]

        # Get the file ID of the photo
        photo_file_id = photo.file_id

        # Send the photo back to the user
        await context.bot.send_photo(chat_id=message.chat_id, photo=photo_file_id)
        await update.message.reply_text('Nice')
    else:
        await update.message.reply_text("No image found in the message.")

if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('time', time_command))
    app.add_handler(CommandHandler('sendText', send_text_command))
    app.add_handler(CommandHandler('sendPhoto', send_photo_command))

    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    app.add_handler(MessageHandler(filters.PHOTO, handle_image))

    app.add_error_handler(error)

    print('Polling...')
    app.run_polling(poll_interval=3)
