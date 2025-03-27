# ✈️ Flight Price Tracker

A web scraping tool built with **Selenium** and **BeautifulSoup** that tracks round-trip flight prices, saves results to a CSV, and sends an email notification if prices fall below a defined threshold.

---

## 📁 Project Structure
```
project_root/
│
├── data/
│   └── tracked_prices.csv            # Scraped flight data
│
├── screenshots/                      # Stores screenshots if needed during debugging
│
├── utils/
│   ├── browser.py                    # Browser initialization code
│   ├── notifier.py                   # Email sending logic
│   └── tracker.py                    # Flight scraping and CSV export logic
│
├── main.py                           # Entry point to run the scraper and notifier
├── demo.ipynb                        # Jupyter notebook demo
├── test_selenium.py                  # Test script for Selenium setup
├── .env                              # Contains sensitive environment variables (not committed)
├── .env.example                      # Example of environment variables required
├── .gitignore                        # Ignore .env and other sensitive files
├── requirements.txt                  # Python dependencies
└── README.md                         # Project documentation
```

---

## ✅ Features
- Scrapes round-trip flight details: Airline, From, To, Departure, Arrival, Return details, and Price.
- Saves flight data in `data/flights_output.csv`.
- Sends email notification if the price falls below a threshold.

---

## 🚀 How to Set Up

### 1️⃣ Clone the repository
```bash
git clone <your_repo_url>
cd <repo_folder>
```

### 2️⃣ Create and activate a virtual environment
```bash
python -m venv webscrapping_env
source webscrapping_env/bin/activate   # On Windows: webscrapping_env\Scripts\activate
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Setup environment variables
- Copy the example file:
```bash
cp .env.example .env
```
- Fill in your `.env` with your email address, app password, and price threshold.

### 5️⃣ Run the tracker
```bash
python main.py
```

---

## 📧 Email Notification Setup
- This project uses Gmail SMTP.
- You need to [generate an App Password from Google](https://support.google.com/accounts/answer/185833?hl=en) and use that in the `.env` file.

---

## 📜 Example .env.example file
```env
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_APP_PASSWORD=your_gmail_app_password
THRESHOLD_PRICE=20000
SMTP_SERVER=smtp.gmail.com
```

---

## 💡 Future Improvements
- Add Telegram or WhatsApp notifications
- Dockerize the app
- Add automatic daily run with cron jobs or GitHub Actions

---

## 🤝 Contributing
Contributions are welcome! Please open issues or pull requests.

---

## 📄 License
This project is for educational purposes only.

---

> Built with ❤️ using Python, Selenium, and BeautifulSoup.

