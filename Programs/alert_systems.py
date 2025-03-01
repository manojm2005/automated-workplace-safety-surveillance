import pyttsx3
import threading
import time

# Initialize the speech engine globally for efficiency
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Adjust speech speed

# Cache to track current alerts and enforce the 5-second gap
last_alert_time = 0
alert_interval = 5  # Fixed alert gap in seconds
alert_lock = threading.Lock()

def speak(message):
    """Speak the given message using pyttsx3."""
    engine.say(message)
    engine.runAndWait()

def generate_alert(missing_ppe):
    """Generates voice alerts with a 5-second gap between repeats."""
    global last_alert_time

    if not missing_ppe:
        return

    # Ensure alerts only repeat every 5 seconds
    current_time = time.time()
    with alert_lock:
        if current_time - last_alert_time < alert_interval:
            return
        last_alert_time = current_time

    # Determine the alert message accurately
    unique_ppe = list(set(missing_ppe))  # Avoid duplicate items

    # 1. If one item is missing, alert for that specific item
    if len(unique_ppe) == 1:
        item = unique_ppe[0]
        if missing_ppe.count(item) == 1:
            alert_message = f"Please wear your {item}."
        else:
            alert_message = f"Please all of you wear your {item}."

    # 2. If more than one type of PPE is missing, give a general PPE alert
    elif len(unique_ppe) > 1:
        alert_message = "Please wear your personal protective equipment."

    # Trigger voice alert
    print("ALERT:", alert_message)  # Log the alert
    threading.Thread(target=speak, args=(alert_message,)).start()
