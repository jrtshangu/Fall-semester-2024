from datetime import datetime as dt

def print_time():
    print("Task completed")
    print(dt.now())
    print()

print_time()

def display_numbers(x, y):
    return 10

x = 3
y = 4
x = display_numbers(x, y)

print(x)