from com.priveasy.formulaai.builtin import BatteryHelper as KBatteryHelper

class PyBattery:
    def get_battery_level(self):
        return KBatteryHelper.getBatteryLevel()

    def is_charging(self):
        return KBatteryHelper.isCharging()
