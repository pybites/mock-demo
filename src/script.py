import requests

TIPS_URL = "https://codechalleng.es/api/tips/"


def get_tips(url=TIPS_URL):
    response = requests.get(url)
    if response.status_code != 200:
        return []
    return response.json()


if __name__ == '__main__':
    for tip in sorted(get_tips(), key=lambda tip: tip['id']):
        print(f"{tip['id']} - {tip['title']}")
