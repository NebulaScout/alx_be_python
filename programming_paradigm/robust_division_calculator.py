def safe_divide(numerator, denominator):
    try:
        result = float(numerator) / float(denominator)
        # result = format(result, '.1f')
        message = "The result of the division is %.1f" % result
    
    except ZeroDivisionError:
        message = "Error: Cannot divide by zero."

    except ValueError:
        message = "Error: Please enter numeric values only."

    return message
