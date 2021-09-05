from phonenumbers import carrier
import phonenumbers
from Test import number

from phonenumbers import geocoder

ch_number = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_number, "es"))

service_number = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_number, "es"))
