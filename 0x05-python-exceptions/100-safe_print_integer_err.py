#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError as message:
        print("Exception: ", end="")
        print(message)
        return False
    except TypeError as text:
        print("Exception: ", end="")
        print(text)
        return False
