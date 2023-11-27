from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, filters, MessageHandler


key_token = "6321661423:AAGtqJfNn2vjcib_vOfAT4MLBJR2VGvEl14" #Masukkan KEY-TOKEN BOT 
user_bot = "cikibolBot" #Masukkan @user bot

names = {} #Menyimpan name yang menggunakan bot

async def start_command(update: Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo, saya bot yang akan membalas pesan kamu. Silahkan gunakan /name <name> untuk mengatur nama kamu.")
    await update.message.reply_text("Gunakan /help untuk menampilkan apa yang dapat saya berikan.")
    
async def help_command(update: Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Kirim pesan, bot akan membalas pesan..\nList commands : \n/start \n/help \n/name <name>")
    
async def set_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    try:
        name = context.args[0]
        names[chat_id] = name
        await update.message.reply_text(f"Halo {name}")
    except (IndexError, ValueError):
        await update.message.reply_text("Penggunaan: /name <name>")

def get_name(chat_id):
    return names.get(chat_id, "User")
   
async def text_massage(update: Update, context:ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    name = get_name(chat_id)
    text_diterima : str = update.message.text
    print(f"Pesan diterima dari {chat_id} {name}: {text_diterima}")
    text_lwr_diterima = text_diterima.lower()
    if 'halo' in text_lwr_diterima or 'hi' in text_lwr_diterima or 'hola' in text_lwr_diterima:
        await update.message.reply_text(f"Hai {name}, perkenalkan saya {user_bot}. Bagaimana kabar kamu?")
    elif 'selamat pagi' in text_lwr_diterima:
        await update.message.reply_text(f"Selamat pagi {name}, semangat hari ini yaa 😊")
    elif 'selamat siang' in text_lwr_diterima:
        await update.message.reply_text(f"Selamat siang {name}, jangan lupa makan siang 😊")
    elif 'selamat malam' in text_lwr_diterima:
        await update.message.reply_text(f"Selamat malam {name}, jangan lupa istirahat 😊")
    elif 'siapa kamu?' in text_lwr_diterima:
        await update.message.reply_text(f"Bot adalah: {user_bot}")
    elif 'apa kabar' in text_lwr_diterima:
        await update.message.reply_text("Kabar baik, kamu bagaimana?")
    elif 'baik' in text_lwr_diterima:
        await update.message.reply_text("Bagus, tetap semangat ya 😊")
    elif 'terima kasih' in text_lwr_diterima:
        await update.message.reply_text("Sama-sama")
    elif 'bye' in text_lwr_diterima:
        await update.message.reply_text("Sampai jumpa lagi :(")
    else:
        await update.message.reply_text("Maaf, saya tidak mengerti pesan kamu")

async def photo_message(update: Update, context:ContextTypes.DEFAULT_TYPE):
    return await update.message.reply_text("Gambar kamu bagus")
        
async def  error(update: Update, context:ContextTypes.DEFAULT_TYPE):
    print(f"error... : {context.error}")


if __name__ == '__main__':
    print("Mulai")
    app = Application.builder().token(key_token).build()
    #COMMAND :
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('name', set_name))
    #MESSAGE:
    app.add_handler(MessageHandler(filters.TEXT, text_massage))
    app.add_handler(MessageHandler(filters.PHOTO, photo_message))
    #error :
    app.add_error_handler(error)
    #polling :
    app.run_polling(poll_interval=1)
