def safe_divide(numerator, denominator):
    try:
        result = float(numerator) / float(denominator)
    except ZeroDivisionError as e:
        print("Error: Cannot divide by zero.")
    except ValueError as e:
        print("Error: Please enter numeric values only.")
    except Exception as e:
        print(e)
    else:
        print(f"The result of the division is {result}")


# safe_divide("fff",10)