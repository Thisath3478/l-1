


import calendar
year=2025
month=1
print(calendar.month(year,month))
print(calendar(2025))


def hotel_cost(nights):
    return 140*nights
def plane_ride_cost(city):
    if "Colombo" == city:
        return 183
    elif "Galle" == city:
        return 295
    elif "Kandy" == city:
        return 300
    elif "Tokyo" == city:
        return 2472
def rental_car_cost(days):
    if days>=7:
        return 40*days - 50
    elif days>=3:
        return 40*days - 20
    else:
        return 40*days
def trip_cods (city,day,spending_cost):
    return rental_car_cost(day)+hotel_cost(days)+plane_ride_cost(city)+spending_money
print("Cost of car rental: ",rental_car_cost(6))
print("Cost of plane ride: ",plane_ride_cost("Tokyo"))
print("Cost of hotel room: ", hotel_cost(7))
print("Total cost of the trip:",trip_cost("Tokyo",7,500))