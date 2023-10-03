import time


# Normal function used by Taipy
def double(nb):
    return nb * 2

def add(nb):
    print("Wait 5 seconds in add function")
    time.sleep(5)
    return nb + 10