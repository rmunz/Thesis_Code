#!/usr/bin/python
import os, sys, getopt, re

def main(argv):
   inputdirectory = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print 'ImageRenaming.py -i <inputdirectory>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'ImageRenaming.py -i <inputdirectory>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputdirectory = arg
   print 'Input Directory is ', inputdirectory

   for filename in os.listdir(inputdirectory):
      #print filename
      tokens = filename.split('.', 2)
      #print tokens
	 
      if len(tokens[1]) == 10:
         tokens[1] = tokens[1][:9] + '0' + tokens[1][9:]

      newFilename = tokens[0] + '.' + tokens[1] + '.' + tokens[2]
      os.rename(inputdirectory + filename, inputdirectory + newFilename)


if __name__ == "__main__":
   main(sys.argv[1:])

