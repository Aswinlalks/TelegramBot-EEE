from datetime import datetime


def get_timetable_for_day():
    # Get the current day of the week (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
    current_day = datetime.now().weekday()

    # Define the timetable for each day of the week
    timetable = {
        0: "Monday timetable:\nDigital Electronics - 9:00 AM\nDCMT - 10:00 AM\nPE - 11:05 AM\nDCMT - 1:00 PM\nMATHS - 02:00 PM\nDigital Electronics - 03:05 PM",
        1: "Tuesday timetable:\nEMT - 9:00 AM\nDE - 10:00 AM\nEMT - 11:05 AM\nLAB - 1:00-4:00 PM",
        2: "Wednesday timetable:\nEMT - 9:00 AM\nMATHS - 10:00 AM\nDCMT - 11:05 AM\nCOI - 1:00 PM\nMentoring Hour - 02:00 PM\nPE - 02:50 PM\nDH - 03:40 PM",
        3: "Thursday timetable:\nDigital Electronics - 9:00 AM\nCOI - 10:00 AM\nM/H/R - 11:05 AM\nMATHS - 1:00 PM\nEMT - 02:00 PM\nDCMT - 03:05 PM",
        4: "Friday timetable:\nMATHS - 9:00 AM\nLAB - 10:00 AM-12:30 PM\nM/H/R - 02:00-04:00 PM",
        5: "Saturday timetable:\nNo classes scheduled",
        6: "Sunday timetable:\nNo classes scheduled"
    }

    # Get the timetable for the current day of the week
    current_timetable = timetable.get(current_day, "No timetable available for today")

    return current_timetable


def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello","hi","sup"):
        return "hey! helloooo..."
    
    if user_message in ("sura"):
        return "panna po*ay@@di m@ne"
    
    if user_message in ("who are you?","who are you?","whois"):
        return "ഇത് ഞാനാടാ നിങ്ങട HOD !"
    
    if user_message in ("time?","time"):
        now = datetime.now()
        date_time = now.strftime("%d-%m-%y\n\n%H:%M:%S\n\n%A")

        return str(date_time)
    
    if user_message in ("timetable","time table"):
        return get_timetable_for_day()
    
    return "i dont understand you,നീ ഏതാടാ നായേ\n\ntry:\nwhois\ntime\ntimetable\nsura\n/reminders\n/addreminder"

    
