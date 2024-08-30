from telegram import KeyboardButton, ReplyKeyboardMarkup

def get_contact():
    return ReplyKeyboardMarkup(
        [
            KeyboardButton("Telefon raqamni yuborish", request_contact=True)
        ], resize_keyboard=True
    )