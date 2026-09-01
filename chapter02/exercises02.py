print("Enter C or F to indicate Celsius or Fahrenheit:...")
scale = input()

print("Enter the temperature:...")
degrees = int(input())


if scale == "C" and degrees >=16 and degrees <=38 or scale == "F" and degrees >= 60 and degrees <= 120:
    print("Is safe temp")
else:
    print("dangerous")
