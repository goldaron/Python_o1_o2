# Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api. 
# Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen ja tulostaa sitä vastaavan säätilan tekstin sekä lämpötilan Celsius-asteina. 
# Perehdy rajapinnan dokumentaatioon riittävästi. Palveluun rekisteröityminen on tarpeen, jotta saat rajapintapyynnöissä tarvittavan API-avaimen (API key). 
# Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi.

import requests
# importing os module for environment variables
import os
# importing necessary functions from dotenv library
from dotenv import load_dotenv, dotenv_values 
# loading variables from .env file
load_dotenv()
# accessing and printing value
key = os.getenv("MY_KEY")

paikkakunta = input("Anna paikkakunta: ")

pyyntö = f"http://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&appid={key}&units=metric"
vastaus = requests.get(pyyntö).json()

print(f"\nSäätilanne, {paikkakunta}:")
print(vastaus["weather"][0]["description"])
print("Lämpötila:", vastaus["main"]["temp"], "°C")