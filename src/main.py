from data_loader import load_data
from data_cleaner import clean_data
from analysis import total_revenue, most_sold_product, save_summary_report
from visualization import sales_trend, sales_by_region


def main():
    file_path = "../data/sample_sales_data.csv"  # Ensure correct file path
    df = load_data(file_path)
    if df is None:
        return

    df = clean_data(df)

    # Print insights
    print(f"Total Revenue: ${total_revenue(df):,.2f}")
    print(f"Most Sold Product: {most_sold_product(df)}")

    # Save reports
    save_summary_report(df)  # Saves the summary as a CSV file
    sales_trend(df, save_path="reports/sales_trend.png")  # Saves sales trend chart
    sales_by_region(
        df, save_path="reports/sales_by_region.png"
    )  # Saves region sales chart


if __name__ == "__main__":
    main()
