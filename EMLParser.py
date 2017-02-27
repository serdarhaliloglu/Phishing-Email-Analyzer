#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import re
import sys
import os
import email
import mail
import json
import hashlib
from bs4 import BeautifulSoup
from lxml.html import tostring, html5parser
from HTMLParser import HTMLParser


class Parser:

	def __init(self):
		print "Parser Class Called"

	def header():
		try:
			f = open(sys.argv[1],'r')
			lines = f.readlines()
			headers = {}
			file = open(sys.argv[1]+".txt","w")
			print ("\n---------------HEADER PART------------------\n")
			file.write("-------------------HEADER PART--------------------\n")
			for line in lines:
				print(line)
				if len(line) == '\n':
					break
				if line[0] != ' ' and line[0] != '\t' and line[0] != '\r':
					hs = line.split(':',1)
					if len(hs) != 2:
						print(hs, ord(line[0]))
						break
					headers[hs[0]] = hs[1]
					file.write(hs[0]+':'+hs[1])	
		except Exception, e:
			print str(e)

	def body():
		try:
			f = open(sys.argv[1],'r+')
			lines = f.read()
			#lines = str(lines)
			b = email.message_from_string(lines)
			body = ""
			file = open(sys.argv[1]+".txt","a")
			print ("\n----------------BODY PART--------------\n")
			file.write('\n' + "----------------BODY PART-----------------" + '\n')
			if b.is_multipart():
				for part in b.walk():
					ctype = part.get_content_type()
					print ("ctype=", ctype)
					if ctype == 'text/plain':
						body = part.get_payload(decode=True)  # decode
						print body
						print "Plain Text Loop"
						file.write(body)
						file.write('\n')
						break

					elif ctype == 'text/html':
						print "HTML Text Loop1"
						body = part.get_payload(decode=True)

						soup = BeautifulSoup(body, "lxml")

						# kill all script and style elements
						for script in soup(["script", "style"]):
							script.extract()

						# get text
						text = soup.get_text()

						# break into lines and remove leading and trailing space on each
						lines = (line.strip() for line in text.splitlines())

						# break multi-headlines into a line each
						chunks = (phrase.strip() for line in lines for phrase in line.split("  "))

						# drop blank lines
						text = '\n'.join(chunk for chunk in chunks if chunk)

						print text
						file.write(text.encode('utf8'))

						file.close()
						break
			else:
					body = b.get_payload(decode=True)
					soup = BeautifulSoup(body, "lxml")

					# kill all script and style elements
					for script in soup(["script", "style"]):
						script.extract()

					# get text
					text = soup.get_text()

					# break into lines and remove leading and trailing space on each
					lines = (line.strip() for line in text.splitlines())

					# break multi-headlines into a line each
					chunks = (phrase.strip() for line in lines for phrase in line.split("  "))

					# drop blank lines
					text = '\n'.join(chunk for chunk in chunks if chunk)

					print text
					file.write(text.encode('utf8'))
					print "NOT MULTIPART"
					file.close()
					
		except Exception, e:
			print str(e)

	def attachment():

		try:
			with open(sys.argv[1], 'r+') as f:
				lines = f.read()
			#lines = str(lines)
			b = email.message_from_string(lines)

			print ("\n-------ATTACHMENT PART-------\n")
			detach_dir = '.'

			if 'attachments' not in os.listdir(detach_dir):
				os.mkdir('attachments')

			for part in b.walk():
				if part.get_content_maintype() == 'multipart':
				# print part.as_string()
					continue
				if part.get('Content-Disposition') is None:
					# print part.as_string()
					continue
				fileName = part.get_filename()

				if bool(fileName):
					filePath = os.path.join(detach_dir, 'attachments', fileName)
					if not os.path.isfile(filePath):
						print fileName

					with open(filePath, 'wa') as fp:
						fp.write(part.get_payload(decode=True))
						fp.write("\n-------ATTACHMENT PART-------\n")
						print (fileName + ' Dosyaya Yazilmistir.')

		except Exception as detail:
			print detail

	if __name__ == "__main__":
		header()
		body()
		attachment()



