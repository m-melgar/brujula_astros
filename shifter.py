from time import sleep

import RPi.GPIO as gpio


class Shifter:

    def __init__(self, input_pin,b ,clock_pin, clear_pin, pause = 1):
        """
        :param input_pin: select input pin
        :param clock_pin: select clock pin
        :param clear_pin: select clear pin
        :param pause: select time between clock ticks (0 by default)
        """
        self.pause = pause
        self.input_pin = input_pin
        self.b = b
        self.clock = clock_pin
        self.clearPin = clear_pin
        self.setupBoard()

    def tick(self):
        gpio.output(self.clock, gpio.HIGH)
        #sleep(self.pause)
        gpio.output(self.clock, gpio.LOW)
        #sleep(self.pause)

    def setValue(self, value):
        for i in range(24):
            bitwise = 0x800000 >> i
            bit = bitwise & value
            if bit == 0:
                gpio.output(self.input_pin, gpio.LOW)
            else:
                gpio.output(self.input_pin, gpio.HIGH)
            Shifter.tick(self)

    def clear(self):
        gpio.output(self.clearPin, gpio.LOW)
        Shifter.tick(self)
        gpio.output(self.clearPin, gpio.HIGH)

    def setupBoard(self):
        gpio.setmode(gpio.BOARD)
        gpio.setup(self.input_pin, gpio.OUT)
        gpio.output(self.input_pin, gpio.LOW)

        gpio.setup(self.clock, gpio.OUT)
        gpio.output(self.clock, gpio.LOW)

        gpio.setup(self.clearPin, gpio.OUT)
        gpio.output(self.clearPin, gpio.HIGH)

#        gpio.setup(self.b, gpio.OUT)
#        gpio.output(self.b, gpio.HIGH)
