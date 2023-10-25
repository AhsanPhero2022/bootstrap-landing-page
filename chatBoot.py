import pyautogui as spam
import time

# List of SMS messages
sms_messages = [
    "I'm deeply sorry.",
    "I apologize for my actions.",
    "Please forgive me.",
    "I regret my behavior.",
    "I didn't mean to hurt you.",
    "I'm truly sorry for what I did.",
    "I hope you can find it in your heart to forgive me.",
    "My actions were thoughtless, and I apologize.",
    "I'm remorseful for causing you pain.",
    "I'm sorry for any misunderstandings.",
    "I take full responsibility for my mistake.",
    "I value our friendship and am sorry for any damage.",
    "I promise to do better in the future.",
    "I'm willing to make amends.",
    "I never intended to upset you.",
    "I understand why you're upset, and I'm sorry.",
    "I'm deeply apologetic for my behavior.",
    "I'm committed to making things right.",
    "I'm sorry for any inconvenience I've caused.",
    "I miss our friendship and want to mend things."
]

limit = int(input("How many messages to send? "))

# Sleep for a few seconds to give you time to focus on the input field
time.sleep(5)

# Ensure the number of messages to send doesn't exceed the length of the list
limit = min(limit, len(sms_messages))

for i in range(limit):
    # Select the next message from the list
    message = sms_messages[i]

    # Type the message
    spam.typewrite(message)

    # Press the Enter key to send the message (adjust the key if needed)
    spam.press("enter")

    # Sleep for a moment to simulate typing speed
    time.sleep(1.0)  # Adjust the duration as needed

print(f"Sent {limit} SMS messages.")

