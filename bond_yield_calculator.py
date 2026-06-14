import numpy as np
from scipy.optimize import brentq

def bond_price(face_value, coupon_rate, ytm, years, freq=2):
    """Calculate theoretical bond price given a YTM"""
    coupon = face_value * coupon_rate / freq
    periods = int(years * freq)
    rate = ytm / freq
    
    pv_coupons = sum([coupon / (1 + rate)**t for t in range(1, periods + 1)])
    pv_face = face_value / (1 + rate)**periods
    
    return pv_coupons + pv_face

def calculate_ytm(face_value, coupon_rate, market_price, years, freq=2):
    """Solve for YTM given market price"""
    def f(ytm):
        return bond_price(face_value, coupon_rate, ytm, years, freq) - market_price
    return brentq(f, 0.0001, 1)

def macaulay_duration(face_value, coupon_rate, ytm, years, freq=2):
    """Calculate Macaulay Duration in years"""
    coupon = face_value * coupon_rate / freq
    periods = int(years * freq)
    rate = ytm / freq
    
    price = bond_price(face_value, coupon_rate, ytm, years, freq)
    
    weighted_times = 0
    for t in range(1, periods + 1):
        cf = coupon if t < periods else coupon + face_value
        pv = cf / (1 + rate)**t
        weighted_times += (t / freq) * pv
    
    return weighted_times / price


# Example usage
if __name__ == "__main__":
    face_value = 100000
    coupon_rate = 0.092
    market_price = 98500
    years = 5

    ytm = calculate_ytm(face_value, coupon_rate, market_price, years)
    duration = macaulay_duration(face_value, coupon_rate, ytm, years)

    print(f"Bond Details:")
    print(f"Face Value: ₹{face_value:,}")
    print(f"Coupon Rate: {coupon_rate*100:.2f}%")
    print(f"Market Price: ₹{market_price:,}")
    print(f"Years to Maturity: {years}")
    print(f"\nYield to Maturity (YTM): {ytm*100:.2f}%")
    print(f"Macaulay Duration: {duration:.2f} years")
