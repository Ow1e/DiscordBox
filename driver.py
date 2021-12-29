# For adafruit driver/software https://github.com/adafruit/Python-Thermal-Printer
import properties

if not properties.emulate:
    from Adafruit_Thermal import *

    printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)
    printer.println("==== DiscordBox ====")


    def send(msg):
        printer.println(msg)
        print(msg)
else:
    def send(msg):
        print(msg)