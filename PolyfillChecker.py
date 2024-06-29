import os
import urllib.request

#Request user to supply url that we can parse. 
#Take their input and put it in the "url" variable.
#initialize url2 variable
print("Please enter a full URL to download and parse")
url = input("URL: ")
url = url.lower()
url2 = url

#Check to see if provided url is in proper sytnax.
if "https://" or "http://" not in url:
    url2 = "https://" + url
else:
    #issue here!
    url2 = url

#Take the user's URL, download the html and save it to html.txt.
#Could probably do without downloading 
urllib.request.urlretrieve(url2, "html.txt")

#Ask user if they would like to save the output.
#If they do want to save the output, rename the output to not collide with further executions.
#If they do not wish to keep the output, simply remove the html.txt file. 
response = input("Would you like to keep this output? (Y/N): ")
if response == "Y" or "y":
    Y = url + "_output.txt"
    os.rename("html.txt", Y)
else:
    Y = url + "_output.txt"
    os.remove("html.txt")
    os.remove("html.txt", Y)
    #Why is this not remove output and magically creating an output file? 