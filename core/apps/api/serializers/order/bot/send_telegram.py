from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from config.env import env
from .texts import caption_text


BOT_TOKEN = env.str("BOT_TOKEN")
GROUP_ID = env.int("GROUP_ID")

bot = TeleBot(token=BOT_TOKEN, parse_mode='HTML')



def location_button(maps_link):
    inline = InlineKeyboardMarkup(row_width=1)
    
    button = InlineKeyboardButton(text="✅ Qabul qilish", callback_data="accept")
    inline.add(button)
    
    button_maps = InlineKeyboardButton(text="📍 Manzilni ko'rish", url=maps_link)
    inline.add(button_maps)
    
    return inline



def send_order(maps_link, order):
    
    caption = caption_text(
        name=order.name,
        phone=order.phone,
        gender=order.gender,
        count=order.count
    )
    
    bot.send_message(
        chat_id=GROUP_ID,
        text=caption,
        reply_markup=location_button(maps_link)
    )
    
    
    


