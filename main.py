# main.py
from modules.formulaai.helpers import (
    PyBattery, PyDevice, PyNetwork, PyStorage,
    PyLocale, PyDisplay, PyApp, PyClipboard
)


print("=== Battery Info ===")
battery = PyBattery()
print("Battery level:", battery.get_level())
print("Is charging:", battery.is_charging())

print("\n=== Device Info ===")
device = PyDevice()
print("Model:", device.get_model())
print("Android version:", device.get_android_version())
print("Manufacturer:", device.get_manufacturer())

print("\n=== Network Info ===")
network = PyNetwork()
print("Is online:", network.is_online())

print("\n=== Storage Info ===")
storage = PyStorage()
print("Free space (bytes):", storage.free_space())
print("Total space (bytes):", storage.total_space())
print("External mounted:", storage.is_external_mounted())

print("\n=== Locale Info ===")
locale = PyLocale()
print("Language:", locale.get_language())
print("Country:", locale.get_country())

print("\n=== Display Info ===")
display = PyDisplay()
resolution = display.get_resolution()
print(f"Resolution: {resolution[0]}x{resolution[1]}")
print("Density DPI:", display.get_density())

print("\n=== App Info ===")
app = PyApp()
print("Package:", app.get_package())
print("Version name:", app.get_version_name())
print("Version code:", app.get_version_code())

print("\n=== Clipboard Test ===")
clipboard = PyClipboard()
clipboard.set_text("Hello from Python!")
print("Clipboard text:", clipboard.get_text())

