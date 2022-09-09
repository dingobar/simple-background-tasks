import requests


async def check_weather_in_bangkok() -> None:
    """Call the met api and get the weather forecast for Bangkok."""
    url = "https://api.met.no/weatherapi/locationforecast/2.0/compact"
    r = requests.get(
        url,
        params={"lat": 13.753859, "lon": 100.500219},  # Bangkok
        headers={"User-Agent": "test"},
    )
    r.raise_for_status()

    temperature = r.json()["properties"]["timeseries"][0]["data"]["instant"]["details"][
        "air_temperature"
    ]
    print("The temperature in Bangkok is ", temperature, "\N{DEGREE SIGN}", "C")


async def print_message(message: str):
    """Print a message to the console.

    Args:
        message (str): The message.
    """
    print(message)
