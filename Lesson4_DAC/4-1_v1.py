import RPi.GPIO as gp
import string

dac = [26,19,13,6,5,11,9,10]

gp.setmode(gp.BCM)
gp.setup(dac, gp.OUT)






def convert_10_to_2(x):
    return bin(x)[2:].zfill(8)


try:
    while True:
        n = input()

        if n == 'q':
            print("Goodbye!")
            break

        if not(n.isdigit()):
            print("Not a number: Enter a number from 0 to 255")
            continue
        
        try:
            n = int(n)
        except ValueError():
            print("IntegerError: Enter an integer")
            continue

        if n < 0:
            print("RangeError: Enter a positive integer from 0 to 255")
            continue

        if n > 255:
            print("RangeError: Enter an integer from 0 to 255")
            continue
        
        print("Expected voltage: ", round(n / 255 * 3.1233, 2), "V")

        b = [int(i) for i in list(convert_10_to_2(int(n)))]
        
        gp.output(dac, b)


except Exception as e:
    print("Error: ", e)

finally:
    gp.output(dac,0)
    gp.cleanup()