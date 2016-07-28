#!/usr/bin/env python 

import os
import sys
import shutil 
import subprocess
import argparse

if __name__ == "__main__":
  parser = argparse.ArgumentParser( description = "Tool to create security.yaml file" )
  parser.add_argument( "-N", help = "Number of machines" )
  parser.add_argument( "-I", "--ip_address", metavar = "STARTING_IP_ADDRESS", 
      help = "Starting IP addresses" )
  parser.add_argument( "-H", "--hostname", metavar = "HOSTNAME", default = "machine",
      help = "Host name" )
  parser.add_argument( "-o", "--output", metavar = "OUTPUT", default = "config/security.yaml",
      help = "Output YAML IPSec/iptables configuration file" )
  args = parser.parse_args()

  doc = dict()
  ip_nums = list( int( i ) for i in args.ip_address.split( '.' ) )
  for i in range( int( args.N ) ):
      ip_address = '.'.join( '%d' % j for j in ip_nums )
      ip_nums[3] = ip_nums[3] + 1
      host = "%s%d" % ( args.hostname, i + 1 )
      machine = "machine%d" % ( i + 1 )
      doc[ host ] = { "machine_name": machine, "ip_address": ip_address }

  if not os.path.exists( os.path.dirname( args.output ) ): 
    os.makedirs( os.path.dirname( args.output ) )
  print( "Writing security configuration to %s" % args.output )
  with open( args.output, "w") as stream:
    try:
      import yaml
      stream.write( yaml.dump( doc, default_flow_style=False) )
    except:
      print( "Failed to import yaml! " )
      for k in doc.keys():
        stream.write( "%s: %s\n" % ( k, doc[k] ) )
