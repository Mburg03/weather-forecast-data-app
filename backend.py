import requests


API_KEY = "092a86539ad9759bb86cdc3c4bc839dc"


def get_data(place, forecast_days=None, kind=None):
    pass
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    content = response.json()
    return content


if __name__ == "__main__":
    print(get_data(place="Tokyo"))