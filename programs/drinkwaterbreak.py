from plyer import notification
import win32com.client as win
import time
a = 5
b = 3
for i in range(b):
    time.sleep(a)
    title = "drink water"
    message = "Abhijeet drink water immediately, for good health"

    notification.notify(
        title=title,
        message=message,
        app_name="drink water reminder",
        timeout=10  # Display duration in seconds
    )
    spk = win.Dispatch("SAPI.SpVoice")
    spk.speak(message)
    print("have water!!")