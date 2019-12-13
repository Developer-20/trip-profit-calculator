#Build an application that help transport companies analyze potential profit to different destinations
#destination dictionary that contains 7 keys and 7 data in the keys respectively
destination = {
    "lagos": 1300,
    "enugu": 880,
    "maiduguri": 1400,
    "calabar": 940,
    "acrra": 1600,
    "cotonou": 1500,
    "ibadan": 720
}
#input statement to know the number of sits in a bus and to know the destination of the driver
destination_select = input("Enter the destination: \n")
sitting_capacity = int(input("Enter the number of seats in the bus: \n"))

#if statement to check if the user's input in destination_select is in the dictionary "destination"
if destination_select in destination:
    distance = destination[destination_select]
    print(distance)
    #end of the if statement
    #if statement to confirm the value of the distance and use the value to calculate for the fuel_cost, drivers_cost and total_cost
    if distance == distance:        
        fuel_cost = (distance / 30) * 145
        drivers_cost = (distance / 10) * 1000
        total_cost = fuel_cost + drivers_cost
        print(total_cost)
else:
    #while statement to checks if the user's input is not in destination_select
    while destination != destination_select:
        print("We couldn't find your destination")
        #code to redo the input statement if the while statement is found to be true 
        destination_select = input("Enter the destination: \n")
        distance = destination[destination_select]
        print(distance)

#the calculation block        
fuel_cost = (distance / 30) * 145
drivers_cost = (distance / 10) * 1000
total_cost = fuel_cost + drivers_cost

#if statement to check if the value of distance is in the following ranges below
if distance >= 700 and distance <= 1000:
    revenue = sitting_capacity * 9800
    total_profit = revenue - total_cost
    print(f"Your profit is {total_profit}")
            
#elif statement to check if the value of distance is in the following ranges below    
elif distance >= 1001 and distance <= 1200:
    revenue = sitting_capacity * 12000
    total_profit = revenue - total_cost
    print(f"Your profit is {total_profit}") 
            
#elif statement to check if the value of distance is in the range below
elif distance > 1200:
    revenue = sitting_capacity * 15000
    total_profit = revenue - total_cost
    print(f"Your profit is {total_profit}")
            
else:
    print("Out of range")

input()