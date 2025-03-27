import os
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
import pandas as pd



def notify(driver,threshold_price):
    load_dotenv()# This will load the variables from .env into environment variables

    EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
    EMAIL_APP_PASSWORD = os.getenv("EMAIL_APP_PASSWORD")
    TO_MAIL=os.getenv("TO_MAIL")
    SMTP_SERVER=os.getenv("SMTP_SERVER")
    

    def send_email(subject, body, to_email):
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = TO_MAIL

        try:
            with smtplib.SMTP_SSL(SMTP_SERVER, 465) as smtp:
                smtp.login(EMAIL_ADDRESS, EMAIL_APP_PASSWORD)
                smtp.send_message(msg)
            print("Email sent successfully.")
        except Exception as e:
            print(f"Error sending email: {e}")

    def notify_if_price_below_threshold(csv_path, threshold_price, to_email):
        df = pd.read_csv(csv_path)
        cheap_flights = df[df['Price'].str.replace(',', '').str[1:].astype(int) < threshold_price]
        print(f"{len(cheap_flights)} flights found")
        if not cheap_flights.empty:
            email_body = f"🚀 {len(cheap_flights)} Flight deals found with set price less than ${threshold_price}:\n\n {driver.current_url} \n\n"
            i=0
            for index, row in cheap_flights.iterrows():
                i=i+1
                email_body += (f"{i}:\n\n "
                    f"Airline Name: {row['Airline Name']} \n| {row['From']} ➡ {row['To']} | \n"
                    f"Departure: {row['Departure']}-Arrival: {row['Arrival']}\n\n"
                    f"Return:\n Airline Name: {row['Return Airline Name']} | {row['Return From']}(return) ➡ {row['Return To']}(return) | \n"
                    f"Departure: {row['Return Departure']}- Arrival: {row['Return Arrival']}\n\n"
                    f"💰 Price: {row['Price']}\n"
                    f"{'-'*50}\n"
                )
            send_email(
                subject="🔥 Cheap Flight Alert",
                body=email_body,
                to_email=to_email
            )
        else:
            print(f"No flights found under {threshold_price}.")


    notify_if_price_below_threshold(
    csv_path="output/flights_output.csv",
    threshold_price=threshold_price,  # change this threshold as per your need
    to_email=TO_MAIL
)