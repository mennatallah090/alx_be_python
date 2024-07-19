def safe_divide(numerator, denominator):
    try:
        result = float(numerator) / float(denominator)
        print(f"The result of the division is {result}")
    except ZeroDivisionError as e:
        print(e)
    except ValueError as e:
        print("Error: Cannot divide by zero.")
    except Exception as e:
        print(e)

# safe_divide("fff",10)