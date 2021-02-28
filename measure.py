import lights
import distance

def checkDistance():
    d = distance.sensor()
    maxDis = 25
    if d < maxDis * 0.1:
        lights.ten()
    elif d < maxDis * 0.2:
        lights.nine()
    elif d < maxDis * 0.3:
        lights.eight()
    elif d < maxDis * 0.4:
        lights.seven()
    elif d < maxDis * 0.5:
        lights.six()
    elif d < maxDis * 0.6:
        lights.five()
    elif d < maxDis * 0.7:
        lights.four()
    elif d < maxDis * 0.8:
        lights.three()
    elif d < maxDis * 0.9:
        lights.two()
    elif d < maxDis * 1:
        lights.one()
    else:
        lights.reset()