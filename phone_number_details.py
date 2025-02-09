""" A program that gives you details about phone number must enter number with prefix"""
import phonenumbers
from phonenumbers import geocoder , carrier , timezone
print("========== Welcome to phone number details program ==========")
while True:
    try:
        print("Enter phone number with country code: ")
        user_input=input()
        phone_num=phonenumbers.parse(user_input,None)
        break
    except phonenumbers.phonenumberutil.NumberParseException:
        print("Please enter country code before the phone number!")

# Get company provider
company_provider=geocoder.country_name_for_number(phone_num,"en")
# Get carrier name
carrier_pr=carrier.name_for_number(phone_num,"en")
# Get time zone
time=timezone.time_zones_for_number(phone_num)

print(f"{phone_num}\n")
print(f"Company provider: {company_provider}\n")
print(f"Carrier: {carrier_pr}\n")
for item in time:
    print(f"Time zone: {item}")
