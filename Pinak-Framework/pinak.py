from termcolor import colored
import requests
import regex
import logging

#Take input from stdin
inp = input(str("Enter Domain Name: "))

#Show input
print(colored("I will now scan: "+inp,'green'))

#Logging for better 'logging'
level    = logging.INFO
format   = '  %(message)s'
handlers = [logging.FileHandler(inp+'_temp.txt'), logging.StreamHandler()]

logging.basicConfig(level = level, format = format, handlers = handlers)

#Parse input to wayback()
print('Scanning WayBack Database')
wbk = requests.get('https://web.archive.org/cdx/search/cdx?url=*.'+inp+'&output=txt&fl=original&collapse=urlkey&page=')
out = regex.findall("[a-z-0-9-_\.A-Z]{1,20}\."+inp,wbk.text)
set_of_domain = set(out)
for domain in set_of_domain:
    logging.info(colored(domain, 'yellow'))
# TODO: Show count

#Parse input to crtSh()
print('Scanning Crt.Sh Database')
crt = requests.get('https://crt.sh/?q=%.'+inp+'&output=json')
out1 = regex.findall("[a-z-0-9-_\.A-Z]{1,20}\."+inp,crt.text)
set_of_domain = set(out1)
for domain in set_of_domain:
    logging.info(colored(domain, 'yellow'))
# TODO: Show count

#Parse input to bufferover()
print('Scanning BufferOver Database')
buf = requests.get('https://dns.bufferover.run/dns?q=.'+inp)
out3 = regex.findall("[a-z-0-9-_\.A-Z]{1,20}\."+inp,buf.text)
set_of_domain = set(out3)
for domain in set_of_domain:
    logging.info(colored(domain, 'yellow'))
# TODO: Show count

print(colored('Resolving subdomains', 'green'))
#Store bufferover() output in temp.txt as append
#sys.stdout.close()

## Resolving Subdomains on 80 and 443 ports
resDom="cat subs_temp.log|httprobe|tee -a ResolvedSubdomains.txt"
out1=subprocess.run(resDom,shell=True)

##Collecting screenshots
ss="cat ResolvedSubdomains.txt | aquatone -ports large"
out2=subprocess.run(ss,shell=True)

#print(colored('Enumerating Juicy Directories ', 'green'))
#esDom="cat ResolvedSubdomains.txt|gee -suffix 'FUZZ'|ffuf -s -t 10 -mc 200 -w /wordlist.txt"
#output=subprocess.run(resDom,shell=True)

# Enumeration follows
