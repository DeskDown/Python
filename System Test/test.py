try:
    5/0
except ZeroDivisionError as e:
    raise ValueError("cannot divide by 0") from None