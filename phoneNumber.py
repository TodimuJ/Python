import phonenumbers
from phonenumbers import geocoder, carrier

number = input("Type in phone number with country code and no spaces: ")
country = phonenumbers.parse(number, "CH")
service = phonenumbers.parse(number, "RO")

print("Country: " + geocoder.description_for_number(country, "en") + "\n")
# print("Carrier:" + carrier.name_for_number(service, "en"))