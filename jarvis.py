import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(level=logging.INFO)

TOKEN = '6905688737:AAExzZjbuguMrKCAADyzyW1IYoTZJLV3A2Y'

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Hello I\'m Jarvis Bot')

def ask_jarvis(update, context):
    question = update.message.text
    answer = ask_me(question)  # функция, которая будет отправлять вопрос мне и получать ответ
    context.bot.send_message(chat_id=update.effective_chat.id, text=answer)

def ask_me(question):
    # здесь будет код, который будет отправлять вопрос мне и получать ответ
    # для примера, я просто верну ответ
    return 'Answer from Jarvis: ' + question

def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text, ask_jarvis))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
