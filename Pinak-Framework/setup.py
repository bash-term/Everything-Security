import subprocess

#run pip install -r requirements.txt
req="pip install -r requirements.txt"
output=subprocess.run(req,shell=True)

#Setting up other dependencies

#httprobe binary
iHttprobe="go get -u github.com/tomnomnom/httprobe"
output=subprocess.run(iWayback,shell=True)
bin1="cp ~/go/bin/httprobe /bin/"
output=subprocess.run(bin1,shell=True)
