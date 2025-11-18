import random
#Ex 1
def rainfall_data(days):
    rain_list = []
    
    for _ in range(days):
        rain_list.append(random.randint(0,80))
        
    return rain_list

#Ex 2
def rainfall_ana(rain_list):
    dry_day = 0
    aver_day = 0
    heavy_day = 0
    
    for i in rain_list:
        if i <= 20:
            dry_day += 1
        elif i >= 65:
            heavy_day += 1
        else:
            aver_day += 1
            
    return dry_day, aver_day, heavy_day

# dry, aver, heavy = rainfall_ana([23,41,63,34,64])
# print(f"{dry} dry day, {aver} average day, {heavy} heavy day")

#Ex 3
# dry, aver, heavy = rainfall_ana(rainfall_data(7))
# print(f"{dry} dry day, {aver} average day, {heavy} heavy day")

#Ex 4
def silage_data(days):
    daily_harvested = []
    moisture = []
    
    for _ in range(days):
        daily_harvested.append(random.randint(1000, 25000))
        moisture.append(random.randint(0, 100))
        
    return  daily_harvested, moisture

#Ex 5
def silage_ana (daily_harvested, moist):
    low_pro = 0
    aver_pro = 0
    high_pro = 0
    wet = 0
    dry = 0
    
    for i in daily_harvested:
        if i <= 5000:
            low_pro += 1
        elif i >= 15000:
            high_pro += 1
        else:
            aver_pro += 1
    for i in moist:
        if i >= 70:
            wet += 1
        elif i <= 50:
            dry += 1
            
    return low_pro, aver_pro, high_pro, wet, dry

# daily_harv, moist = silage_data(7)
# low, aver, high, wet, dry = silage_ana(daily_harv, moist)
# print(f"{low} low prod day, {aver} aver prod day, {high} high prod day, {wet} wet day, {dry} dry day")

#Ex 6
def silage_dm_ana(daily_harvested, moist):
    dm_list = []
    loop_counter = 0
    
    for kg in daily_harvested:
        dm_cal = kg*(1 - moist[loop_counter]/100)
        dm_list.append(dm_cal)
        loop_counter += 1
        
    dm_aver = sum(dm_list)/len(dm_list)
    
    return dm_list, dm_aver

# dm_content, average_dm = silage_dm_ana([1,2,3], [10,50,50])
# print(dm_content)
# print(average_dm)

#Ex 7
def tractor_data(num_tractor):
    hour_list = []
    fuel_consum = []
    
    for _ in range(num_tractor):
        hour_list.append(random.randint(1, 8))
        fuel_consum.append(random.randint(10,100))
        
    return hour_list, fuel_consum

#Ex 8
def tractor_ana (hour_list, fuel_cons):
    tractor_maint_list = []
    fuel_cons_rate = []
    loop_index = 0
    
    for i in hour_list:
        cons_rate = fuel_cons[loop_index]/i
        fuel_cons_rate.append(cons_rate)
        
        if cons_rate >= 16:
            tractor_maint_list.append(loop_index)
            
        loop_index += 1
        
    return fuel_cons_rate, tractor_maint_list

# hours_list_user, fuel_user = tractor_data(7)
# fuel_rate, tractor_need_maint = tractor_ana(hours_list_user, fuel_user)
# print(fuel_rate)
# print(tractor_need_maint)


                           
        
    