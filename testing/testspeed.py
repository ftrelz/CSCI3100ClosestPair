#!/usr/bin/python3
import subprocess
import sys
import re

def findtime(searchstring):
    return float(re.findall("[0-9]+.*[0-9]* ms", searchstring)[0].strip(" ms"))

def main():
    print("Datapoints:\t\tBrute Avg Time:\t\tEfficient Avg Time\n")
    brutesum = 0
    efficientsum = 0
    for i in [x * 1000 for x in [2**y for y in range(0, 10)]]:
        for j in range(100):   
            #bruteoutput = subprocess.check_output(["./driver", "0", str(i), str(j)], universal_newlines=True)
            #brutesum += findtime(bruteoutput)
            efficientoutput = subprocess.check_output(["./driver", "1", str(i), str(j)], universal_newlines=True)
            efficientsum += findtime(efficientoutput)
        
        print("{}\t\t\t{}\t\t\t{}\n".format(i, round(brutesum / 100, 4), round(efficientsum / 100, 4)))
        sys.stdout.flush()

main()

