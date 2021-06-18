
import math
from datetime import date
current_date = date.today()

w = float(input("Enter the width of the tire in mm (ex 205): "))
a = float(input("Enter the aspect ratio of the tire (ex 60): "))
d = float(input("Enter the diameter of the wheel in inches (ex 15): "))

volume = math.pi * w ** 2 * a * (w * a + 2540 * d) /10000000
volume = round(volume, 1)

with open("volumes.txt", "at")as volume_file:
    print(f"{current_date},{w},{a},{d},{volume}", file = volume_file)

