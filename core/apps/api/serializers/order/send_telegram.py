from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from config.env import env

BOT_TOKEN = env.str("BOT_TOKEN")
GROUP_ID = env.int("GROUP_ID")

bot = TeleBot(token=BOT_TOKEN, parse_mode='HTML')



def location_button(maps_link):
    inline = InlineKeyboardMarkup(row_width=1)
    
    button = InlineKeyboardButton(text="Qabul qilish", callback_data="accept")
    inline.add(button)
    button_maps = InlineKeyboardButton(text="Manzilni ko'rish", url=maps_link)
    inline.add(button_maps)
    
    return inline


def caption_text(**kwargs):
    caption = ''
    
    if kwargs['gender'] == 'other':
        choice_label = "📦 Boshqa"
        gender_text = "Pochta"
    elif kwargs['gender'] == "male":
        choice_label = "🧑‍💼 Yo'lovchi"
        gender_text = "Erkak"
    else:
        choice_label = "👩🏻 Yo'lovchi"
        gender_text = "Ayol"
        
    if kwargs['count'] == "one":
        count = '1 kishi'
    elif kwargs['count'] == "two":
        count = "2 kishi"
    elif kwargs['count'] == "there":
        count = '3 kishi'
    else:
        count = '4 kishi'
    
    caption = "🎯 <b>Yangi Buyurtma</b>\n\n"
    caption += f"👤 <b>Ism: {kwargs['name']}</b>\n"
    caption += f"📞 <b>Telefon: {kwargs['phone']}</b>\n"
    caption += f"<b>{choice_label}: {gender_text}</b>\n"  
    caption += f"🔢 <b>Soni: {count}</b>"

    return caption  

  

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
    

