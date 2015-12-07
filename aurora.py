#!/usr/bin/env python3

# Name            :  Aurora Forecast
# Script Name     :  aurora.py
# Created         :  December 5, 2015
# Last Modified   :  December 7, 2015


from datetime import datetime
from lxml import html
import requests
import time
import tkinter
from PIL import ImageTk, Image

localtime   = time.localtime()
timeString  = time.strftime("%Y-%m-%d : %H:%M:%S", localtime)

#******************************************************************************#
#******************************************************************************#
# TODO: MAKE THIS TWO CODES INTO ONE. CHECK TODO LIST
def auroraMapEurope():

        # Create the main window
        window = tkinter.Tk()
        window.title("Aurora Europe")
        window.geometry("900x500")
        window.configure(background='black')

        path = "europeMap.jpg"
        # Create photo image
        img = ImageTk.PhotoImage(Image.open(path))
        panel = tkinter.Label(window, image = img)
        panel.pack(side = "bottom", fill ="both", expand = "yes")

        #Start the GUI
        window.mainloop()

        main()


def auroraMapNAmerica():
        # Create the main window
        window = tkinter.Tk()
        window.title("Aurora Norh America")
        window.geometry("900x500")
        window.configure(background='black')

        path = "nAmericaMap.jpg"
        # Create photo image
        img = ImageTk.PhotoImage(Image.open(path))
        panel = tkinter.Label(window, image = img)
        panel.pack(side = "bottom", fill ="both", expand = "yes")

        #Start the GUI
        window.mainloop()

        main()
#******************************************************************************#
#******************************************************************************#


def EuropeanTime():
        # Get information for Europe (North) Time and Date
        page = requests.get('http://www.aurora-service.eu/aurora-forecast/')
        tree = html.fromstring(page.content)

        # Get information for 3 days aurora level
        timeLevel = tree.xpath('//*[@id="left-col"]/div[1]/div[2]/p[4]')
        auroraLevel = tree.xpath('//*[@id="left-col"]/div[1]/div[2]/pre/p/strong')

        print ("\t\tEuropean Aurora Level")
        printLevel(timeLevel, auroraLevel)

        print("Do you want to display Aurora Level map?: y/n ")
        choice = input(">> ")
        if choice == 'y':
            auroraMapEurope()
        else:
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
        print("Do you want to display Aurora Level map?: y/n ")
        choice = input(">> ")
        if choice == 'y':
            auroraMapNAmerica()
        else:
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


def main():
    print ("**************************************************")
    print ("Choose which region you want to display aurora level: \n")
    print ("\t1. Europe")
    print ("\t2. North America")
    print ("\t0. To quit")

    choice = True

    while choice:
            choice = int(input(" >> "))
            if choice == 1:
                return EuropeanTime()
            elif choice == 2:
                return NAmericanTime()
            elif choice == 0:
                choices = False
            else:
                print ("****************************************")
                print("Please choose,\n 1)Europe,\n 2)North America, \n 3)Quit")


if __name__ == '__main__':
    main()
