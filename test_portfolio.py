"""
Automated Unit Tests for Stock Portfolio Tracker
"""

import os
import unittest
from portfolio_tracker import (
    STOCK_PRICES,
    calculate_portfolio_totals,
    save_portfolio_to_txt,
    save_portfolio_to_csv,
)


class TestStockPortfolioTracker(unittest.TestCase):
    def setUp(self):
        self.sample_prices = {
            "AAPL": 180.00,
            "TSLA": 250.00,
            "MSFT": 400.00,
        }
        self.sample_portfolio = {
            "AAPL": 10,  # 10 * 180 = 1800
            "TSLA": 2,   # 2 * 250 = 500
            "MSFT": 5,   # 5 * 400 = 2000
        }
        self.test_txt = "test_portfolio.txt"
        self.test_csv = "test_portfolio.csv"

    def tearDown(self):
        for path in (self.test_txt, self.test_csv):
            if os.path.exists(path):
                os.remove(path)

    def test_calculate_portfolio_totals(self):
        breakdown, total = calculate_portfolio_totals(self.sample_portfolio, self.sample_prices)

        # Expected: 1800 + 500 + 2000 = 4300
        self.assertEqual(total, 4300.00)

        # AAPL tests
        self.assertEqual(breakdown["AAPL"]["shares"], 10)
        self.assertEqual(breakdown["AAPL"]["unit_price"], 180.00)
        self.assertEqual(breakdown["AAPL"]["total_value"], 1800.00)
        self.assertAlmostEqual(breakdown["AAPL"]["weight"], (1800 / 4300) * 100, places=2)

        # TSLA tests
        self.assertEqual(breakdown["TSLA"]["shares"], 2)
        self.assertEqual(breakdown["TSLA"]["unit_price"], 250.00)
        self.assertEqual(breakdown["TSLA"]["total_value"], 500.00)

        # MSFT tests
        self.assertEqual(breakdown["MSFT"]["shares"], 5)
        self.assertEqual(breakdown["MSFT"]["unit_price"], 400.00)
        self.assertEqual(breakdown["MSFT"]["total_value"], 2000.00)

    def test_fractional_shares(self):
        fractional_portfolio = {"AAPL": 2.5}
        breakdown, total = calculate_portfolio_totals(fractional_portfolio, self.sample_prices)
        # 2.5 * 180 = 450
        self.assertEqual(total, 450.00)
        self.assertEqual(breakdown["AAPL"]["total_value"], 450.00)
        self.assertEqual(breakdown["AAPL"]["weight"], 100.00)

    def test_save_to_txt(self):
        saved = save_portfolio_to_txt(self.sample_portfolio, self.sample_prices, self.test_txt)
        self.assertTrue(os.path.exists(saved))
        with open(saved, "r", encoding="utf-8") as f:
            content = f.read()
            self.assertIn("STOCK PORTFOLIO SUMMARY", content)
            self.assertIn("AAPL", content)
            self.assertIn("$4,300.00", content)

    def test_save_to_csv(self):
        saved = save_portfolio_to_csv(self.sample_portfolio, self.sample_prices, self.test_csv)
        self.assertTrue(os.path.exists(saved))
        with open(saved, "r", encoding="utf-8") as f:
            lines = f.readlines()
            self.assertTrue(len(lines) >= 4)
            self.assertIn("Stock Symbol", lines[0])
            self.assertIn("TOTAL INVESTMENT VALUE", "".join(lines))
            self.assertIn("4300.00", "".join(lines))


if __name__ == "__main__":
    unittest.main()
