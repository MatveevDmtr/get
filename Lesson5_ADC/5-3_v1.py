import RPi.GPIO as gp
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
comp = 4
troyka = 17

gp.setmode(gp.BCM)
gp.setup(dac, gp.OUT)
gp.setup(leds, gp.OUT)
gp.setup(troyka, gp.OUT, initial=gp.HIGH)
gp.setup(comp, gp.IN)

def convert_10_to_2(n):
    return [int(elem) for elem in bin(n)[2:].zfill(8)]

def adc():
    for i in range(256):
        curr_bin_val = convert_10_to_2(i)
        comp_val = gp.input(comp)

        gp.output(dac, curr_bin_val)
        time.sleep(0.0001)

        if not(comp_val):
            return i

def adc_binsearch():
    val = 0
    for i in range(7, -1, -1):
        val += 2 ** i
        curr_bin_val = convert_10_to_2(val)
        comp_val = gp.input(comp)

        gp.output(dac, curr_bin_val)
        time.sleep(0.05)

        if not(comp_val):
            val -= 2 ** i
    
    return val

try:
    while True:
        dig_val = adc()
        gp.output(leds, [int(elem) for elem in ('1' * int(dig_val / 221 * 8)).zfill(8)])
        print("Voltage:", round(dig_val / 256 * 3.3, 2))

        gp.output(dac, 0)
finally:
    gp.output(dac, 0)
    gp.output(troyka, 0)
    gp.cleanup()