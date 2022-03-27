from urllib.error import HTTPError
import requests
from backgroundtask import BackgroundTask


class CheckWeather(BackgroundTask):
    async def task(*_, **__) -> None:
        url = "https://api.met.no/weatherapi/locationforecast/2.0/compact"
        r = requests.get(
            url,
            params={"lat": 13.753859, "lon": 100.500219},  # Bangkok
            headers={"User-Agent": "test"},
        )
        r.raise_for_status()

        temperature = r.json()["properties"]["timeseries"][0]["data"]["instant"][
            "details"
        ]["air_temperature"]
        print("The temperature in Bangkok is ", temperature, u"\N{DEGREE SIGN}", "C")
