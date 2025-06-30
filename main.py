# convert datas from PC_extend_board_network_analyzer to data which has frequency and gain in columns.
# you can easy to analyze data in excel gragh generation.

import os
import math
import csv

def main():
  # get current directory
  path = str(os.getcwd())
  print(path)

  # deal with all files in directory
  for filename in os.listdir(path +"\\experiment-files"):
    datas = [0]
    fileType = filename[-4:]

  # only csv file is dealed
    if(fileType == '.csv'):

    # open file and ignore some lines at first and at last
      with open(path+'\\experiment-files\\'+filename) as f:
        flag = 0
        while(1):
          line = f.readline()
          if(flag == 1):
            if(line.split(',')[0] != 'Numerical of Memory Trace'):
              datas.append(line)
              continue
            else:
              break
          if(line.split(',')[0] == 'Measurement Number' and flag == 0):
            flag = 1

    # make result csv file
      with open(path+'\\results\\'+filename[:-4]+'.csv', 'x', newline = '') as result:
        writer = csv.writer(result)
        writer.writerow(['frequency[MHz]', 'gain[dB]'])

    # calculate and store data
        for data in datas:
          if type(data) != type(1):
            dataSplited = data.split(',')
            frequency = float(dataSplited[1])/1e6
            realPart  = float(dataSplited[5])
            imaginaryPart = float(dataSplited[6])
            gain = (20)*math.log10(math.sqrt((realPart*realPart)+(imaginaryPart*imaginaryPart)))
            writer.writerow([frequency, gain])


if __name__ == "__main__":
  main()