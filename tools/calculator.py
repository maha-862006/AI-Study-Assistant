import re

def calculate(expression):
    try:
        allowed = re.match(r'^[0-9+\-*/(). ]+$', expression)

        if not allowed:
            return "Error: Invalid characters in expression"

        result = eval(expression)
        return result

    except ZeroDivisionError:
        return "Error: Division by zero"

    except Exception as e:
        return f"Error: {str(e)}"