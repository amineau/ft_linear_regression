#!/usr/bin/python

import sys
import csv
from error import *
import os.path
import argparse


class Main:

    def __init__(self):
      self.checkArgs()
      self.run()

    def checkArgs(self):
        parser = argparse.ArgumentParser(description="Calcul the estimate price")
        parser.add_argument("-v", "--verbose", action="store_true")
        parser.add_argument("theta0", type=float, help="theta 0")
        parser.add_argument("theta1", type=float, help="theta 1")
        parser.add_argument("mileage", type=int, help="mileage to estimate")
        self.args = parser.parse_args()
        
    
    def run(self):
        result = self.args.theta0 + self.args.theta1 * self.args.mileage
        if self.args.verbose:
            print("The estimate price is %s"%(result))
        else:
            print(int(result))

Main()