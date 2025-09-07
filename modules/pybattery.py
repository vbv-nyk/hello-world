from com.priveasy.formulaai.builtin import BatteryHelper as KBatteryHelper

class PyBattery:
    def __init__(self):
        # Access the singleton instance
        self._kt = KBatteryHelper.INSTANCE

    def get_battery_level(self):
        return self._kt.getBatteryLevel()

    def is_charging(self):
        return self._kt.isCharging()
