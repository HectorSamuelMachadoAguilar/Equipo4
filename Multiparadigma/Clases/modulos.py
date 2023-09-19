import csv
import random

def split(inputFile,outPutName,lines):
    with open(inputFile,'r') as file:
        header = file.readline().strip()
        outPutFile=None
        linecount=0
        for line in file:
            if linecount % lines ==0:
                if outPutFile is not None:
                    outPutFile.close()
                outPutFile.open(f"{outPutName}_{linecount//lines}.csv",'w')
                outPutFile.write(header+"\n")
            outPutFile.write(line)
            linecount+=1
    if outPutFile is not None:
            outPutFile.close()
