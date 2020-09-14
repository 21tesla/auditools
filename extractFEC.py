#!/usr/bin/python

from __future__ import print_function

import argparse
import os
import sys
import struct
import binascii

my_parser = argparse.ArgumentParser(description='get FEC values')
my_parser.add_argument('-file', type=str, 
                       help='the container file [FecContainer.fec]', 
                       required=True, 
                       action='store')

args = my_parser.parse_args()

fec_file =  args.file

with open(fec_file, "rb") as binary_file:
    data = binary_file.read()
 
file_length_in_bytes = os.path.getsize(fec_file)

vcrn = binascii.hexlify(data[14:19])
vin = data[20:37]
number_of_fec = (file_length_in_bytes - 43 - 132 - 12) / (2*4)

print()
print ('MIB2_FEC_Generator.sh -n', vcrn, '-v', vin, '-f ' , end='')

register = 43+(4*(number_of_fec))
for x in range (43, register, 4):
  print (binascii.hexlify(data[x:x+4]), ',' , sep='', end='')

print("00060800,00060900")

exit()