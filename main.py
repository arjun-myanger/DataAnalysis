import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
from fpdf import FPDF


# ----------------- Load Data -----------------
def load_data():
    """Asks user for a CSV file and loads it into a DataFrame."""
    file_path = input("Enter the path to your CSV file: ").strip()

    if not os.path.exists(file_path):
        print("❌ Error: File not found. Please check the path and try again.")
        return None

    df = pd.read_csv(file_path)
    print("\n✅ Data Loaded Successfully!")
    print(df.head())  # Preview the first few rows
    return df


# ----------------- Data Cleaning -----------------
def clean_data(df):
    """Handles missing values and duplicates."""
    df.drop_duplicates(inplace=True)
    df.fillna(0, inplace=True)  # Fill missing values with 0
    return df


# ----------------- User Selection Menu -----------------
def user_menu():
    """Displays options for the user to choose analysis type."""
    print("\n🔍 What would you like to analyze?")
    print("1️⃣ View Summary Statistics")
    print("2️⃣ Generate Data Visualizations")
    print("3️⃣ Find Correlations Between Columns")
    print("4️⃣ Export Report (CSV + PDF)")
    print("0️⃣ Exit")

    choice = input("Enter your choice: ").strip()
    return choice


# ----------------- Analysis Functions -----------------
def show_summary(df):
    """Displays basic summary statistics."""
    print("\n📊 Data Summary:")
    print(df.describe())


def generate_visualizations(df):
    """Allows user to choose columns for visualizations."""
    print(
        "\n📈 Available Numeric Columns:",
        df.select_dtypes(include=["number"]).columns.tolist(),
    )

    col_x = input("Enter the column for X-axis: ").strip()
    col_y = input("Enter the column for Y-axis: ").strip()

    if col_x not in df.columns or col_y not in df.columns:
        print("❌ Invalid column names. Please try again.")
        return

    # Create scatter plot
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x=df[col_x], y=df[col_y])
    plt.xlabel(col_x)
    plt.ylabel(col_y)
    plt.title(f"{col_y} vs {col_x}")
    plt.savefig("reports/data_visualization.png")
    plt.show()
    print("✅ Visualization saved as 'reports/data_visualization.png'")


def find_correlations(df):
    """Finds and displays correlation between numeric columns."""
    print("\n🔗 Correlation Matrix:")
    corr_matrix = df.corr()
    print(corr_matrix)


def export_report(df):
    """Exports a summary report as a CSV and PDF file."""
    df.describe().to_csv("reports/data_summary.csv")
    print("✅ Summary report saved as 'reports/data_summary.csv'")

    # Generate PDF report
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, "Data Analysis Report", ln=True, align="C")
    pdf.ln(10)

    pdf.set_font("Arial", "", 12)
    for col in df.describe().columns:
        pdf.cell(200, 10, f"{col}: {df[col].mean():.2f} (Avg)", ln=True)

    pdf.output("reports/data_report.pdf")
    print("✅ PDF report saved as 'reports/data_report.pdf'")


# ----------------- Main Program Loop -----------------
def main():
    os.makedirs("reports", exist_ok=True)  # Ensure reports folder exists

    df = load_data()
    if df is None:
        return

    df = clean_data(df)

    while True:
        choice = user_menu()

        if choice == "1":
            show_summary(df)
        elif choice == "2":
            generate_visualizations(df)
        elif choice == "3":
            find_correlations(df)
        elif choice == "4":
            export_report(df)
        elif choice == "0":
            print("👋 Exiting. Thank you for using the data analysis tool!")
            break
        else:
            print("❌ Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
