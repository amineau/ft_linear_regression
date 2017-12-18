#!/usr/bin/python

import sys
import csv
import os.path
import argparse
from error import *
from pylab import *
import subprocess as cmd


class Main:

    def __init__(self):
        self.checkArgs()
        self.initTheta()
        self.getData()
        self.show()
        self.run()
        print(self.estimatePrice(50000))
        print(self.theta0)
        ioff()
        show()

    def show(self):
        x = list()
        y = list()
        ion()
        show()
        for data in self.data:
            x.append(int(data['km']))
            y.append(int(data['price']))
        plot(x, y, "x")
        draw()
        pause(0.001)
        

    def run(self):
        for i in range(5):
            theta0, theta1 = self.calculTheta()
            self.theta0 = theta0    
            self.theta1 = theta1    

    def checkArgs(self):
        parser = argparse.ArgumentParser(description="Calcul the linear regression")
        parser.add_argument("-v", "--verbose", action="store_true")
        parser.add_argument("-p", "--path", type=str, help="path of the theta's file")
        parser.add_argument("-n", "--name", type=str, help="name of the theta's file")
        parser.add_argument("file", type=str, help="file containts the csv's data")
        args = parser.parse_args()
        self.pathThetasFile = args.path
        self.nameThetasFile = args.name if args.name else "thetas.csv"
        self.csvFile = args.file


    def initTheta(self):
        self.theta0 = 0
        self.theta1 = 0

    def getData(self):
        if os.path.isfile(self.csvFile):
            with open(self.csvFile) as csvfile:
                reader = csv.DictReader(csvfile)
                self.data = list()
                for dct in reader:
                    self.data.append(dct)
    
    def cmdOutput(self, com):
        pipe = cmd.Popen(com, stdout=cmd.PIPE, stderr=cmd.PIPE)
        output, errput = pipe.communicate()
        return output , errput

    def estimatePrice(self, mileage):
        com = "python estimate_price %s %s %s"%(self.theta0, self.theta1, mileage)
        output = self.cmdOutput(com.split())
        if output[1]:
            Error("Error during the estimate price command : \n%s\n%s"%(com, output[1]))
        return int(output[0])

    def calculTheta(self):
        sum_theta_0 = 0
        sum_theta_1 = 0
        for data in self.data:
            sum_theta_0 += self.estimatePrice(data['km']) - int(data['price'])
            sum_theta_1 += (self.estimatePrice(data['km']) - int(data['price'])) * int(data['km'])
        return sum_theta_0 / len(self.data), sum_theta_1 / len(self.data)

Main()