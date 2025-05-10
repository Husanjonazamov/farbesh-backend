

def caption_text(**kwargs):
    caption = ''
    
    if kwargs['count'] == "one":
        count = '1 kishi'
    elif kwargs['count'] == "two":
        count = "2 kishi"
    elif kwargs['count'] == "there":
        count = '3 kishi'
    else:
        count = '4 kishi'
    
    if kwargs['gender'] == 'other':
        choice_label = "📦 Boshqa"
        gender_text = "Pochta"
        
        caption = "🎯 <b>Yangi Buyurtma</b>\n\n"
        caption += f"📞 Telefon: <b>+{kwargs['phone']}</b>\n"
        caption += f"<b>{choice_label}: {gender_text}</b>\n"  
        
    elif kwargs['gender'] == "male":
        choice_label = "🧑‍💼 Yo'lovchi"
        gender_text = "Erkak"
         
        caption = "🎯 <b>Yangi Buyurtma</b>\n\n"
        caption += f"📞 Telefon: <b>+{kwargs['phone']}</b>\n"
        caption += f"<b>{choice_label}: {gender_text}</b>\n"  
        caption += f"🔢 <b>Soni: {count}</b>"
         
        
    else:
        choice_label = "👩🏻 Yo'lovchi"
        gender_text = "Ayol"

        caption = "🎯 <b>Yangi Buyurtma</b>\n\n"
        caption += f"📞 Telefon: <b>+{kwargs['phone']}</b>\n"
        caption += f"<b>{choice_label}: {gender_text}</b>\n"  
        caption += f"🔢 <b>Soni: {count}</b>"

    return caption  

