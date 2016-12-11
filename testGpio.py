from gpiozero import OutputDevice
from time import sleep

def createOutputDevice(pin):
    return OutputDevice(pin)


outputPins = [5, 6, 13, 19, 26]
outputDevices = map(createOutputDevice, outputPins)

print "Test setup is running on these pins: " + ", ".join(map(str, outputPins))
print "Ensure you have these pins connected to the relays on the NO (normally open) input"

print "Testing individual pins, enabling them for 2 seconds each"
for device in outputDevices:
    print "Turning on device on pin %s" % device.pin
    device.on()
    sleep(2)
    print "Turning off device on pin %s" % device.pin
    device.off()
    sleep(0.5)
print ""
sleep(1)
print "Testing maximum load for pins. Turning on 1 more pin every 2 seconds"
for device in outputDevices:
    print "Turning on device on pin %s" % device.pin
    device.on()
    sleep(2)

print "Test finalized. Turning all devices off"
for device in outputDevices:
    print "Turning off device on pin %s" % device.pin
    device.off()
print ""
sleep(1)
print "Torture test 1: Enable all pins at once"
for device in outputDevices:
    print "Turning on device on pin %s" % device.pin
    device.on()

print "Test finalized. Turning all devices off"
for device in outputDevices:
    print "Turning off device on pin %s" % device.pin
    device.off()
print ""
sleep(1)
print "Torture test 2: Flickering all pins at once in short intervals (100ms)"
for x in range(10):
    for device in outputDevices:
        print "Turning on device on pin %s" % device.pin
        device.on()
    sleep(0.1)
    for device in outputDevices:
        print "Turning off device on pin %s" % device.pin
        device.off()
    sleep(0.1)
print ""
print "All tests completed"