import math as m
import random as r

from math import log10, floor

class dataGen:
    def __roundSigFig__(self, x, sig):
        return round(x, sig - int(m.floor(m.log10(abs(x)))) - 1)

    def clearGens(self, x):
        if x == 'all':
            y = True
        else:
            y = False
        if x == 'angles' or y == True:
            file = open("__angles.txt", "w")
            file.truncate(0)
            file.close()
        if x == 'times' or y == True:
            file = open("__times.txt", "w")
            file.truncate(0)
            file.close()
        if x == 'velocities' or y == True:
            file = open("__velocities.txt", "w")
            file.truncate(0)
            file.close()
        if x == 'gravities' or y == True:
            file = open("__gravities.txt", "w")
            file.truncate(0)
            file.close()
        if x == "y's" or y == True:
            file = open("___y's.txt", "w")
            file.truncate(0)
            file.close()
        y = False

    def angleGen(self, x):
        file = open("__angles.txt", "a")
        for i in range(0,x):
            q = 22/7
            p = r.randint(30, 60)
            file.write(str(p))
            file.write('\n')
        file.close()

    def timeGen(self, x):
        file = open("__times.txt", "a")
        for i in range(0,x):
            p = r.randint(1, 5)
            file.write(str(p))
            file.write('\n')
        file.close()

    def velocityGen(self, x):
        file = open("__velocities.txt", "a")
        for i in range(0,x):
            p = r.randint(90, 120)
            file.write(str(p))
            file.write('\n')
        file.close()

    def gravityGen(self, x):
        file = open("__gravities.txt", "a")
        for i in range(0,x):
            p = r.randint(4, 25)
            file.write(str(p))
            file.write('\n')
        file.close()

    def calculateY(self, x):
        file = open("__velocities.txt", "r")
        q = file.readlines()
        vel = [x.replace('\n', '') for x in q]
        file.close()
        # print(vel)

        file = open("__times.txt", "r")
        w = file.readlines()
        time = [x.replace('\n', '') for x in w]
        file.close()
        # print(time)

        file = open("__angles.txt", "r")
        e = file.readlines()
        angle = [x.replace('\n', '') for x in e]
        file.close()
        # print(angle)

        file = open("__gravities.txt", "r")
        u = file.readlines()
        grav = [x.replace('\n', '') for x in u]
        file.close()
        # print(grav)

        file = open("___y's.txt", "a")
        for i in range(0, x):
            # vel to v, time to t, angle to a, grav to g
            v = float(vel.pop(0))
            t = float(time.pop(0))
            a = float(angle.pop(0))*(m.pi/180)
            g = float(grav.pop(0))
            # v*t*sin(a) - .5*g*t^2
            y = ((v * t * m.sin(a)) - (.5 * g * t * t))
            z = len(str(int(y)))
            if z == 1:
                y = self.__roundSigFig__(y, 3)
            elif z == 2:
                y = self.__roundSigFig__(y, 4)
            elif z == 3:
                y = self.__roundSigFig__(y, 5)
            file.write(str(y))
            file.write('\n')
        file.close()


d = dataGen()
# x = int(input('Please input the number of data points to generate here:'))
x = 50
print(str(x) + ' will be generated')
print('Clearing previous data')
d.clearGens('all')
print('Generating angles')
d.angleGen(x)
print('Generating gravities')
d.gravityGen(x)
print('Generating times')
d.timeGen(x)
print('Generating velocities')
d.velocityGen(x)
print("Calculating y's")
d.calculateY(x)
print('Finished')
