import pyb

TRIG_PIN = 'X2'
ECHO_PIN = 'X1'
SOUND_SPEED = 343.0  # m/s

trig = pyb.Pin(TRIG_PIN, pyb.Pin.OUT_PP)
echo = pyb.Pin(ECHO_PIN, pyb.Pin.IN)

def measure_distance():
    trig.low()
    pyb.udelay(2)
    trig.high()
    pyb.udelay(10)
    trig.low()

    while echo.value() == 0:
        pass
    start = pyb.micros()

    while echo.value() == 1:
        pass
    end = pyb.micros()

    duration = end - start
    distance_cm = (duration * SOUND_SPEED) / (2 * 10000.0)
    return distance_cm

def proximity_loop(threshold_cm=20):
    while True:
        dist = measure_distance()
        if dist < threshold_cm:
            print("NEAR")
        else:
            print("FAR")
        pyb.delay(300)
