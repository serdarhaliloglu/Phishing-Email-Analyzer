# MSS
- MSS is an open source project to analyze malware which spreads via e-mail. MSS has three different modules, namely parsing, VirusTotal, blacklist modules.

## Team Members
   - Serdar HALİLOĞLU
   - Miray ELİBÜYÜK
   - Seçil TOPRAKEŞEN

## Parser Module

### EMLParser Usage

- python EMLParser.py FileName.eml
- The aim of parsing module in our project MSS is to separate all information in the email contents.

### IP-Link Parser

The script written by Johnny Wachter is used. We have changed the regex in IPAddresses.py which is in the class files.
https://github.com/JohnnyWachter/intel

The codes are integrated into our project. It will be added soon.

## VirusTotal Module
- Development of this module is over. It will be added soon.

## Blacklist Module
- It will check whether ip addresses or domain names in blacklist or not.
- Blacklists we use are RBL, SBL and so on.

### Usage
- python blacklist.py 
   - The system will ask you whether you want to scan an ip address or a domain name.
    - If you want to check an ip address, you have to write "i" for scanning.
      - Then, system will ask you to enter an ip address
    - If you want to check a domain name, you have to write "d" for scanning.
      - Then, system will ask you to enter a domain name.
