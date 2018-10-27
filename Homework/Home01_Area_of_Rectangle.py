__author__ = 'stanislav-kuhtinski'
print("Hi, I will help you to count a rectangular area. /n")
while True:
    units = input("Please enter the units(mm,cm,m): ")
    if str(units) == 'mm' or str(units) == 'cm' or str(units) == 'm':
        break
    else:
        print("%s please use only characters (mm,cm,m)./n" % units)
        continue
while True:
    width = float(input("Please enter the width: "))
    if int(width) > 0:
        break
    else:
        print("%s please use only numbers./n" % width)
        continue
while True:
    length = float(input("Please enter the length: "))
    if int(length) > 0:
        break
    else:
        print("%s please use only numbers./n" % length)
        continue

print(
    "Thank you, you have entered the width: {} and the length: {}. Area of your Rectangle is: {}{}".format(width, length, width * length, units))
