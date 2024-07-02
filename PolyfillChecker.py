import os
import urllib.request
from urllib.parse import urlsplit
from pathlib import Path

#Remove html.txt in case the last run was stopped before output was deleted
path = Path("html.txt")

if path.is_file():
    print("Deleting old html.txt file. Please run again.")
    os.remove(path)
    exit()

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

#Parse html file and search each line for cdn.polyfill.io
#If the string is found, print out vulnerable message and line found
#If not foud result != 1, print not vulnerable.
result = 0
print("Parsing HTML...")

with open('html.txt', 'r', encoding='utf-8') as file:
    htmlData = file.readlines()
    
    for row in htmlData:
        domain = "cdn.polyfill.io"

        if row.find(domain) != -1:
            print("cdn.polyfill.io found in html!")
            ind = str(htmlData.index(row) + 1)
            print("Found on line: " + ind)
            htmlData.index(row)
            result = 1

if result != 1:
    print("Website is not vulnerable!")

#Ask user if they would like to save the output.
#If they do want to save the output, rename the output to not collide with further executions.
#If they do not wish to keep the output, simply remove the html.txt file. 
response = input("Would you like to keep the HTML output? (Y/N): ")
response = response.lower()

if response == "y" or response == "yes":
    renamedFile = urlsplit(url2).netloc + "_PC_Output.txt"
    os.rename("html.txt", renamedFile)
    print("Output file saved as " + renamedFile)
else:
    os.remove("html.txt")
    print("Output file has been removed.")