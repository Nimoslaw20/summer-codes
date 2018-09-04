#Csv learning
import csv

##def Rcsv():
##      with open('LTBI_estimates_2018-05-19.csv') as fin:
##            print(list(csv.reader(fin)))
####            for i in fin:
####                  print((list(csv.reader(fin))), sep = ' ', end ='\n')
##
##Rcsv()



def checkin():
      isonum = 3
      e_hhsize = 6
      with open('LTBI_estimates_2018-05-19.csv', 'r') as fin:
            data = list(csv.reader(fin))
            ison= [row[isonum] for row in data[1:]]
            ehhsize =[row[e_hhsize] for row in data[1:]]
            print("The last  iso_numeric is: ", ison[-1])
            print("The last ehhsize is: ", ehhsize[-1])
            #print(max(ison))
checkin()
