#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

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

""" Important! 
--->>>> Requires dnspython
"""
bls = [ "short.rbl.jp", "owps.dnsbl.net.aupbl.spamhaus.org","bogons.cymru.com",
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
		"torserver.tor.dnsbl.sectoor.de"

	]


def color(text, color_code):
		if sys.platform == "win32" and os.getenv("TERM") != "xterm":
				return text

		return '\x1b[%dm%s\x1b[0m' % (color_code, text)


def red(text):
		return color(text, 31)


def blink(text):
		return color(text, 5)


def green(text):
		return color(text, 32)


def blue(text):
		return color(text, 34)

var1 = 0 
var2 = 0 
var3 = 0
var4 = 0
var5 = 0

print "Click i or d for scanning"
x = raw_input()
if x == "i":
		print "Write an ip address"
		myIP = raw_input()

		for bl in bls:
				try:
						my_resolver = dns.resolver.Resolver()
						query = '.'.join(reversed(str(myIP).split("."))) + "." + bl
						my_resolver.timeout = 2
						my_resolver.lifetime = 2
						answers = my_resolver.query(query, "A")
						answer_txt = my_resolver.query(query, "TXT")
						var5 = var5+1
						print 'IP: %s IS listed in %s (%s: %s)' %(myIP, bl, answers[0], answer_txt[0])

				except dns.resolver.NXDOMAIN:
					var1= var1+1
					print 'IP: %s is NOT listed in %s' %(myIP, bl)

			 
				except dns.resolver.Timeout:
					var2= var2+1
					print (blink('WARNING: Timeout querying ' + bl))

				except dns.resolver.NoNameservers:
					var3= var3+1
					print (blink('WARNING: No nameservers for ' + bl))

				except dns.resolver.NoAnswer:
					var4= var4+1
					print (blink('WARNING: No answer for ' + bl))
		var6= var1 + var2 + var3 + var4 + var5
		print
		print '*****RESULT OF %s BLACKLIST SERVERS FOR %s*****' %(var6,myIP)
		print 
		print 'The IP address is not listed in %s BLServer(s).'  %(var1)      
		print 'The IP address is listed in %s BLServer(s).'  %(var5) 
		print     
		print 'Timeout querying in %s BLServer(s).'  %(var2) 
		print 'No answer for %s BLServer(s).'  %(var4) 
		print 'No nameservers for %s BLServer(s).'  %(var3) 
		print 

else:
		import socket
		print "Write a domain address"
		myDomain = raw_input()

		for bl in bls:
			try:
				myIP = socket.gethostbyname(myDomain)
				my_resolver = dns.resolver.Resolver()
				query = '.'.join(reversed(str(myIP).split("."))) + "." + bl
				my_resolver.timeout = 2
				my_resolver.lifetime = 2
				answers = my_resolver.query(query, "A")
				answer_txt = my_resolver.query(query, "TXT")
				var5 = var5+1
				print 'IP: %s IS listed in %s (%s: %s)' %(myDomain, bl, answers[0], answer_txt[0])

			except dns.resolver.NXDOMAIN:
				var1= var1+1
				print 'IP: %s is NOT listed in %s' %(myIP, bl)

			 
			except dns.resolver.Timeout:
				var2= var2+1
				print (blink('WARNING: Timeout querying ' + bl))
			except dns.resolver.NoNameservers:
				var3= var3+1
				print (blink('WARNING: No nameservers for ' + bl))

			except dns.resolver.NoAnswer:
				var4= var4+1
				print (blink('WARNING: No answer for ' + bl))
		var6= var1 + var2 + var3 + var4 + var5
		print
		print '*****RESULT OF %s BLACKLIST SERVERS FOR %s*****' %(var6,myIP)
		print 
		print 'The IP address is not listed in %s BLServer(s).'  %(var1)      
		print 'The IP address is listed in %s BLServer(s).'  %(var5) 
		print     
		print 'Timeout querying in %s BLServer(s).'  %(var2) 
		print 'No answer for %s BLServer(s).'  %(var4) 
		print 'No nameservers for %s BLServer(s).'  %(var3) 
		print
