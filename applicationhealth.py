import requests

def check_application_status(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return 'up'
        else:
            return 'down'
    except requests.exceptions.RequestException as e:
        return 'down'

def main():
    url = "https://www.labourbook.online/"
    status = check_application_status(url)
    if status == 'up':
        print(f"The application at {url} is UP.")
    else:
        print(f"The application at {url} is DOWN.")

if __name__ == "__main__":
    main()
