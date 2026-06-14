# Finance Projects

Python projects combining finance concepts with data analysis and automation.

## 📊 Project 1: Live Stock Price Tracker

A Python script that pulls live stock prices for a watchlist of companies using the `yfinance` library, calculates daily percentage change, and visualizes performance with a color-coded bar chart (green = gains, red = losses).

**Companies tracked:** Ubiquiti, Nauticus Robotics, IBM, Lithium Americas, Palantir, Meta, Microsoft, Joby Aviation, Rigetti Computing, AeroVironment, Redwire

**Tech used:** `yfinance`, `pandas`, `matplotlib`

**Skills demonstrated:** API integration, data analysis, financial metrics, data visualization

---

## 💰 Project 2: Bond Yield Calculator (YTM & Duration)

A Python tool that calculates **Yield to Maturity (YTM)** and **Macaulay Duration** for a coupon-paying bond, given its face value, coupon rate, market price, and time to maturity. Uses numerical root-finding to solve for YTM based on actual bond pricing theory.

**Example output:** For a ₹1,00,000 bond with a 9.20% coupon trading at ₹98,500 with 5 years to maturity, the tool calculates a YTM of 9.58% and a Macaulay Duration of 4.11 years — correctly reflecting that bonds trading at a discount have YTM higher than their coupon rate.

**Tech used:** `numpy`, `scipy`

**Skills demonstrated:** Fixed income analytics, numerical methods, financial modeling — built on real concepts applied during a debt capital markets internship.

---

*More projects coming soon — portfolio tracker, stock screener.*
