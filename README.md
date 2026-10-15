# TASK 2: Stock Portfolio Tracker 📈

A clean, interactive Python application that tracks stock holdings and calculates the total portfolio investment value based on manually defined stock prices.

---

## 🎯 Goal & Objectives
- Allow users to input stock symbols and quantities.
- Use a predefined (hardcoded) dictionary to store stock prices.
- Calculate the total value for each holding and the total portfolio investment.
- Provide clear, formatted summaries displaying shares, prices, total value, and percentage weights.
- Optionally save the final portfolio summary to a `.txt` report or `.csv` spreadsheet.

---

## 🔑 Key Concepts Used

| Concept | Implementation in Project |
| :--- | :--- |
| **Dictionary** | `STOCK_PRICES` stores ticker-to-price mappings (e.g., `{"AAPL": 180.00, "TSLA": 250.00}`). `portfolio` tracks user holdings (symbol -> shares). |
| **Input / Output** | Interactive CLI with prompts, input validation, case-insensitivity, and formatted ASCII summary tables. |
| **Basic Arithmetic** | Multiplications (`shares * price`), accumulations (`sum()`), and percentage calculations (`(stock_total / total_investment) * 100`). |
| **File Handling (Optional)** | Python's `open()` context manager and `csv` module for exporting `.txt` reports and `.csv` spreadsheets. |
| **Defensive Programming** | Graceful error handling for invalid stock symbols, negative numbers, non-numeric inputs, and empty submissions. |

---

## 📁 Project Structure

```
task II/
├── portfolio_tracker.py      # Main interactive application
├── test_portfolio.py         # Automated unit test suite
├── portfolio_summary.txt     # Sample exported text report
├── portfolio_summary.csv     # Sample exported CSV spreadsheet
└── README.md                 # Project documentation
```

---

## 🚀 How to Run

### 1. Run the Portfolio Tracker
Open your terminal in this directory and execute:

```powershell
py portfolio_tracker.py
```
*(or `python portfolio_tracker.py`)*

### 2. Run the Unit Tests
To verify all calculations and file operations:

```powershell
py test_portfolio.py
```

---

## 💡 Example Usage Walkthrough

### Terminal Interaction:
```text
############################################################
#           WELCOME TO STOCK PORTFOLIO TRACKER             #
############################################################
Track your investments based on current stock market prices.

========================================
       AVAILABLE STOCKS & PRICES        
========================================
Stock Symbol     |    Price per Share
----------------------------------------
AAPL             | $           180.00
AMZN             | $           185.00
GOOGL            | $           175.50
META             | $           500.00
MSFT             | $           420.00
NVDA             | $           120.00
TSLA             | $           250.00
========================================

Enter stock symbol (or 'DONE' to finish): AAPL
Enter quantity of shares: 5
 [+] Added 5 share(s) of AAPL to portfolio.

Enter stock symbol (or 'DONE' to finish): TSLA
Enter quantity of shares: 2
 [+] Added 2 share(s) of TSLA to portfolio.

Enter stock symbol (or 'DONE' to finish): DONE

====================================================================
                   PORTFOLIO SUMMARY REPORT                   
====================================================================
Stock    |   Quantity |    Price ($) |      Value ($) |    Weight
--------------------------------------------------------------------
AAPL     |          5 | $     180.00 | $       900.00 |     64.3%
TSLA     |          2 | $     250.00 | $       500.00 |     35.7%
====================================================================
 TOTAL PORTFOLIO INVESTMENT VALUE: $1,400.00
====================================================================

Save Options:
 [1] Save as Text file (.txt)
 [2] Save as CSV spreadsheet (.csv)
 [3] Save as Both (.txt and .csv)
 [4] Do not save (Exit)

Enter your choice (1/2/3/4): 3
 [OK] Portfolio successfully saved to:
     - Text Report: portfolio_summary.txt
     - CSV File:    portfolio_summary.csv
```

---

## 📄 Export Formats

### Text Report (`.txt`)
Includes timestamped summary table with formatted currency and percentage weights:
```text
====================================================================
                   STOCK PORTFOLIO SUMMARY                    
 Generated on: 2026-10-16 02:35:51
====================================================================
Stock    |   Quantity |    Price ($) |      Value ($) |    Weight
--------------------------------------------------------------------
AAPL     |          5 | $     180.00 | $       900.00 |     64.3%
TSLA     |          2 | $     250.00 | $       500.00 |     35.7%
====================================================================
 TOTAL PORTFOLIO INVESTMENT VALUE: $1,400.00
====================================================================
```

### CSV Spreadsheet (`.csv`)
Can be directly opened in Microsoft Excel, Google Sheets, or LibreOffice:
```csv
Stock Symbol,Quantity,Price Per Share ($),Total Value ($),Weight (%)
AAPL,5,180.00,900.00,64.29
TSLA,2,250.00,500.00,35.71

TOTAL INVESTMENT VALUE,,,1400.00,100.00%
```
