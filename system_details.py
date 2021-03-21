import wmi

sys = wmi.WMI()
my_sys = c.Win32_ComputerSystem()[0]
print(f"Manufacturer: {my_sys.Manufacturer}")
print(f"Model: {my_sys.Model}")
print(f"Name: {my_sys.Name}")
print(f"ProcessorNumber: {my_sys.NumberofProcessors}")
print(f"Type: {my_sys.SystemType}")
print(f"Family: {my_sys.SystemFamily}")


