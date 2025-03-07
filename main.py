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
    """Allows user to choose numeric columns for visualizations."""
    numeric_columns = df.select_dtypes(include=["number"]).columns.tolist()

    print("\n📈 Available Numeric Columns:")
    for idx, col in enumerate(numeric_columns, start=1):
        print(f"{idx}. {col}")

    try:
        x_index = int(input("Enter the number for the X-axis column: ")) - 1
        y_index = int(input("Enter the number for the Y-axis column: ")) - 1

        if x_index not in range(len(numeric_columns)) or y_index not in range(
            len(numeric_columns)
        ):
            print("❌ Invalid selection. Please enter a valid number from the list.")
            return

        col_x = numeric_columns[x_index]
        col_y = numeric_columns[y_index]

        # Generate scatter plot
        plt.figure(figsize=(8, 5))
        sns.scatterplot(x=df[col_x], y=df[col_y])
        plt.xlabel(col_x)
        plt.ylabel(col_y)
        plt.title(f"{col_y} vs {col_x}")

        save_path = "reports/data_visualization.png"
        plt.savefig(save_path)
        print(f"✅ Visualization saved as '{save_path}'")
        plt.show()

    except ValueError:
        print("❌ Please enter valid numbers.")


def find_correlations(df):
    """Finds and displays correlation between numeric columns."""
    print("\n🔗 Finding Correlations...")

    # Use a copy of df instead of modifying the original
    numeric_df = df.select_dtypes(include=["number"]).copy()

    if numeric_df.empty:
        print("❌ No numeric columns found to calculate correlation.")
        return

    corr_matrix = numeric_df.corr()

    if corr_matrix.empty:
        print("❌ Correlation matrix is empty. No valid correlations.")
    else:
        print("\n✅ Correlation Matrix:")
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

    while True:  # Ensure this loop exists
        choice = user_menu()

        if choice == "1":
            show_summary(df)
        elif choice == "2":
            generate_visualizations(df)
        elif choice == "3":
            print("\n🛠️ Running Correlation Analysis...")  # Debugging message
            find_correlations(df)  # Calls the function
        elif choice == "4":
            export_report(df)
        elif choice == "0":
            print("👋 Exiting. Thank you for using the data analysis tool!")
            break  # This will now correctly exit the while loop
        else:
            print("❌ Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
