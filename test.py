import win32api

def printInfo(device):
    print((device.DeviceName, device.DeviceString))
    settings = win32api.EnumDisplaySettings(device.DeviceName, -1)
    for varName in ['Color', 'BitsPerPel', 'DisplayFrequency']:
        print("%s: %s"%(varName, getattr(settings, varName)))

device = win32api.EnumDisplayDevices()
printInfo(device)