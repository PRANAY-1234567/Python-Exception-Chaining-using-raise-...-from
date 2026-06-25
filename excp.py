def test():
    try:
        raise AttributeError("Underlying exception")
    except AttributeError as cause:
        raise ValueError("Main Exception") from cause

try:
    test()

except ValueError as ex:
    print("Main Exception :", ex)
    print("Underlying exception :", ex.__cause__)
