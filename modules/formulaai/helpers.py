from com.priveasy.formulaai.builtin import BatteryHelper, DeviceHelper, NetworkHelper, \
    StorageHelper, LocaleHelper, DisplayHelper, AppHelper, ClipboardHelper

class PyBattery:
    def get_level(self): return BatteryHelper.getBatteryLevel()
    def is_charging(self): return BatteryHelper.isCharging()

class PyDevice:
    def get_model(self): return DeviceHelper.getDeviceModel()
    def get_android_version(self): return DeviceHelper.getAndroidVersion()
    def get_manufacturer(self): return DeviceHelper.getManufacturer()

class PyNetwork:
    def is_online(self): return NetworkHelper.isOnline()

class PyStorage:
    def free_space(self): return StorageHelper.getInternalFreeSpace()
    def total_space(self): return StorageHelper.getInternalTotalSpace()
    def is_external_mounted(self): return StorageHelper.isExternalStorageMounted()

class PyLocale:
    def get_language(self): return LocaleHelper.getLanguage()
    def get_country(self): return LocaleHelper.getCountry()

class PyDisplay:
    def get_resolution(self): 
        pair = DisplayHelper.getScreenResolution()
        return (pair.getFirst(), pair.getSecond())

    def get_density(self): return DisplayHelper.getDensityDpi()

class PyApp:
    def get_package(self): return AppHelper.getPackageName()
    def get_version_name(self): return AppHelper.getVersionName()
    def get_version_code(self): return AppHelper.getVersionCode()

class PyClipboard:
    def set_text(self, text): ClipboardHelper.setText(text)
    def get_text(self): return ClipboardHelper.getText()
