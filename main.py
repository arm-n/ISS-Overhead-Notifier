import requests
from datetime import datetime
import smtplib

# Your email credentials (use environment variables or secrets in production)
MY_EMAIL = "gokucodes247@gmail.com"
PASSWORD = "your_password_here"

# Your geographic coordinates
MY_LAT = 15.087380
MY_LNG = -96.547745

# Parameters for Sunrise-Sunset API
parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,  # 24-hour format
}

# Check if ISS is currently overhead (±5 degrees of your location)
def is_iss_overhead():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    iss_position = response.json()["iss_position"]

    iss_lat = float(iss_position["latitude"])
    iss_lng = float(iss_position["longitude"])

    print("ISS Position:", (iss_lat, iss_lng))

    if MY_LAT - 5 <= iss_lat <= MY_LAT + 5 and MY_LNG - 5 <= iss_lng <= MY_LNG + 5:
        return True
    return False

# Check if it's currently night at your location
def is_night():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()["results"]

    sunrise_hour = int(data["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(data["sunset"].split("T")[1].split(":")[0])
    current_hour = datetime.utcnow().hour

    print(f"Sunrise: {sunrise_hour}, Sunset: {sunset_hour}, Now: {current_hour}")

    if current_hour >= sunset_hour or current_hour <= sunrise_hour:
        return True
    return False

# Send email if ISS is overhead and it's night
if is_iss_overhead() and is_night():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Watch Out 🚀\n\nThe ISS is above you in the sky!"
        )
        print("✅ Email sent!")
else:
    print("📡 No ISS overhead or it's daytime.")
