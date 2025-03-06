import matplotlib.pyplot as plt
import seaborn as sns


def sales_trend(df):
    """Plots daily sales trends."""
    sales_trend = df.groupby("Date")["Total_Revenue"].sum()
    plt.figure(figsize=(10, 5))
    plt.plot(sales_trend, marker="o", linestyle="-")
    plt.xlabel("Date")
    plt.ylabel("Total Revenue ($)")
    plt.title("Daily Sales Trend")
    plt.xticks(rotation=45)
    plt.grid()
    plt.show()


def sales_by_region(df):
    """Plots sales revenue by region."""
    region_sales = df.groupby("Region")["Total_Revenue"].sum()
    plt.figure(figsize=(8, 5))
    sns.barplot(x=region_sales.index, y=region_sales.values)
    plt.xlabel("Region")
    plt.ylabel("Total Revenue ($)")
    plt.title("Sales by Region")
    plt.show()
