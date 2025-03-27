import pandas as pd


def save(flight_data):
    df = pd.DataFrame(flight_data)
    df.to_csv("output/flights_output.csv", index=False)
    print("✅ Saved to flights_output.csv!")