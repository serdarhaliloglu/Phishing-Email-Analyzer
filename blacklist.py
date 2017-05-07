import dns.resolver
import sys
import os
import sys
import urllib
import urllib2
import argparse
import re
import socket
from urllib2 import urlopen

bls = [ "dnsrbl.org","rbl.megarbl.net","rbl.realtimeblacklist.com","bl.blocklist.de","bad.psky.me",
		"escalations.dnsbl.sorbs.net","stabl.rbl.webiron.net",
		"cabl.rbl.webiron.net","babl.rbl.webiron.net","short.rbl.jp", 
		"owps.dnsbl.net.aupbl.spamhaus.org","bogons.cymru.com",
		"rdts.dnsbl.net.au","web.dnsbl.sorbs.net","dnsbl.inps.de",
		"korea.services.net","ix.dnsbl.manitu.net","dnsbl.njabl.org",
		"spamlist.or.kr","spamrbl.imp.ch","proxy.block.transip.nl",
		"virus.rbl.msrbl.net","zen.spamhaus.org","db.wpbl.info",
		"duinv.aupads.org","ricn.dnsbl.net.au","dnsbl-2.uceprotect.net",
		"spam.abuse.ch","b.barracudacentral.org","cbl.abuseat.org",
		"dnsbl-1.uceprotect.net","bl.emailbasura.org","socks.dnsbl.sorbs.net",
		"spam.spamrats.com","sbl.spamhaus.org","osps.dnsbl.net.au",
		"t3direct.dnsbl.net.au","psbl.surriel.com","tor.dnsbl.sectoor.de",
		"drone.abuse.ch","relays.bl.gweep.ca","dynip.rothen.com",
		"omrs.dnsbl.net.au","dul.dnsbl.sorbs.net","residential.block.transip.nl",
		"spam.dnsbl.sorbs.net","owfs.dnsbl.net.au","noptr.spamrats.com",
		"ips.backscatterer.org","dyna.spamrats.com","http.dnsbl.sorbs.netimages.rbl.msrbl.net",
		"ubl.lashback.com","ohps.dnsbl.net.au","blacklist.woody.ch",
		"ubl.unsubscore.com","bl.spamcop.net","probes.dnsbl.net.auproxy.bl.gweep.ca",
		"dnsbl.sorbs.net","virus.rbl.jp","combined.rbl.msrbl.net",
		"misc.dnsbl.sorbs.net","orvedb.aupads.org","bl.spamcannibal.org",
		"spam.rbl.msrbl.net","dnsbl.cyberlogic.net","wormrbl.imp.ch",
		"zombie.dnsbl.sorbs.net","virbl.bit.nl","relays.bl.kundenserver.de",
		"smtp.dnsbl.sorbs.net","rbl.interserver.net","xbl.spamhaus.org",
		"osrs.dnsbl.net.au","dul.ru","rmst.dnsbl.net.au",
		"bl.deadbeef.com","combined.abuse.ch","dnsbl.dronebl.org",
		"cdl.anti-spam.org.cn","blackholes.five-ten-sg.com","aspews.ext.sorbs.net",
		"dnsbl-3.uceprotect.net","phishing.rbl.msrbl.net","relays.nether.net",
		"torserver.tor.dnsbl.sectoor.de", "bl.score.senderscore.org",
		"dnsbl.ahbl.org","rp.invaluement.com"] #setting of DNS Blacklist Servers

var1 = var2 = var3 = var4 = var5 = 0 

print 'Please enter an IP address or a Domain address'
input = raw_input()

pat = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")   #ip validation regex
test1 = pat.match(input)
if test1:	#if the given is a valid ip address									
	myIP=input  # set input to myIP

else:  #if the given is not a valid ip address, can be a valid domain address or invalid input
	validate = re.compile("^(([a-zA-Z]{1})|([a-zA-Z]{1}[a-zA-Z]{1})|([a-zA-Z]{1}[0-9]{1})|([0-9]{1}[a-zA-Z]{1})|([a-zA-Z0-9][a-zA-Z0-9-_]{1,61}[a-zA-Z0-9]))\.([a-zA-Z]{2,6}|[a-zA-Z0-9-]{2,30}\.[a-zA-Z]{2,3})$") #domain validation regex
	test2 = validate.match(input)  
	if test2:  #if the given is a valid domain address
		print '' #do nothing
	else: #if the given is not a valid ip or domain address
		print "\nInvalid IP or Domain address. Please enter the valid one."
		sys.exit(0) #exit

for bl in bls:    #if the given is a valid ip or domain address start scanning process
		try:	
				myIP = socket.gethostbyname(input) #convert domain address to ip address
				my_resolver = dns.resolver.Resolver()
				query = '.'.join(reversed(str(myIP).split("."))) + "." + bl
				my_resolver.timeout = 2
				my_resolver.lifetime = 2
				answers = my_resolver.query(query, "A")
				answer_txt = my_resolver.query(query, "TXT")
				var5 = var5+1
				print 'IP: %s IS listed in %s (%s: %s)' %(myIP, bl, answers[0], answer_txt[0]) 

		except socket.gaierror:
			sys.exit("Invalid Domain address. Please enter the valid one.")  #exit, if convertion is false

		except dns.resolver.NXDOMAIN:
			var1= var1+1
			print 'IP: %s is NOT listed in %s' %(myIP, bl)
			 
		except dns.resolver.Timeout:
			var2= var2+1
			print ('WARNING: Timeout querying ' + bl) 

		except dns.resolver.NoNameservers:
			var3= var3+1
			print ('WARNING: No nameservers for ' + bl)

		except dns.resolver.NoAnswer:
			var4= var4+1
			print ('WARNING: No answer for ' + bl) 

var6= var1 + var2 + var3 + var4 + var5 			   # calcute total number of DNS Blacklist Servers

print '\n*****RESULT OF %s BLACKLIST SERVERS FOR %s*****\n' %(var6,myIP) 		# print total number of DNS Blacklist Servers
print 'The IP address is not listed in %s BLServer(s).'  %(var1)     		    # print the ip/domain is not listed how many of DNS Blacklist Servers
print 'The IP address is listed in %s BLServer(s).\n'  %(var5)     			    # print the ip/domain is listed how many of DNS Blacklist Servers
print 'Timeout querying in %s BLServer(s).'  %(var2)                            # print the number of timeouts from DNS Blacklist Servers
print 'No answer for %s BLServer(s).'  %(var4)                                  # print the number of no answer from DNS Blacklist Servers
print 'No nameservers for %s BLServer(s).\n'  %(var3) 
