from config import *

@bot.message_handler(
    func=lambda message: message.text.split()[0] in ["English", "Italian"]
    # message.content_type == 'text' and 
    )
def set_langauge(message):
    """sets language and returns language value and send user confirmation message"""
    chat_id = message.chat.id
    user_object = get_user(message)
    lang = user_object["lang"]
    message_lang = message.text.split()[0].upper()
    language = set_lang(user_object["user_id"], message_lang)
    set_lang_text = {
        "ENGLISH": """Language is set to: English 🇬🇧""",
        "ITALIAN": """La lingua è impostata su: Italian 🇮🇹"""
    }
    bot.send_message(
        chat_id,
        text=set_lang_text[language],
        reply_markup=dashboard.get(language)
    )