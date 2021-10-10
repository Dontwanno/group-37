import requests


def get_weather(city):
    # set the api key and the url of the weather website
    api_key = "094eaa9002d7545fbda3e4c9f5956fe9"
    base_url = "https://api.openweathermap.org/data/2.5/forecast?"
    # complete url
    complete_url = base_url + "appid=" + api_key + "&q=" + city

    # get the info from the API
    response = requests.get(complete_url)
    response_json = response.json()
    # check if the city exists
    if response_json["cod"] != "404":
        print(response_json)
        return response_json
    else:
        print("City not found")
        return 0


get_weather("Delft")
