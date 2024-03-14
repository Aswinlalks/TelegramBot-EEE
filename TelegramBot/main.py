import constants as keys
from telegram.ext import *
import responses as R
from reminders import add_reminder, get_reminders

print("bot started")

def start_command(update, context):
    update.message.reply_text("try:\nwhois\ntime\ntimetable\nsura\n/reminders\n/addreminder")

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

    
def error(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater = Updater(keys.API_KEY,use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("addreminder", add_reminder_command))
    dp.add_handler(CommandHandler("reminders", reminders_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))
    

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()
