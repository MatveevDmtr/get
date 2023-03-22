import RPi.GPIO as gp
import time

dac = [26,19,13,6,5,11,9,10]

gp.setmode(gp.BCM)
gp.setup(dac, gp.OUT)






def convert_10_to_2(x):
    return bin(x)[2:].zfill(8)


try:
    while True:
        for n in range(256):
        
            print("Expected voltage: ", round(n / 255 * 3.1233, 2), "V")

            b = [int(i) for i in list(convert_10_to_2(int(n)))]
        
            gp.output(dac, b)

            time.sleep(0.01)
        
        for n in range(255, -1, -1):
        
            print("Expected voltage: ", round(n / 255 * 3.1233, 2), "V")

            b = [int(i) for i in list(convert_10_to_2(int(n)))]
        
            gp.output(dac, b)

            time.sleep(0.01)


except Exception as e:
    print("Error: ", e)

finally:
    gp.output(dac,0)
    gp.cleanup()