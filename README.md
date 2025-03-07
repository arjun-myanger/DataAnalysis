# 📊 Interactive Data Analysis Tool

## 🚀 Overview
This Python-based tool allows users to **analyze any dataset interactively**. It provides:
- **Automatic data loading & cleaning** 📂
- **Statistical summaries** 📊
- **Correlation analysis** 🔗
- **Customizable visualizations** 📈
- **Report generation (CSV & PDF)** 📄

Users can **upload any CSV file** and choose what they want to analyze dynamically!

---

## 📂 Project Structure
```
DataAnalysis/
│── data/                     # Store dataset files
│── reports/                  # Generated reports (CSV, PDF, images)
│── main.py                   # Main script for analysis
│── README.md                 # Documentation
│── requirements.txt           # Dependencies
```

---

## 🔧 Installation & Setup
### 1️⃣ Install Dependencies
Make sure you have Python installed, then run:
```sh
pip install pandas matplotlib seaborn fpdf
```

### 2️⃣ Clone the Repository (Optional)
```sh
git clone https://github.com/YOUR_USERNAME/data_analysis_tool.git
cd data_analysis_tool
```

### 3️⃣ Run the Program
```sh
python main.py
```

---

## 📑 Features

### ✅ 1️⃣ Load & Clean Any CSV Dataset
- **Handles missing values & duplicates automatically**.
- Supports **any dataset** with numeric values.

### ✅ 2️⃣ View Statistical Summaries
- Displays **mean, min, max, and standard deviation** for numeric columns.

### ✅ 3️⃣ Find Correlations 🔗
- Computes **correlation matrices** to show relationships between numeric columns.

### ✅ 4️⃣ Generate Custom Visualizations 📈
- Users can **select columns for scatter plots**.
- Saves **plots as images in `reports/` folder**.

### ✅ 5️⃣ Export Reports 📄
- **CSV summary** of key insights.
- **PDF report** with numerical summaries.

---

## 🎯 How to Use
1. **Run `python main.py`**
2. **Enter the path to your dataset (CSV file).**
3. **Choose an analysis option:**
   - `1️⃣` View summary statistics
   - `2️⃣` Generate visualizations
   - `3️⃣` Find correlations
   - `4️⃣` Export reports (CSV + PDF)
   - `0️⃣` Exit

---

## 📌 Contributing
Pull requests are welcome! If you find any issues, feel free to open an issue.

---

## 📜 License
This project is open-source and available under the **MIT License**.

