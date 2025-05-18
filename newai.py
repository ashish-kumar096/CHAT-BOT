import pyautogui
import time
import pyperclip
import google.generativeai as genai

# Gemini API key
genai.configure(api_key="AIzaSyA-7SN4si8_wTA3BcYaELfh2BLmEmKIonU")

def is_last_message_from_sender(chat_log, sender_name="Chandravanshi"):
    # Split the chat log into lines and check the last non-empty one
    messages = [line for line in chat_log.strip().split('\n') if line.strip()]
    if not messages:
        return False
    last_message = messages[-1]
    return f"] {sender_name}:" in last_message

# Step 1: Click on the Chrome icon
pyautogui.click(828, 1176)
time.sleep(1)

while True:
    time.sleep(5)

    # Step 2: Select and copy chat
    pyautogui.moveTo(1232, 264)
    pyautogui.dragTo(1862, 914, duration=2.0, button='left')
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)
    pyautogui.click(1499, 964)

    # Step 3: Retrieve chat text
    chat_history = pyperclip.paste()
    print("CHAT HISTORY:\n", chat_history)
    print("From Chandravanshi?", is_last_message_from_sender(chat_history))

    if is_last_message_from_sender(chat_history):
        model = genai.GenerativeModel("gemini-1.5-pro")
        convo = model.start_chat(history=[
            {
                "role": "user",
                "parts": ["You are a person named Ashish who speaks Hindi and English. You are from India, and you roast people a little bit in a funny way based on the chat history. Only reply with the next message."]
            }
        ])
        response = convo.send_message(chat_history)
        response_text = response.text.strip()

        print("RESPONSE:\n", response_text)
        pyperclip.copy(response_text)

        # Step 4: Paste the message
        pyautogui.click(1477, 965)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        pyautogui.press('enter')
# Example chat processing
command = '''
[9:55 am, 29/3/2025] Ashish: Hii
[9:55 am, 29/3/2025] Chandravanshi: Hii
[9:56 am, 29/3/2025] Chandravanshi: Bro
[9:56 am, 29/3/2025] Ashish: Kya kr raha hai
[9:56 am, 29/3/2025] Chandravanshi: Padh raha hu
[9:56 am, 29/3/2025] Ashish: Chatbot ka presentation bana le
[9:57 am, 29/3/2025] Chandravanshi: Ha bana raha hu bhai
[10:09 am, 29/3/2025] Ashish: jaldi bana le kal submit krna hai
[10:10 am, 29/3/2025] Chandravanshi: Ha thik ha
'''

model = genai.GenerativeModel("gemini-1.5-pro")
response = model.generate_content(command)

print(response.text)
