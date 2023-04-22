#!/bin/python3

months = open("months.txt")

# print(months.read())
# months.seek(0)
# print(months.readline())
# months.seek(0)
# print(months.readlines())

# print(months.mode)
# print(months.readable())

# for x in months:
#     print(x.strip())


months.close()


days = open("days.txt", "a") # write - w | append - a
print(days)
# days.write("\nMonday")
days.write("\nTuesday")
days.close()