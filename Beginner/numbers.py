# 1. Write a function that takes two arguments, 145 and 'o',
def format_example(number, character):
    return "Number: {}, Character: {}".format(number, character)
result = format_example(145, 'o')
print("Formatted Output:", result)
print("Representation Used: String format method")

print("\n----------------------------------------\n")
# 2. In a village, there is a circular pond with a radius of 84 meters.
radius = 84
pi = 3.14
pond_area = pi * radius * radius
total_water = pond_area * 1.4
print("Pond Area (without decimals):", int(pond_area))
print("Total Water in Pond (liters, without decimals):", int(total_water))

print("\n----------------------------------------\n")
# 3. If you cross a 490 meter long street in 7 minutes,
distance = 490            # meters
time_minutes = 7
time_seconds = time_minutes * 60

speed = distance / time_seconds

print("Speed (meters/second, without decimals):", int(speed))
