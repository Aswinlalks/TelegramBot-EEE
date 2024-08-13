from datetime import datetime


def get_timetable_for_day():
    # Get the current day of the week (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
    current_day = datetime.now().weekday()

    # Define the timetable for each day of the week
    timetable = {
        0: "Monday timetable:\nSIM - 9:00 AM\nPS-1 - 10:00 AM\nIE & FT - 11:05 AM\nLAB - 1:00-4:00 PM",
        1: "Tuesday timetable:\nMPMC - 9:00 AM\nS & S - 10:00 AM\nPS-1 - 11:05 AM\nSIM - 1:00 PM\nDM - 02:10 PM\nS & S - 03:05 PM",
        2: "Wednesday timetable:\nLAB - 9:00 AM-12 PM\nIE & FT - 1:00 PM\nMentoring Hour - 02:00 PM\nDM - 02:50 PM\nDH - 03:40 PM",
        3: "Thursday timetable:\nPS-1 - 9:00 AM\nMPMC - 10:00 AM\nSIM - 11:05 AM\nIE & FT - 1:00 PM\nS & S - 02:00 PM\nMPMC - 03:05 PM",
        4: "Friday timetable:\nS & S - 9:00 AM\nMPMC - 9:50 AM\nSIM - 10:50 AM\nPS-1 - 11:40 AM\nM/H/R - 02:00 - 4:00 PM",
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
        return "i am batman"
    
    if user_message in ("time?","time"):
        now = datetime.now()
        date_time = now.strftime("%d-%m-%y\n\n%H:%M:%S\n\n%A")

        return str(date_time)
    
    if user_message in ("/timetable@rizzrizzrizzbot","time table","/timetable"):
        return get_timetable_for_day()
    
    return "i dont understand you,\n\ntry:\nwhois\ntime\nsura\n/timetable\n/assignments\n/notes\n/uptime"



    
