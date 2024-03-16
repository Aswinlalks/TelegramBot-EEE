import time
import constants as keys
from telegram.ext import *
import responses as R
from responses import *
#from reminders import add_reminder, get_reminders
from document_links import get_drive_link
import json
import assignment_fetcher


print("bot started")
# Store the time when the bot starts
start_time = time.time()

def start_command(update, context):
    update.message.reply_text("try:\nwhois\ntime\nsura\n/timetable\n/notes\n/assignments\n/uptime")

def help_command(update, context):
    update.message.reply_text('google something')

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)
    update.message.reply_text(response)



def handle_document_request(update, context):
    try:
        file_path = 'links.json'  # Replace with the actual path to your JSON file
        with open(file_path, 'r') as file:
            data = json.load(file)
            documents = data.get('documents', {})
            if documents:
                document_list = []
                for idx, (document_name, drive_link) in enumerate(documents.items(), 1):
                    document_text = f"{idx}. [{document_name}]({drive_link})"
                    document_list.append(document_text)

                document_text = "\n".join(document_list)
                reply_text = "Available documents:\n" + document_text
                update.message.reply_text(reply_text, parse_mode='Markdown')
            else:
                update.message.reply_text("No documents found.")
    except Exception as e:
        print("Error fetching documents:", e)
        update.message.reply_text("An error occurred while fetching the documents.")

def uptime_command(update, context):
    current_time = time.time()
    uptime_seconds = current_time - start_time
    uptime_hours = uptime_seconds // 3600
    uptime_minutes = (uptime_seconds % 3600) // 60
    uptime_seconds %= 60
    update.message.reply_text(f"Bot has been running for\n{int(uptime_hours)} hours, {int(uptime_minutes)} minutes, and {int(uptime_seconds)} seconds.")


def assignments_command(update, context):
    username = "22ee523"
    password = "passd@123"
    assignments = assignment_fetcher.fetch_assignments(username, password)
    if assignments:
        response = "\n\n".join([f"Subject: {assignment['subject']}\nLast Date: {assignment['last_date']}" for assignment in assignments])
        current_time = time.strftime("%d %b %Y %I:%M %p")
        response += f"\n\nFetched from ETLab website at \n{current_time}"
        update.message.reply_text(response)
    else:
        update.message.reply_text("Failed to fetch assignments. Please check your credentials.")


def error(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater = Updater(keys.API_KEY,use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("notes", handle_document_request))
    dp.add_handler(CommandHandler("uptime", uptime_command))
    dp.add_handler(CommandHandler("assignments", assignments_command))



    dp.add_handler(MessageHandler(Filters.text, handle_message))
    

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()
