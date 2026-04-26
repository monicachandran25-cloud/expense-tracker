import pandas as pd
import matplotlib.pyplot as plt

def generate_report():
    try:
        # Read data
        df = pd.read_csv("data.csv", names=["date", "amount", "category"])

        # Convert amount to numeric (safety)
        df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

        # Drop invalid rows
        df = df.dropna()

        # Total spending
        total = df["amount"].sum()
        print("\n💰 Total Spending:", total)

        # Category-wise spending
        category_sum = df.groupby("category")["amount"].sum()
        print("\n📊 Spending by Category:\n")
        print(category_sum)

        # Create chart
        category_sum.plot(kind="bar")
        plt.title("Expenses by Category")
        plt.xlabel("Category")
        plt.ylabel("Amount")

        # Save chart
        plt.tight_layout()
        plt.savefig("chart.png")
        plt.close()

        print("\n📈 Chart saved as chart.png")

    except FileNotFoundError:
        print("❌ data.csv not found. Please add some expenses first.")