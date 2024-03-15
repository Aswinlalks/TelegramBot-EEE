import time
import constants as keys
from telegram.ext import *
import responses as R
from responses import *
from reminders import add_reminder, get_reminders
from document_links import get_drive_link
import json


print("bot started")
# Store the time when the bot starts
start_time = time.time()

def start_command(update, context):
    update.message.reply_text("try:\nwhois\ntime\nsura\n/timetable\n/reminders\n/addreminder\n/notes\n/uptime")

def help_command(update, context):
    update.message.reply_text('google something')

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)
    update.message.reply_text(response)

def reminders_command(update, context):
    update.message.reply_text('Type /addreminder to add an assignment reminder.')

def add_reminder_command(update, context):
    # Parse the command arguments (assignment and due date)
    args = context.args
    if len(args) < 2:
        update.message.reply_text('Please provide the assignment and due date in the format: /addreminder[space]<assignment>[space]<due date>')
        return

    assignment = args[0]
    due_date = ' '.join(args[1:])  # Join remaining arguments for due date

    # Add reminder
    add_reminder(update.message.from_user.id, assignment, due_date)
    update.message.reply_text('Reminder added successfully!')

def reminders_command(update, context):
    # Get reminders for the user
    reminders = get_reminders(update.message.from_user.id)
    if not reminders:
        update.message.reply_text('No reminders found.')
        return
    
    reminder_text = '\n'.join([f"- {assignment} due on {due_date}" for assignment, due_date in reminders])
    update.message.reply_text('Your reminders:\n' + reminder_text)

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


    
def error(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater = Updater(keys.API_KEY,use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("addreminder", add_reminder_command))
    dp.add_handler(CommandHandler("reminders", reminders_command))
    dp.add_handler(CommandHandler("notes", handle_document_request))
    dp.add_handler(CommandHandler("uptime", uptime_command))


    dp.add_handler(MessageHandler(Filters.text, handle_message))
    

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()
