import telebot, wikipedia, re
from telebot import types

# Создаем экземпляр бота
bot = telebot.TeleBot('5699526376:AAHOeh3zmWrvdEWWsxvfMAx0N0Q4gL5R7WE')
# Устанавливаем русский язык в Wikipedia
wikipedia.set_lang("ru",)
# Чистим текст статьи в Wikipedia и ограничиваем его тысячей символов
def getwiki(s):
    try:
        ny = wikipedia.page(s)
        # Получаем первую тысячу символов
        wikitext=ny.content[:1000]
        # Разделяем по точкам
        wikimas=wikitext.split('.')
        # Отбрасываем всЕ после последней точки
        wikimas = wikimas[:-1]
        # Создаем пустую переменную для текста
        wikitext2 = ''
        # Проходимся по строкам, где нет знаков «равно» (то есть все, кроме заголовков)
        for x in wikimas:
            if not('==' in x):
                    # Если в строке осталось больше трех символов, добавляем ее к нашей переменной и возвращаем утерянные при разделении строк точки на место
                if(len((x.strip()))>3):
                   wikitext2=wikitext2+x+'.'
            else:
                break
        # Теперь при помощи регулярных выражений убираем разметку
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)
        # Возвращаем текстовую строку
        return wikitext2
    # Обрабатываем исключение, которое мог вернуть модуль wikipedia при запросе
    except Exception as e:
        return 'В энциклопедии нет информации об этом'
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Отправьте мне любое слово, и я найду его значение на Wikipedia')
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, getwiki(message.text))
# Запускаем бота


keyboard = types.InlineKeyboardMarkup()
service = types.InlineKeyboardMarkup()
back = types.InlineKeyboardMarkup()

button1 = types.InlineKeyboardButton("Список услуг: ", callback_data="Услуги")
button2 = types.InlineKeyboardButton("Перейти на сайт", callback_data="Сайт")
button3 = types.InlineKeyboardButton("Контакты для связи", callback_data="Связь")

back1 = types.InlineKeyboardButton("Назад", callback_data="Назад")

service1 = types.InlineKeyboardButton("Ремонт и установка техники", callback_data="Авто")
service2 = types.InlineKeyboardButton("Ремонт авто", callback_data="Собака")
service3 = types.InlineKeyboardButton("Репетиторы и обучение", callback_data="Ремонт")
service4 = types.InlineKeyboardButton("Красота", callback_data="Телевизор")
service5 = types.InlineKeyboardButton("Перевозки и курьеры", callback_data="Мебель")
service6 = types.InlineKeyboardButton("Хозяйство и уборка", callback_data="Жена")
service7 = types.InlineKeyboardButton("Компьютеры и IT", callback_data="Айти")
service8 = types.InlineKeyboardButton("Дизайнеры", callback_data="Дизайнеры")
service9 = types.InlineKeyboardButton("Аренда", callback_data="Аренда")
service10 = types.InlineKeyboardButton("Юристы", callback_data="Юристы")
service11 = types.InlineKeyboardButton("Тренеры", callback_data="Тренеры")
service12 = types.InlineKeyboardButton("Фото, видео, аудио", callback_data="Медиа")
service13 = types.InlineKeyboardButton("Творчество, рукоделие и хобби", callback_data="Творчество")
service14 = types.InlineKeyboardButton("Организация мероприятий", callback_data="Мероприятия")
service15 = types.InlineKeyboardButton("Артисты", callback_data="Артисты")
service16 = types.InlineKeyboardButton("Охрана и детективы", callback_data="Охрана")
service17 = types.InlineKeyboardButton("Услуги для животных", callback_data="Животные")
service18 = types.InlineKeyboardButton("Разное", callback_data="Разное")


keyboard.add(button1, button2, button3)
service.add(service1, service2, service3, service4, service5, service6, service7, service8, service9,
            service10, service11, service12, service13, service14, service15, service16, service17, service18)
back.add(back1)


@bot.message_handler(commands=['start', 'hi'])
def start_message(message):
    bot.send_message(message.chat.id, "Здравствуйте.")
    bot.send_message(message.chat.id, "Выберите действие", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "Услуги":
        bot.send_message(call.from_user.id, "Список услуг", reply_markup=service)
    elif call.data == "Сайт":
        bot.send_message(call.from_user.id, "http://127.0.0.1:8000/api/v1/docs/", reply_markup=back)
    elif call.data == "Связь":
        bot.send_contact(call.from_user.id, "+996778827540", "Kutmanbek", "Mederbekov", reply_markup=back)
    elif call.data == "Назад":
        bot.send_message(call.from_user.id, "Выберите действие", reply_markup=keyboard)


@bot.message_handler(content_types=['sticker'])
def send_sticker(message):
    bot.send_sticker(message.chat.id, message.sticker.file_id)

bot.polling(none_stop=True, interval=0)