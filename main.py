import random
import datetime as dt
from vk_api import VkApi
from vk_api.longpoll import VkLongPoll, VkEventType
from data.config import *
from data.keyboard import *
from data.parser import news_parser
from data.locations_worker import LocationsDb, select_best_location


def get_index(index):
    i = 0
    for j in INFO:
        if i == index:
            return j, INFO.get(j)
        i += 1


def write_start_message(user_id):
    vk.messages.send(user_id=user_id, message="🏚 Главное меню", random_id=0,
                     keyboard=main_inline_keyboard.get_keyboard())


def set_main_keyboard(user_id, message):
    vk.messages.send(user_id=user_id, message=message, random_id=0,
                     keyboard=main_keyboard.get_keyboard())


def share_location(user_id):
    vk.messages.send(user_id=user_id, message="📩 Отлично, осталось только поделится своим местоположением",
                     keyboard=send_location.get_keyboard(), random_id=0)


def none_write_message(user_id):
    vk.messages.send(user_id=user_id, message="‼ Ничего вводить не требуется", random_id=0)


def send_best_location(user_id, name, address):
    vk.messages.send(user_id=user_id, message=f"🏠 Адрес: {address}\n🔎 Название организации: {name}\n"
                                              f"И помни:\n{random.choice(QUOTES)}", random_id=0)


def write_pass_menu(user_id):
    vk.messages.send(user_id=user_id, message=f"⁉ Вот какой мусор мы вам можем помочь сдать",
                     random_id=0, keyboard=main_pass_keyboard.get_keyboard())


def write_news_menu(user_id, ind):
    global INDEX
    vk.messages.send(user_id=user_id, message=f"{get_index(INDEX)[0]}\n{get_index(INDEX)[-1]}", random_id=0,
                     keyboard=list_keyboard.get_keyboard())
    INDEX += ind


vk_session = VkApi(token=TOKEN)
vk = vk_session.get_api()
long_poll = VkLongPoll(vk_session)
locate_db = LocationsDb()
INFO = news_parser()
for event in long_poll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            text = event.text
            try:
                result = vk_session.method("messages.getById", {"message_ids": [event.message_id],
                                                                "group_id": 189072320})
                geolocation = result["items"][0]["geo"]["coordinates"]
                lat, lon = geolocation["latitude"], geolocation["longitude"]
                best_lat_lon, name, address = select_best_location(lat, lon, locate_db.select_category(CATEGORY))
                send_best_location(event.user_id, name, address)
                set_main_keyboard(event.user_id, "✅ Возвращена клавиатура")
            except KeyError:
                pass
            if text == "Начать":
                set_main_keyboard(event.user_id, "Привет! я подскажу тебе где ближе всего:")
                write_start_message(event.user_id)
            elif text == "✳ Сдать батарейки":
                share_location(event.user_id)
                CATEGORY = "batteries"
            elif text == "✳ Сдать Раздельный мусор":
                share_location(event.user_id)
                CATEGORY = "waist"
            elif text == "✳ Сдать стекло":
                share_location(event.user_id)
                CATEGORY = "glass"
            elif text == "✳ Сдать макулатуру":
                share_location(event.user_id)
                CATEGORY = "paper"
            elif text == "📜 Главное меню":
                write_start_message(event.user_id)
            elif text == "✳ Сдать мусор":
                write_pass_menu(event.user_id)
            elif text == "✳ Эко - новости":
                write_news_menu(event.user_id, 0)
            elif text == "Следующая новость ➡":
                write_news_menu(event.user_id, 1)
            elif text == "⬅ Предыдущая новость":
                try:
                    write_news_menu(event.user_id, -1)
                except Exception:
                    write_news_menu(event.user_id, 0)
            else:
                none_write_message(event.user_id)
            INFO = news_parser() if dt.datetime.now().time().minute == 0 else INFO
