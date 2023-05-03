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

def adc():
    for i in range(256):
        curr_bin_val = convert_10_to_2(i)
        comp_val = gp.input(comp)

        gp.output(dac, curr_bin_val)
        time.sleep(0.0001)

        if not(comp_val):
            return i
    
    return 255

def new_adc():
    v_dec = 0
    for i in range (0, 8):
        mass = 7 - i
        gp.output(dac[i], 1)
        time.sleep(0.01)
        
        compValue = gp.input(comp)
        if compValue == 0:
            gp.output(dac[i], 0)
        else:
            v_dec = v_dec + 2**mass
    return v_dec

try:
    gp.output(troyka, 1)

    with open("result.txt", "w") as resfile:
        for i in range(1000):
            resfile.write(str(adc()))

finally:
    gp.output(dac, 0)
    gp.output(troyka, 0)
    gp.cleanup()