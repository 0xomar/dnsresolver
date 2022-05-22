#!/usr/bin/env python3

# dnsresolver.py omarfayyad.com
# author: Omar Fayyad
#
# script uses one argument as the domain
#        
#
# example: webenum.sh omarfayyad.com
# 
#----------------------------------------------------------------------------------
import dns.resolver
import sys

record_types = ['A', 'AAAA', 'NS', 'CNAME', 'MX', 'PTR', 'SOA', 'TXT']
try:
	domain = sys.argv[1]
except IndexError:
	print('Syntax Error - python3 dnsresolver.py <domainname>')

for records in record_types:
	try:
		answer = dns.resolver.resolve(domain,records)
		print('\n'+f'{records} Records')
		print('-'*30)
		for server in answer:
			print(server.to_text())
	except dns.resolver.NoAnswer:
		pass
	except NameError:
		quit()
	except dns.resolver.NXDOMAIN:
		print(f'{domain} does not exist.')
		quit()
	except KeyboardInterrupt:
		print('Just quitting. Run it again if you like!')
		quit()
