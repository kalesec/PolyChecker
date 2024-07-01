import os
import urllib.request
from urllib.parse import urlsplit

#Request user to supply url that we can parse. 
#Take their input and put it in the "url" variable.
#initialize url2 variable
print("Please enter a full URL to download and parse")
url = input("URL: ")
url = url.lower()
url2 = url

#Check to see if provided url is in proper sytnax.
if "https" and "http" in url:
    url2 = url
else:
    url2 = "https://" + url

#Confirmation and next steps
print("URL Entered: " + url2)
print("Downloading HTML...")

#Take the user's URL, download the html and save it to html.txt.
#Could probably do without downloading 
urllib.request.urlretrieve(url2, "html.txt")

# NEXT: PARSE HTML FILE AND SEARCH FOR cdn.polyfill.io (double check that)
# if the string is found print out vulnerable and remidiation steps, if not yadda yadda

#Ask user if they would like to save the output.
#If they do want to save the output, rename the output to not collide with further executions.
#If they do not wish to keep the output, simply remove the html.txt file. 
response = input("Would you like to keep this output? (Y/N): ")
response = response.lower()

if response == "y" or "yes":
    renamedFile = urlsplit(url2).netloc + "_PC_Output.txt"
    os.rename("html.txt", renamedFile)
    print("Output file saved as " + renamedFile)
else:
    os.remove("html.txt")
    print("Output file has been removed.")