import math
#Ex 1
def calculate_area(length, width):
    area = (length*width)/4047
    return area

#Ex 2
def fertiliser_required(acres, usage):
    return acres*usage

#Ex 3 recheck
def tractor_speed(RPM, wheel_diameter):
    rev_per_hour = RPM*60
    wheel_circum_km = (wheel_diameter*0.0000254)*math.pi #1 inch = 0.0000254
    linear_speed = rev_per_hour*wheel_circum_km
    return linear_speed

#Ex 4
def farm_projections(herd_size):
    area = 1.5*herd_size #1.5 acres per cattle
    cost_feed_per_week = 5*0.46*herd_size*7
    return area, round(cost_feed_per_week,3)

# acres, feed_cost = farm_projections(100) 
# print (f"For a herd size of 100, the required land size is {acres}, and the project feed cost per week is {feed_cost}") 

#Ex 5
def farm_projections_2(herd_size, feed_cost_kg = 0.46):
    area = 1.5*herd_size #1.5 acres per cattle
    cost_feed_per_week = 5*feed_cost_kg*herd_size*7
    return area, round(cost_feed_per_week,3)

#Ex 6
def frondend_loader_check (load):
    if load <= 10:
        return "Low load detected – raise the forks higher or check the load sensor"
    elif load >= 500:
        return "Excessive load – remove weight before proceeding"
    else:
        return "Normal load detected – proceed with caution"

# user_load = float(input("your load in kg: "))
# result_check_load = frondend_loader_check(user_load)
# print(result_check_load)

#Ex 7
def irrigation_projection (rainfall):
    if rainfall <= 20:
        print("Irrigation is required")
    elif rainfall >= 65:
        print("Excessive rainfall – monitor the fields for flooding")
    else:
        print("No irrigation required, the rainfall was sufficient")

# user_rainfall = float(input("Previous day rainfall in mm: "))
# irrigation_projection(user_rainfall)


#Ex 8
def  water_pump_control (moist):
    if moist <= 30:
        print("Pump is on at 100%")
    elif moist >= 70:
        print("Pump is off")
    else:
        print("Pump is on at 50%")

# user_moist = float(input("Your moisture level in %: "))
# water_pump_control(user_moist)

#Ex 9
def irrigation_projection_control (rainfall, moist):
    if moist <=30:
        if rainfall <= 20:
            return("Pump is on at 100%")
        elif rainfall >= 65:
            return("Pump is off")
        else:
            return("Pump is on at 30%")
    else:
        if rainfall <= 20:
            return("Pump is on at 30%")
        elif rainfall >= 65:
            return("Pump is off")
        else:
            return("Pump is off")
        
# current_moist,previous_rainfall = float(input("Your moisture level in %: ")),float(input("Previous day rainfall in mm: "))
# irrigation_result = irrigation_projection_control(previous_rainfall,current_moist)
# print(irrigation_result)
