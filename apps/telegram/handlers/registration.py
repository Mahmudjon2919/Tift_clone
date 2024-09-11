import re
from apps.common.models import Region, District
from apps.education.models import Faculty
from apps.telegram.keyboards import replies
from apps.telegram import states
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from datetime import datetime
def get_phone(update, context):
    print("UPDATE IN PHONE STATE")
    if update.message and update.message.contact:
        contact_user_id=update.message.contact.user_id
        user_id=update.message.from_user_id
        if contact_user_id !=user_id:
            update.message.reply_text("Bu raqam sizga tegishli emas!", reply_markup=replies.get_contact())
            return states.PHONE
        phone=update.message.contact.phone_number
        context.user_data["phone"]=phone
        update.message.reply_text("You are in the right way", reply_markup=replies.get_contact())
        return states.PHONE
    update.message.reply_text("Iltimos telefon raqamingizni tugma orqali yuboring", reply_markup=replies.get_contact())
    return states.PHONE


def get_full_name(update, context):
    if update.message and update.message.text:
        full_name = update.message.text
        context.user_data['full_name'] = full_name
        update.message.reply_text("Everything is ok, please send your passport in AA1234567 format", reply_markup=ReplyKeyboardMarkup)
        return states.PASSPORT

    update.message.reply_text("Please send your name as text", reply_markup=ReplyKeyboardRemove())
    return states.FULL_NAME




def get_passport(update, context):
    if update.message and update.message.text:
        if not re.match("^(A-Z){2}\d{7}$", update.message.text):
            update.message.reply_text("Please send your passport data in AA1234567 format", reply_markup=ReplyKeyboardRemove())
            return states.PASSPORT

        context.user_data['passport']=update.message.text
        update.message.reply_text("Correct please send your PINFL")
        return states.PINFIL

    update.message.reply_text("Please send your passport data as text")
    return states.PASSPORT





def get_pinfil(update, context):
    if update.message and update.message.text:
        text=update.message.text
        if str(text).isdigit() and len(text)==14:
            context.user_data['pinfl'] = text
            update.message.reply_text("Please choise your gender", reply_markup=replies.get_gender())
            return states.GENDER


        update.message.reply_text("Please send your correct  PINFL")
        return states.PINFIL

def get_gender(update, context):
    if update.message and  update.message.text:
        text=update.message.text
        genders={
            "Erkak":"male",
            "Ayol":"female"
        }
        if text  in genders.keys():
            context.user_data['gender'] = genders[text]
            update.message.reply_text("Tug'ilgan sanangizni 01.01.2000 formatida yuboring", reply_markup=ReplyKeyboardRemove)
            return states.BIRTH_DATA

    update.message.reply_text("Please, chose your gender through the buttons below", reply_markup=replies.get_gender())
    return states.GENDER


def get_birth_date(update, context):
    if update.message and update.message.text:
        text=update.message.text
        if re.match("^(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.(199[6-9]|20[0-9]{2})$", text):
            try:
                birth_date=datetime.strptime(text, "%d.%m.%Y")
                context.user_data['birth_date']=birth_date
                update.message.reply_text("Please, choose your faculty", reply_markup=replies.get_items(Faculty.objects.all()))
                return states.FACULTY
            except ValueError:
                pass

    update.message.reply_text("Please send your birth date in 01.01.2000 format. Years should be greater than 1995")
    return states.BIRTH_DATA
def get_faculty(update, contetx):
    if update.message and update.message.text:
        text=update.message.text
        try:
            faculty=Faculty.objects.get(title=text)
            contetx.user_data['faculty']=faculty.id
            update.message.reply_text("Please choose your direction", reply_markup=replies.get_items(faculty.directions, "title"))
            return states.DIRECTION
        except Faculty.DoesNotExist:
            pass
        update.message.reply_text("please choose faculty from the button bellow", reply_markup=replies.get_items(Faculty.objects.all(), "title"))
        return states.FACULTY
def get_direction(update, context):
    if update.message and update.message.text:
        text = update.message.text
        faculty_id = context.user_data.get('faculty')

        if not faculty_id:
            update.message.reply_text("Please select a faculty first.")
            return states.FACULTY

        try:
            faculty = Faculty.objects.get(id=faculty_id)
            direction = faculty.directions.get(title=text)
            context.user_data['direction'] = direction.id
            update.message.reply_text("Please choose your region", reply_markup=replies.get_items(direction.regions, "title"))
            return states.REGION
        except faculty.directions.model.DoesNotExist:
            update.message.reply_text("Please choose a direction from the buttons below", reply_markup=replies.get_items(faculty.directions.all(), "title"))
            return states.DIRECTION

    update.message.reply_text("Please choose your direction using the buttons below.")
    return states.DIRECTION


def get_region(update, context):
    if update.message and update.message.text:
        text = update.message.text
        try:
            region = Region.objects.get(title=text)
            context.user_data['region'] = region.id
            update.message.reply_text("Please choose your district", reply_markup=replies.get_items(region.districts.all(), "title"))
            return states.DISTRICT
        except Region.DoesNotExist:
            pass
        update.message.reply_text("Please choose a region from the buttons below", reply_markup=replies.get_items(Region.objects.all(), "title"))
        return states.REGION

    update.message.reply_text("Please choose your region using the buttons below.")
    return states.REGION



def get_district(update, context):
    if update.message and update.message.text:
        text = update.message.text
        region_id = context.user_data.get('region')

        if not region_id:
            update.message.reply_text("Please select a region first.")
            return states.REGION

        try:
            district = District.objects.get(title=text, region_id=region_id)
            context.user_data['district'] = district.id
            update.message.reply_text("Registration process complete!", reply_markup=ReplyKeyboardRemove())

            return states.COMPLETE
        except District.DoesNotExist:
            pass

        region = Region.objects.get(id=region_id)
        update.message.reply_text("Please choose a district from the buttons below", reply_markup=replies.get_items(region.districts.all(), "title"))
        return states.DISTRICT

    update.message.reply_text("Please choose your district using the buttons below.")
    return states.DISTRICT


