

class norm:
    def normAngle(self, x):
        file = open("angles.txt", "w")
        file.truncate(0)
        file.close()
        file = open("__angles.txt", "r")
        aa = []
        for i in range(0, x):
            aa.append(int(file.readline()) / 60)
        file.close()
        file = open("angles.txt", "a")
        for i in range(0, x):
            a = aa.pop(0)
            file.write(str(a))
            file.write('\n')
        file.close()

    def normTime(self, x):
        file = open("times.txt", "w")
        file.truncate(0)
        file.close()
        file = open("__times.txt", "r")
        ta = []
        for i in range(0, x):
            ta.append(int(file.readline()) / 5)
        file.close()
        file = open("times.txt", "a")
        for i in range(0, x):
            t = ta.pop(0)
            file.write(str(t))
            file.write('\n')
        file.close()

    def normVelocity(self, x):
        file = open("velocities.txt", "w")
        file.truncate(0)
        file.close()
        file = open("__velocities.txt", "r")
        va = []
        for i in range(0, x):
            va.append(int(file.readline()) / 120)
        file.close()
        file = open("velocities.txt", "a")
        for i in range(0, x):
            v = va.pop(0)
            file.write(str(v))
            file.write('\n')
        file.close()

    def normGravity(self, x):
        file = open("gravities.txt", "w")
        file.truncate(0)
        file.close()
        file = open("__gravities.txt", "r")
        ga = []
        for i in range(0, x):
            ga.append(int(file.readline()) / 25)
        file.close()
        file = open("gravities.txt", "a")
        for i in range(0, x):
            g = ga.pop(0)
            file.write(str(g))
            file.write('\n')
        file.close()

    def normY(self, x):
        file = open("ys.txt", "w")
        file.truncate(0)
        file.close()
        file = open("___y's.txt", "r")
        ya = []
        for i in range(0, x):
            ya.append(float(file.readline()) / 500)
        file.close()
        file = open("ys.txt", "a")
        for i in range(0, x):
            y = ya.pop(0)
            file.write(str(y))
            file.write('\n')
        file.close()


n = norm()
x = 50
n.normTime(x)
n.normAngle(x)
n.normGravity(x)
n.normVelocity(x)
n.normY(x)
