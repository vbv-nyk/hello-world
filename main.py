from modules.pybattery import PyBattery
battery = PyBattery()
print("Battery level:", battery.get_battery_level())
print("Charging:", battery.is_charging())
print("Working")
