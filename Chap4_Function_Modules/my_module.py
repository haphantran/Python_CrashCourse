import math
def greet(name):
    print("Xin chào,", name)

def calculate_area(width, height):
    return width * height

def int_input(prompt,error_message,min_value=-math.int):
    while True:
        try:
            value = int(input(prompt))
            if value < min_value:
                print(error_message)
            else:
                return value
        except ValueError:
            print(error_message)