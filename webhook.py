import requests
from colorama import Fore, init

init(autoreset=True)

def send_webhook(webhook_url, message):
    payload = {
        "content": message,
        "username": "User"
    }
    response = requests.post(webhook_url, json=payload)
    if response.status_code == 204:
        print(Fore.GREEN + f"Webhook sent successfully: {message}")
    else:
        print(Fore.RED + f" Couldnt be sent")

def send_multiple_webhooks():
    webhook_url = input(Fore.MAGENTA + "Enter the webhook link/URL: ")
    message = input(Fore.MAGENTA + "Enter what you want to say: ")
    try:
        count = int(input(Fore.MAGENTA + "How many times do you want it sent: "))
    except ValueError:
        print(Fore.RED + "Invalid number, Sending Once .")
        count = 1

    for i in range(count):
        print(Fore.MAGENTA + f"Sending message {i + 1}...")
        send_webhook(webhook_url, message)

    print(Fore.GREEN + "All messages have been sent")

if __name__ == "__main__":
    send_multiple_webhooks()