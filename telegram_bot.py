import requests

# Replace with your actual bot token and chat ID
BOT_TOKEN = "7557174507:AAFSmFW5nxJ-fLOPS-B_wi0uT5wkQ5-PEx8"
CHAT_ID = "1278635048"

def send_telegram_signal(signal_row):
    signal = signal_row['signal']
    time = signal_row['time']
    confidence = signal_row.get('confidence', 'N/A')

    message = f"📢 Signal Alert\nTime: {time}\nSignal: {signal}\nConfidence: {confidence}"
    
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}

    response = requests.post(url, data=data)

    if response.status_code != 200:
        raise Exception(f"Telegram Error: {response.text}")
