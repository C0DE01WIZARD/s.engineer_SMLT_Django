import telepot

token = '6600850602:AAGPhNvuwEbtw5UVsR0XozxwqRJCrxYJsnE'
my_id = -1001995449879
telegramBot = telepot.Bot(token)


def send_message(text):
    telegramBot.sendMessage(-1001995449879, text, parse_mode="Markdown")
