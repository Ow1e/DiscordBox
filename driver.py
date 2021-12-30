# For adafruit driver/software https://github.com/adafruit/Python-Thermal-Printer
import properties

if not properties.emulate:
    import serial, adafruit_thermal_printer
    uart = serial.Serial("/dev/serial0", baudrate=19200, timeout=3000)
    ThermalPrinter = adafruit_thermal_printer.get_printer_class(properties.version)
    printer = ThermalPrinter(uart)
    printer.feed(2)
    printer.print("Initializing support... ")
    def send(msg):
        print(msg)
        printer.print(msg)
    printer.print("Done!")
else:
    def send(msg):
        print(msg)