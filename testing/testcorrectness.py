#!/usr/bin/python3
import subprocess
import re
import sys

class Outcome:
    a = (0.0, 0.0)
    b = (0.0, 0.0)
    dsq = 0
    
    def distSquared(self, a, b):
        dx = self.a[0] - self.b[0]
        dy = self.a[1] - self.b[1]
        return dx * dx + dy * dy

    def __init__(self, x, y, distance=0):
        self.a = x
        self.b = y
        if distance != 0:
            self.dsq = distance
        else:
            self.dsq = self.distSquared(self.a, self.b)

def findoutcome(searchstring):
    dsq = int(re.findall(" [0-9]+\n", searchstring)[0].strip(" ").strip("\n"))
    points = re.findall("[0-9]+,[0-9]+", searchstring)
    a = (int(re.findall("[0-9]+,", points[0])[0].strip(",")), int(re.findall(",[0-9]+", points[0])[0].strip(",")))
    b = (int(re.findall("[0-9]+,", points[1])[0].strip(",")), int(re.findall(",[0-9]+", points[1])[0].strip(",")))
    return Outcome(a, b, dsq)

def equaloutcomes(a, b):
    if a.dsq == b.dsq:
        if (a.a == b.a and a.b == b.b) or (a.a == b.b and a.b == b.a):
            return True

    return False

def main():
    for i in [x * 1000 for x in [2**y for y in range(0, 10)]]:
        for j in range(1, 100):
            bruteoutput = subprocess.check_output(["./driver", "0", str(i), str(j)], universal_newlines=True)
            bruteoutcome = findoutcome(bruteoutput)
            efficientoutput = subprocess.check_output(["./driver", "1", str(i), str(j)], universal_newlines=True)
            efficientoutcome = findoutcome(efficientoutput)
            if not equaloutcomes(bruteoutcome, efficientoutcome):
                print("\n")
                print("Incorrect output: ")
                print("Seed: {}".format(i))
                print("Brute: ")
                print("Distance squared: {}".format(bruteoutcome.dsq))
                print("Point A: {}\t\tPoint B: {}".format(bruteoutcome.a, bruteoutcome.b))
                print("Efficient: ")
                print("Distance squared: {}".format(efficientoutcome.dsq))
                print("Point A: {}\t\tPoint B: {}".format(efficientoutcome.a, efficientoutcome.b))
                print("\n")
                sys.stdout.flush()

main()
