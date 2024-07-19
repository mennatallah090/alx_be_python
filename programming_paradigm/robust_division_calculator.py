def safe_divide(numerator, denominator):
    try:
        result = float(numerator) / float(denominator)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    except ValueError:
        print("Error: Please enter numeric values only.")
        return None
    except Exception as e:
        print(e)
        return None
    else:
        if result is not None:
            print(f"The result of the division is {result}")
        return None
