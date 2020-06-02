from pyowm.caches.lrucache import LRUCache
import pyowm

status = ""
sign = u'\N{DEGREE SIGN}'
temperature = ""


def user_value():
    global status
    global temperature
    owm = pyowm.OWM("087d6d20af763d169b1d4be61e22776b")
    oberservation = owm.weather_at_place("Adelaide,AU")
    weather = oberservation.get_weather()
    temperature = weather.get_temperature('celsius')['temp']
    status = weather.get_status()

user_value()
print(status)
print(temperature)

