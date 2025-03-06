def total_revenue(df):
    """Calculates total revenue."""
    return df["Total_Revenue"].sum()


def most_sold_product(df):
    """Finds the most sold product."""
    return df.groupby("Product")["Units_Sold"].sum().idxmax()
