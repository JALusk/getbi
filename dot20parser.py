#!/usr/bin/python2.7 -tt

##
# Quick-and-dirty approach to approximating level population of H 
# in my vmax_changes models of SN 2000cb
#
# Takes in the departure coefficients (b_i's) from the .20 file
# as well as the ground state NLTE population densities from the 
# laus = 5 .o file, and the temperature structure from the .20 file
#

import gzip

class Dot20Parser:
  def __init__(self, model_name, model_number, file_path):
    self.model_name   = model_name 
    self.model_number = model_number
    self.file_path    = file_path
## TODO: filename should be passed as an argument
#model_name = "sn00cb_NLTE_vm40k_spec"
#model_num  = "12179"

#filename = model_name + ".20." + model_num + ".gz"

# This filename applies to the example data in the git repository:
#filename = 'dot20_example.dat'

## given a file, desired ion, and level, getbi() returns the bi at each
## layer in the atmosphere
##def getbi(filename, ionID, level):
  
## PHOENIX ouput files are gzipped, so use the gzip module
## to open them. 'rb' is a mode for reading a binary file.
##f = gzip.open(filename, 'rb')

## My example data, however, is not gzipped:
#f = open(filename, 'r')

#file_content = f.readlines()
#f.close()
  
## The data I want is bookended by two fixed strings.
#bi_startline = file_content.index(" 'START departure coefficients version 1.0'\n")
#bi_endline   = file_content.index(" 'END departure coefficients version 1.0'\n")
  
#nLayers = int(file_content[bi_startline + 1].split()[0])

#bi_data = file_content[bi_startline + 3 : bi_endline]
#bi_data = [w.replace('D' , 'E') for w in bi_data]

## Setting which ion/level you want to import
### TODO: These should be passed as arguments, as well.
#ionID = 100
#level = 1

## Almost always 128 layers, but that could change. NOTE: This code will
## break if PHOENIX output format changes to more/less than 10 layers/line
#if nLayers%10 == 0:
  #nlines = nLayers/10
#else:
  #nlines = nLayers/10 + 1

#foundData = False
#biFloat = []

#for line in bi_data:
  #if line.split()[0:2] == [str(ionID), str(level)]:
    ## Read in the bi data for that ionID,level
    #foundData = True
    #start = bi_data.index(line)
    #bi = bi_data[start + 1 : nlines + 1]

    #for line in bi:
      #biFloat = biFloat + [float(x) for x in line.split()]

    #print biFloat

#if foundData == False:
  #print "ERROR: Found no data for level %s of ion %s" % (level, ionID)
