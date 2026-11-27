"""
math_utilities.py - Custom module for mathematical utilities.

This module provides unit conversions and advanced mathematical calculations
that complement Python's built-in math module.

Author: [Your Name]
Date: [Current Date]
"""

import math


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9


def km_to_miles(km):
    """Convert kilometers to miles."""
    return km * 0.621371


def miles_to_km(miles):
    """Convert miles to kilometers."""
    return miles / 0.621371


def kg_to_pounds(kg):
    """Convert kilograms to pounds."""
    return kg * 2.20462


def pounds_to_kg(pounds):
    """Convert pounds to kilograms."""
    return pounds / 2.20462


def compound_interest(principal, rate, time, n=1):
    """
    Calculate compound interest.

    Formula: A = P * (1 + r/n)^(n*t)

    Args:
        principal (float): Initial amount.
        rate (float): Annual interest rate (in percentage).
        time (float): Time in years.
        n (int): Number of times interest is compounded per year.

    Returns:
        tuple: (final_amount, interest_earned)
    """
    r = rate / 100
    amount = principal * math.pow((1 + r / n), n * time)
    interest = amount - principal
    return round(amount, 2), round(interest, 2)


def factorial(n):
    """Calculate factorial using math.factorial."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    return math.factorial(n)


def area_circle(radius):
    """Calculate area of a circle."""
    return round(math.pi * radius ** 2, 2)


def area_rectangle(length, width):
    """Calculate area of a rectangle."""
    return round(length * width, 2)


def area_triangle(base, height):
    """Calculate area of a triangle."""
    return round(0.5 * base * height, 2)


def area_square(side):
    """Calculate area of a square."""
    return round(side ** 2, 2)


# The __name__ == "__main__" paradigm
if __name__ == "__main__":
    print("Testing math_utilities module directly...")
    print(f"100°C = {celsius_to_fahrenheit(100)}°F")
    print(f"10 km = {km_to_miles(10):.2f} miles")
    print(f"Compound Interest: {compound_interest(1000, 5, 2)}")
    print(f"Factorial of 5: {factorial(5)}")
    print(f"Area of circle (r=5): {area_circle(5)}")
