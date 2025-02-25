#!/usr/bin/env python3

def give_bmi(
        height: list[int | float],
        weight: list[int | float]
        ) -> list[int | float]:
    """
    Calculate the BMI for each height and weight pair.

    Parameters:
    height (list[int | float]): List of heights.
    weight (list[int | float]): List of weights.

    Returns:
    list[int | float]: List of calculated BMI values.
    """
    if len(height) != len(weight):
        raise ValueError("Height and weight lists must be of the same length.")
    bmi_values = []
    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            raise TypeError("Height and weight must be int or float.")
        if h <= 0:
            raise ValueError("Height must be greater than zero.")
        bmi = w / (h ** 2)
        bmi_values.append(bmi)
    return bmi_values


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Apply a limit to BMI values.

    Parameters:
    bmi (list[int | float]): List of BMI values.
    limit (int): Limit to compare against.

    Returns:
    list[bool]: List of booleans indicating if BMI is above the limit.
    """
    if not all(isinstance(value, (int, float)) for value in bmi):
        raise TypeError("All BMI values must be int or float.")
    if not isinstance(limit, (int, float)):
        raise TypeError("Limit must be an int or float.")
    result = [value > limit for value in bmi]
    return result
