import time


def slow():
    time.sleep(1)


def fast():
    time.sleep(0.2)
    print("Fast function executed")


for i in range(3):
    slow()
    fast()