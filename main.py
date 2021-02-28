
import time
import measure
import lights

def startup():
    time.sleep(0.1)
    lights.ten()
    time.sleep(0.3)
    lights.reset()
    time.sleep(0.2)
    lights.ten()
    time.sleep(0.1)
    lights.reset()
    time.sleep(0.1)
    lights.ten()
    time.sleep(0.1)
    ligths.reset()

startup()

while True:
    measure.checkDistance()
    time.sleep(0.1)
        
