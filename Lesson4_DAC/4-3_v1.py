import RPi.GPIO as gp


pwm_out = 27

gp.setmode(gp.BCM)
gp.setup(pwm_out, gp.OUT)
pwm = gp.PWM(pwm_out, 1000)




def convert_10_to_2(x):
    return bin(x)[2:].zfill(8)


try:
    pwm.start(0)
    while True:
        n = input()

        if n == 'e':
            print("Goodbye!")
            break

        if not(n.isdigit()):
            print("Not a number: Enter a number from 0 to 100")
            continue
        
        try:
            n = int(n)
        except ValueError():
            print("IntegerError: Enter an integer")
            continue

        if n < 0:
            print("RangeError: Enter a positive integer from 0 to 100")
            continue

        if n > 100:
            print("RangeError: Enter an integer from 0 to 100")
            continue

        pwm.ChangeDutyCycle(n)
        print("Expected voltage: ", n / 100 * 3.3, "V")
    pwm.stop()

except Exception as e:
    print("Error: ", e)

finally:
    gp.output(pwm_out, 0)
    gp.cleanup()