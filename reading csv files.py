##import csv
###----------------------------------------------------------------------
##def csvreading():
##      with open('LTBI_estimates_2018-05-19.csv') as csvfile:
##            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
##            for row in spamreader:
##                  print(', '.join(row))
##
##
##csvreading()



def filered():
      filename = 'LTBI_estimates_2018-05-19.csv'
      file = open(filename, mode='r')
      #text = print(file.read())
      data = file.read_csv(filename)
      print(data.head())
      file.close()

filered()
