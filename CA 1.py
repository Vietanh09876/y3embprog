import random
#Question 1
def irrigation_pump_data_gen(no_pump = 10):
    pump_hours = []
    volume_pumped =[]
    
    for _ in range(no_pump):
        pump_hours.append(random.randint(1, 24))
        volume_pumped.append(random.randint(20,150))
        
    return pump_hours, volume_pumped

#Question 2
def irrigation_pump_flowrate(pump_usage, volume_pumped):
    flow_rate = []
    
    for i in range(len(pump_usage)):
        flow_rate.append(round(volume_pumped[i]/pump_usage[i], 3))
        
    return flow_rate

#Question 3
def pump_effi_flagging(flowrate):
    effi_list = []
    maint_list = []
    
    for i in range(len(flowrate)):
        effi_cal = round((flowrate[i]/20)*100, 3)
        if effi_cal < 50:
            effi_list.append(effi_cal)
            maint_list.append(i)
    
    return effi_list, maint_list

#Question 4
hours_pumping_list, vol_pumped_list = irrigation_pump_data_gen(5)
print(f"Hours of pumping: {hours_pumping_list}")
print(f"Volume pumped: {vol_pumped_list}")

calced_flowrate_list = irrigation_pump_flowrate(hours_pumping_list, vol_pumped_list)
print(f"Pumps flowrate: {calced_flowrate_list}")

efficiency_list, maintenance_list = pump_effi_flagging(calced_flowrate_list)
print(f"Pumps that need maintenance: {maintenance_list}")
print(f"Pumps with efficiency below 50%: {efficiency_list}")
