import pandas as pd

# Load the scraped Flipkart data

df = pd.read_csv(r"C:\Users\sapna\Downloads\flipkart.csv")


print(df.head())

# Exporting to a new file
df.to_csv("cleaned_flipkart_data.csv", index=False)

print("Export Successful!")