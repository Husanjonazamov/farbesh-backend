from telebot.types import (
    KeyboardButton, ReplyKeyboardMarkup, WebAppInfo,
    InlineKeyboardMarkup, InlineKeyboardButton
)



def WebappButton():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    button = KeyboardButton(text="Taxi chaqirish", web_app=WebAppInfo(url="https://farbesh-tau.vercel.app/"))
    markup.add(button)

    return markup


# def accept_button(maps_link):
#     inline = InlineKeyboardMarkup(row_width=1)
    
#     button = InlineKeyboardButton(text="✔️ Qabul Qilingan", callback_data="accepted")
#     inline.add(button)
    
#     button_maps = InlineKeyboardButton(text="📍 Manzilni ko'rish", url=maps_link)
#     inline.add(button_maps)
    
#     return inline






