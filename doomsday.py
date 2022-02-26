weekday_dict = {
    0: "Sunday",
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
}

date = input("Enter a date in MM/DD/YYYY format: ")
month, day, year = [int(i) for i in date.split("/")]

century = year // 100
sub_century = year % 100
leap = sub_century % 4 == 0 and (century % 100 != 0 or century % 400 == 0)

anchor_day = (5 * (century % 4)) % 7 + 2
a = sub_century // 12
b = sub_century % 12
c = b // 4
d = a + b + c
doomsday_weekday = anchor_day + d
doomsday_weekday %= 7

doomsday_dict = {
    1: 3,
    2: 28,
    3: 14,
    4: 4,
    5: 9,
    6: 6,
    7: 11,
    8: 8,
    9: 5,
    10: 10,
    11: 7,
    12: 12,
}

leap_doomsday_dict = doomsday_dict.copy()
leap_doomsday_dict[1] = 4
leap_doomsday_dict[2] = 29

if leap:
    doomsday = leap_doomsday_dict[month]
else:
    doomsday = doomsday_dict[month]

weekday = (day - doomsday) % 7 + doomsday_weekday
print("That day was a " + weekday_dict[weekday])
