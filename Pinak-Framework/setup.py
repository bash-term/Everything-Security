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

#Chrome and Aquatone binary
iChr1="wget https://download-chromium.appspot.com/dl/Linux_x64?type=snapshots -O Chrome.zip"
output=subprocess.run(iChr1,shell=True)
iChr2="unzip Chrome.zip"
output=subprocess.run(iChr2,shell=True)
iChr3="cp chrome /bin/"
output=subprocess.run(iChr3,shell=True)

iAqua1="wget https://github.com/michenriksen/aquatone/releases/download/v1.7.0/aquatone_linux_amd64_1.7.0.zip -O Aquatone.zip"
output=subprocess.run(iAqua1,shell=True)
iAqua2="unzip Aquatone.zip"
output=subprocess.run(iAqua2,shell=True)
iAqua3="cp aquatone /bin/"
output=subprocess.run(iAqua3,shell=True)
