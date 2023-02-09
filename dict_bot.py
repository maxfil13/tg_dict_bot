# В google colab добавить: !pip install pyTelegramBotAPI
# Чтобы добавить новое слово — нужно его прописать в объект DEFINITOINS на 13 строчке
# Важно все новые аббривиатуры в коде писать только с маленьких букв
# Пользователь в телеграм может писать и с большой и с маленькой — код всегда приводит к строчным

from telebot import TeleBot, types

bot = TeleBot(token='token', parse_mode='html') # создание бота

# словарь с определениями и аббревиатурами, которые знает бот
# в формате:
# 'ключевая фраза': 'соответствующее ей определение'
DEFINITOINS = {
    'регресс': 'Проверить что новый функционал не сломал существующий',
    'авторизация': '(от англ. «authorization») — процесс проверки (подтверждения) прав при попытке выполнения неких действий',
    'аджайл': '(от англ. «Agile») — гибкая методология разработки, объединяющая в себе целый ряд подходов и практик, основанных на 12 принципах Манифеста гибкой разработки программного обеспечения, а также практические подходы к разработке',
    'айди': '(или «айдишник», от англ. «id», «identificator») — уникальный признак объекта, который позволяет отличить его от других объектов, то есть идентифицировать',
    'айпи': '(или «айпишник», «айпи-адрес», от англ. «IP», «Internet Protocol Address») — уникальный адрес компьютера в Сети, который присваивается провайдером индивидуально каждому устройству и даёт возможность выхода в Интернет',
    'айти': '(или «ИТ», «информационные технологии», от англ. «IT», «Information Technologies») — довольно обширный класс дисциплин и областей деятельности, которые относятся к современным технологиям. Другими словами, это отрасль, отвечающая за обработку, сбор, хранение и передачу информации с помощью технических устройств и вычислительной техники',
    'апи': '(от англ. «API», «Application Programming Interface») — программный интерфейс приложения или интерфейс прикладного программирования. Простыми словами, это описание вариантов взаимодействия компьютерных программ между собой',
    'аутентификация': '(установление подленности) предотвращает доступ к сети нежелательных лиц и разрешает вход для легальных пользователей.',
    'баг': 'некая ошибка/дефект в написанном коде/программе, из-за которой программа ведет себя неожиданно, и, как следствие, выдает неправильные результаты',
    'баг-репорт': 'это отчёт, который информирует об ошибке в работе приложения. Сам документ доложен быть хорошо структурирован и содержать необходимую информацию.',
    'байт': 'базовая единица хранения и обработки информации, которая состоит из 8 битов',
    'батник': 'пакетный файл, т.е. текстовый файл (MS-DOS, OS/2 или Windows), который содержит последовательность команд, служащих для исполнения командным интерпретатором. После запуска данного файла программа-интерпретатор (например, cmd.exe) читает его построчно и по порядку исполняет команды',
    'бета-тест': 'последнее испытание разрабатываемого продукта (ПО/приложения/сайта) перед его официальным выпуском',
    'бэклог': 'От англ. backlog (дословно — очередь работ) — еще не запланированный объем работы, который требуется выполнить команде. Каждая созданная задача вначале попадает в бэклог, а потом уже в спринт.',
    'бэклог': 'От англ. backlog (дословно — очередь работ) — еще не запланированный объем работы, который требуется выполнить команде. Каждая созданная задача вначале попадает в бэклог, а потом уже в спринт.',
     'верификация': '(verification) — это процесс оценки системы, чтобы понять, удовлетворяют ли результаты текущего этапа разработки условиям, которые были сформулированы в его начале.',
   'идентификация': 'это определение пользователя в автоматизированной системе (например, в интернет-банке) по уникальному признаку — идентификатору. Для этого пользователь должен сообщить свой признак системе.',
    

}

# обработчик команды '/start'
@bot.message_handler(commands=['start'])
def start_command_handler(message: types.Message):
    # отправляем ответ на команду '/start'
    bot.send_message(
        chat_id=message.chat.id, # id чата, в который необходимо направить сообщение
        text='Привет! Я помогу тебе расшифровать сложные аббревиатуры и термины 🤓\nВведи интересующий термин, например, регресс', # текст сообщения
    )

# обработчик всех остальных сообщений
@bot.message_handler()
def message_handler(message: types.Message):
    # пробуем найти ключевую фразу в словаре
    definition = DEFINITOINS.get(
        message.text.lower(), # приводим текст сообщения к нижнему регистру
    )
    # если фразы нет в словаре, то переменная definition будет иметь значение None
    # проверяем это условие
    if definition is None:
        # если ключевая фраза не была найдена в словаре
        # отправляем ответ
        bot.send_message(
            chat_id=message.chat.id,
            text='😋 Я пока не знаю такого определения,'+'\nпопробуй ввести другое слово',
        )
        # выходим из функции
        return
    
    # если ключевая фраза была найдена, формируем текст сообщения и отправляем его
    # если перед строкой поставить букву f, то в фигурных скобках {} можно использовать переменные :)
    bot.send_message(
        chat_id=message.chat.id,
        text=f'-:\n<code>{definition}</code>',
    )

    bot.send_message(
        chat_id=message.chat.id,
        text=f'Жду следующий термин',
    )


# главная функция программы
def main():
    # запускаем нашего бота
    bot.infinity_polling()


if __name__ == '__main__':
    main()
