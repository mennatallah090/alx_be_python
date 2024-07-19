def safe_divide(numerator, denominator):
    try:
        result = numerator / denominator
        print(f"The result of the division is {result}")
    except ZeroDivisionError as e:
        print(e)
    except ValueError as e:
        print(e)
    except Exception as e:
        print(e)

# safe_divide("fff",10)