import logging
import asyncio
import aiohttp
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
from config import BOT_TOKEN, OWM_API_KEY

# Настройка логгирования для отслеживания работы бота
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
# Бот обрабатывает взаимодействие с Telegram API
# Диспетчер управляет обработчиками сообщений и команд
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Обработчик команды /start
# Выполняется, когда пользователь отправляет команду /start
@dp.message(Command("start"))
async def cmd_start(message: Message):
    # Отправляем приветственное сообщение
    await message.answer(
        "Привет! Я бот погоды. Напиши 'погода Город', чтобы узнать текущую погоду.\n"
        "Например: погода Киев\n\n"
        "Введи /help для получения справки."
    )

# Обработчик команды /help
# Выполняется, когда пользователь отправляет команду /help
@dp.message(Command("help"))
async def cmd_help(message: Message):
    # Создаем текст справки с использованием HTML-форматирования
    help_text = (
        "🌤 <b>Как пользоваться ботом погоды:</b>\n\n"
        "Просто напиши <i>погода</i> и название города.\n"
        "Например: <code>погода Мюнхен</code> или <code>погода Лондон</code>\n\n"
        "Я покажу текущую температуру, влажность и описание погоды.\n\n"
        "Доступные команды:\n"
        "/start - Запуск бота\n"
        "/help - Показать эту справку"
    )
    # Отправляем справку с поддержкой HTML-форматирования
    await message.answer(help_text, parse_mode="HTML")

# Функция для получения данных о погоде через API OpenWeatherMap
async def get_weather(city_name):
    # Формируем URL для запроса к API OpenWeatherMap
    # units=metric - получаем температуру в градусах Цельсия
    # lang=ru - получаем описание погоды на русском языке
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={OWM_API_KEY}&units=metric&lang=ru"
    
    # Создаем HTTP-сессию для запроса
    async with aiohttp.ClientSession() as session:
        # Отправляем GET-запрос к API
        async with session.get(url) as response:
            # Проверяем статус ответа
            if response.status == 200:
                # Если статус 200 (OK), парсим JSON-ответ
                data = await response.json()
                return {
                    'status': 'success',
                    'data': data
                }
            else:
                # Если статус не 200, возвращаем ошибку
                return {
                    'status': 'error',
                    'error': f"Ошибка {response.status}"
                }

# Обработчик сообщений с запросом погоды
# Выполняется, когда пользователь отправляет сообщение, начинающееся с "погода "
@dp.message(F.text.lower().startswith("погода "))
async def show_weather(message: Message):
    # Извлекаем название города из сообщения
    # Удаляем "погода " из начала сообщения и обрезаем пробелы
    city_name = message.text.lower().replace("погода ", "", 1).strip()
    
    # Получаем данные о погоде через API
    weather_result = await get_weather(city_name)
    
    # Проверяем, успешно ли получены данные
    if weather_result['status'] == 'success':
        # Получаем данные из ответа API
        data = weather_result['data']
        
        # Извлекаем нужные данные из ответа API
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']
        city = data['name']
        
        # Составляем сообщение с информацией о погоде
        # Используем HTML-форматирование для красивого вывода
        weather_message = (
            f"🌡 <b>Погода в городе {city}:</b>\n\n"
            f"🌡 Температура: {temperature}°C\n"
            f"💧 Влажность: {humidity}%\n"
            f"☁️ Описание: {description}"
        )
        
        # Отправляем сообщение с погодой пользователю
        await message.answer(weather_message, parse_mode="HTML")
    else:
        # Если произошла ошибка, отправляем сообщение об ошибке
        await message.answer(
            "😕 Извините, не могу найти информацию о погоде для указанного города. "
            "Пожалуйста, проверьте название города и попробуйте снова.\n\n"
            "Пример: погода Киев"
        )

# Точка входа в программу
async def main():
    # Запуск бота в режиме long-polling
    # Бот будет постоянно проверять наличие новых сообщений
    await dp.start_polling(bot)

# Проверяем, что скрипт запущен напрямую, а не импортирован
if __name__ == "__main__":
    # Запускаем асинхронную функцию main()
    asyncio.run(main())