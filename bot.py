import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from nerd import start_script

BOT_TOKEN = "8796761100:AAFRNRVbGpG1IZsS5tgpyLkkSt2mcP8Mcjk"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot is Online 🚀")


async def run(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Script Started ⚡")
    
    asyncio.create_task(asyncio.to_thread(start_script))


app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("run", run))

app.run_polling()