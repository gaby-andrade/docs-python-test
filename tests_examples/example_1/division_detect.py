def division_detect(numerator: int, denominator: int) -> bool:
    try:
        numerator / denominator
    except ZeroDivisionError:
        return False
    else:
        return True
