"""
=============================================================================
TASK 2: Stock Portfolio Tracker
=============================================================================
A Python program that calculates the total investment value of a stock
portfolio based on manually defined (hardcoded) stock prices.

Key Concepts Used:
- Dictionaries: Storing stock price mappings and user portfolio holdings.
- Input / Output: Receiving stock names/quantities and displaying formatted summaries.
- Basic Arithmetic: Calculating per-stock totals and aggregate investment value.
- File Handling: Exporting portfolio summary reports to .txt or .csv files.
=============================================================================
"""

import csv
from datetime import datetime
from typing import Dict, Tuple

# Hardcoded dictionary defining stock prices (in USD)
STOCK_PRICES: Dict[str, float] = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "GOOGL": 175.50,
    "MSFT": 420.00,
    "AMZN": 185.00,
    "NVDA": 120.00,
    "META": 500.00,
}


def display_market_prices(prices: Dict[str, float]) -> None:
    """Display the list of available stocks and their hardcoded prices."""
    print("\n" + "=" * 40)
    print("       AVAILABLE STOCKS & PRICES        ")
    print("=" * 40)
    print(f"{'Stock Symbol':<16} | {'Price per Share':>18}")
    print("-" * 40)
    for symbol, price in sorted(prices.items()):
        print(f"{symbol:<16} | ${price:>17.2f}")
    print("=" * 40)


def calculate_portfolio_totals(
    portfolio: Dict[str, int | float],
    prices: Dict[str, float]
) -> Tuple[Dict[str, Dict[str, float]], float]:
    """
    Calculate the total value for each holding and the aggregate portfolio value.

    Returns:
        breakdown: Dictionary mapping symbol to {shares, price, total_value, weight}
        total_investment: Sum of all holdings' values
    """
    total_investment = sum(portfolio[sym] * prices[sym] for sym in portfolio)
    breakdown = {}

    for sym, shares in portfolio.items():
        unit_price = prices[sym]
        stock_total = shares * unit_price
        weight = (stock_total / total_investment * 100) if total_investment > 0 else 0.0
        breakdown[sym] = {
            "shares": shares,
            "unit_price": unit_price,
            "total_value": stock_total,
            "weight": weight,
        }

    return breakdown, total_investment


def display_portfolio_summary(
    portfolio: Dict[str, int | float],
    prices: Dict[str, float]
) -> float:
    """Display a formatted summary table of the user's investment portfolio."""
    if not portfolio:
        print("\n[!] Your portfolio is currently empty.")
        return 0.0

    breakdown, total_investment = calculate_portfolio_totals(portfolio, prices)

    print("\n" + "=" * 68)
    print("                   PORTFOLIO SUMMARY REPORT                   ")
    print("=" * 68)
    print(f"{'Stock':<8} | {'Quantity':>10} | {'Price ($)':>12} | {'Value ($)':>14} | {'Weight':>9}")
    print("-" * 68)

    for sym, data in sorted(breakdown.items()):
        shares_str = f"{data['shares']:.2f}" if isinstance(data['shares'], float) and not data['shares'].is_integer() else f"{int(data['shares'])}"
        print(
            f"{sym:<8} | "
            f"{shares_str:>10} | "
            f"${data['unit_price']:>11.2f} | "
            f"${data['total_value']:>13.2f} | "
            f"{data['weight']:>8.1f}%"
        )

    print("=" * 68)
    print(f" TOTAL PORTFOLIO INVESTMENT VALUE: ${total_investment:,.2f}")
    print("=" * 68)

    return total_investment


def save_portfolio_to_txt(
    portfolio: Dict[str, int | float],
    prices: Dict[str, float],
    filename: str = "portfolio_summary.txt"
) -> str:
    """Export the portfolio summary report to a .txt file."""
    breakdown, total_investment = calculate_portfolio_totals(portfolio, prices)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filename, mode="w", encoding="utf-8") as file:
        file.write("=" * 68 + "\n")
        file.write("                   STOCK PORTFOLIO SUMMARY                    \n")
        file.write(f" Generated on: {timestamp}\n")
        file.write("=" * 68 + "\n")
        file.write(f"{'Stock':<8} | {'Quantity':>10} | {'Price ($)':>12} | {'Value ($)':>14} | {'Weight':>9}\n")
        file.write("-" * 68 + "\n")

        for sym, data in sorted(breakdown.items()):
            shares_str = f"{data['shares']:.2f}" if isinstance(data['shares'], float) and not data['shares'].is_integer() else f"{int(data['shares'])}"
            file.write(
                f"{sym:<8} | "
                f"{shares_str:>10} | "
                f"${data['unit_price']:>11.2f} | "
                f"${data['total_value']:>13.2f} | "
                f"{data['weight']:>8.1f}%\n"
            )

        file.write("=" * 68 + "\n")
        file.write(f" TOTAL PORTFOLIO INVESTMENT VALUE: ${total_investment:,.2f}\n")
        file.write("=" * 68 + "\n")

    return filename


def save_portfolio_to_csv(
    portfolio: Dict[str, int | float],
    prices: Dict[str, float],
    filename: str = "portfolio_summary.csv"
) -> str:
    """Export the portfolio holdings and totals to a .csv file."""
    breakdown, total_investment = calculate_portfolio_totals(portfolio, prices)

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        # Header row
        writer.writerow(["Stock Symbol", "Quantity", "Price Per Share ($)", "Total Value ($)", "Weight (%)"])

        # Data rows
        for sym, data in sorted(breakdown.items()):
            writer.writerow([
                sym,
                data["shares"],
                f"{data['unit_price']:.2f}",
                f"{data['total_value']:.2f}",
                f"{data['weight']:.2f}",
            ])

        # Summary footer row
        writer.writerow([])
        writer.writerow(["TOTAL INVESTMENT VALUE", "", "", f"{total_investment:.2f}", "100.00%"])

    return filename


def get_valid_quantity() -> float:
    """Prompt user until a positive number is entered for quantity."""
    while True:
        qty_input = input("Enter quantity of shares: ").strip()
        try:
            qty = float(qty_input)
            if qty <= 0:
                print(" [!] Quantity must be greater than 0. Please try again.")
                continue
            # If it's a whole number, cast to int
            return int(qty) if qty.is_integer() else qty
        except ValueError:
            print(" [!] Invalid input. Please enter a numerical quantity (e.g., 5 or 10.5).")


def main() -> None:
    """Main interactive execution flow."""
    print("\n" + "#" * 60)
    print("#           WELCOME TO STOCK PORTFOLIO TRACKER             #")
    print("#" * 60)
    print("Track your investments based on current stock market prices.")

    # Show initial price board
    display_market_prices(STOCK_PRICES)

    portfolio: Dict[str, int | float] = {}

    print("\nInstructions:")
    print(" - Enter stock symbol and quantity to add to your portfolio.")
    print(" - Type 'LIST' to re-display available stocks.")
    print(" - Type 'SHOW' to preview your current portfolio.")
    print(" - Type 'DONE' when you are finished adding stocks.")

    while True:
        print("\n" + "-" * 50)
        symbol = input("Enter stock symbol (or 'DONE' to finish): ").strip().upper()

        if symbol == "DONE":
            break
        elif symbol == "LIST":
            display_market_prices(STOCK_PRICES)
            continue
        elif symbol == "SHOW":
            display_portfolio_summary(portfolio, STOCK_PRICES)
            continue
        elif symbol == "":
            print(" [!] Symbol cannot be blank.")
            continue
        elif symbol not in STOCK_PRICES:
            print(f" [!] '{symbol}' is not in the price list.")
            print(f"     Available tickers: {', '.join(sorted(STOCK_PRICES.keys()))}")
            continue

        # Get valid quantity
        quantity = get_valid_quantity()

        # Update portfolio
        if symbol in portfolio:
            portfolio[symbol] += quantity
            print(f" [+] Added {quantity} more share(s) of {symbol}. Total {symbol}: {portfolio[symbol]}")
        else:
            portfolio[symbol] = quantity
            print(f" [+] Added {quantity} share(s) of {symbol} to portfolio.")

    # Final summary display
    print("\n" + "#" * 60)
    print("#                 FINAL PORTFOLIO RESULTS                  #")
    print("#" * 60)
    total = display_portfolio_summary(portfolio, STOCK_PRICES)

    if not portfolio or total == 0:
        print("\nNo stocks were added. Thank you for using Stock Portfolio Tracker!")
        return

    # Optional file export
    print("\nSave Options:")
    print(" [1] Save as Text file (.txt)")
    print(" [2] Save as CSV spreadsheet (.csv)")
    print(" [3] Save as Both (.txt and .csv)")
    print(" [4] Do not save (Exit)")

    while True:
        choice = input("\nEnter your choice (1/2/3/4): ").strip()
        if choice == "1":
            saved_file = save_portfolio_to_txt(portfolio, STOCK_PRICES)
            print(f" [OK] Portfolio successfully saved to: {saved_file}")
            break
        elif choice == "2":
            saved_file = save_portfolio_to_csv(portfolio, STOCK_PRICES)
            print(f" [OK] Portfolio successfully saved to: {saved_file}")
            break
        elif choice == "3":
            txt_file = save_portfolio_to_txt(portfolio, STOCK_PRICES)
            csv_file = save_portfolio_to_csv(portfolio, STOCK_PRICES)
            print(f" [OK] Portfolio successfully saved to:")
            print(f"     - Text Report: {txt_file}")
            print(f"     - CSV File:    {csv_file}")
            break
        elif choice in ("4", "n", "N", "exit", "quit"):
            print(" [i] Summary not saved to disk.")
            break
        else:
            print(" [!] Invalid option. Please select 1, 2, 3, or 4.")

    print("\nThank you for using Stock Portfolio Tracker! Happy investing!")


if __name__ == "__main__":
    main()
