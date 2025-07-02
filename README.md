# 🛰️ ISS Overhead Notifier

A Python automation script that notifies you via email when the **International Space Station (ISS)** is flying overhead **your location** and it’s dark enough to see it! It fetches live ISS coordinates and your local sunrise/sunset time using public APIs, and sends an email if the ISS is visible.

## ✨ Features

* Tracks real-time ISS location using Open Notify API.
* Checks day/night condition via Sunrise-Sunset API.
* Sends you an email alert if ISS is nearby **at night**.

## 🧰 Tech Stack

* Python 3
* `requests` for API communication
* `datetime` for time checking
* `smtplib` for email delivery

## 📂 Project Structure

```
📦 iss-overhead-notifier
├── 📄 main.py                # Main script to run the program
├── 📁 SMTP
│   └── 📁 SEND_EMAIL
│       └── 📄 main.py       # (Optional) Handles SMTP logic if modularized
├── 📄 README.md              # Documentation
```

## ▶️ How to Run

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/iss-overhead-notifier.git
cd iss-overhead-notifier
```

2. **Install dependencies**

```bash
pip install requests
```

3. **Set your credentials**

In `main.py`, replace:

```python
MY_EMAIL = "youremail@example.com"
PASSWORD = "yourpassword"
```

with your real email and app password. (Use [App Passwords](https://support.google.com/accounts/answer/185833) if you're using Gmail.)

4. **Run the script**

```bash
python main.py
```

## 🧪 Example Output

```
ISS position: (76.84, 14.97)
Sunrise: 5 & Sunset: 18
```

Then, if ISS is visible:

📩 An email is sent: "Subject: Watch Out\n\nThe ISS is above YOU in the sky"

## 🔁 How It Works

* `is_iss_overhead()`:

  * Checks if ISS is within ±5° latitude and longitude of your location
* `is_night()`:

  * Checks if current time is after sunset or before sunrise
* If both are `True`, an email is sent

## 🚀 Future Enhancements

* Run the script every 60 seconds using a scheduler (like `while True + time.sleep()`)
* Deploy as a background service or use GitHub Actions with cron

## 🛡️ Safety Tips

* Use environment variables or `.env` file for email credentials
* Do not expose real passwords in the script

## 📄 License

This project is licensed under the MIT License.

---

Watch the stars and automate your alerts 🌌
