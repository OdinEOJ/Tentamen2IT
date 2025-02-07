import datetime

def tid():
    while True:
        now = datetime.datetime.now()
        print(f"Current time: {now.hour}:{now.minute}:{now.second}")  # Debug print
        if now.hour == 12 and now.minute == 7:
            print("Klokken er 12:05")
            break  # Exit the loop after printing the message

tid()