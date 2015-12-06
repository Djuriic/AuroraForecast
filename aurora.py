#!/usr/bin/env python3
'''
Name: Aurora Forecast
Update Date: December 6, 2015

'''
from datetime import datetime
from lxml import html
import requests
import time


localtime   = time.localtime()
timeString  = time.strftime("%Y-%m-%d : %H:%M:%S", localtime)


def EuropeanTime():
        # Get information for Europe (North) Time and Date
        page = requests.get('http://www.aurora-service.eu/aurora-forecast/')
        tree = html.fromstring(page.content)

        # Get information for 3 days aurora level
        timeLevel = tree.xpath('//*[@id="left-col"]/div[1]/div[2]/p[4]')
        auroraLevel = tree.xpath('//*[@id="left-col"]/div[1]/div[2]/pre/p/strong')

        print ("\t\tEuropean Aurora Level")
        printLevel(timeLevel, auroraLevel)
        main()

def NAmericanTime():
        # Get information for North American , Time and Date
        page = requests.get('http://www.aurora-service.org/aurora-forecast/')
        tree = html.fromstring(page.content)

        # Get information for 3 days aurora level
        timeLevel = tree.xpath('//*[@id="left-col"]/div[1]/div[2]/p[2]')
        auroraLevel = tree.xpath('//*[@id="left-col"]/div[1]/div[2]/pre')

        print ("\t\tNorth America Aurora Level")
        printLevel(timeLevel, auroraLevel)
        main()

def printLevel(tLevel, aLevel ):
        # Print out Time and Date
        for element in tLevel:
            print ('\n')
            print (element.text_content())
            print ('\n')
        # Print out the 3 days level
        for element in aLevel:
            print (element.text_content())
            print ("Your time is :", timeString)
            print ("UT time is : ", datetime.utcnow().strftime("%Y-%m-%d : %H:%M:%S",))
            return


def main():
    print ("**************************************************")
    print ("Choose which region you are in: \n")
    print ("\t1. Europe")
    print ("\t2. North America")
    print ("\t0. To quit")

    choices = True

    while choices:
        try:
            choice = int(input(" >> "))
            if choice == 1:
                return EuropeanTime()
            elif choice == 2:
                return NAmericanTime()
            elif choice == 0:
                choices = False
            else:
                print("Please choose,\n 1)Europe,\n 2)North America, \n 3)Quit")
        except ValueError:
            print("input is not a integer, Try again")


if __name__ == '__main__':
    main()
