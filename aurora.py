'''
Name: Aurora Tracker
Update Date: December 4, 2015

'''

from lxml import html
import requests
import time

localtime   = time.localtime()
timeString  = time.strftime("%Y/%m/%d : %H:%M:%S", localtime)

# Get information  Date and time
page = requests.get('http://www.aurora-service.eu/aurora-forecast/')
tree = html.fromstring(page.content)

# Get information for 3 days aurora level
timeLevel = tree.xpath('//*[@id="left-col"]/div[1]/div[2]/p[4]')
auroraLevel = tree.xpath('//*[@id="left-col"]/div[1]/div[2]/pre/p/strong')

for element in timeLevel:
    print '\n'
    print element.text_content()
    print '\n'


print "\t\tEurope Aurora Level"
for element in auroraLevel:
    print element.text_content()

print "Your time: ", timeString

