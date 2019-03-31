import requests

#This is the Australia Post Authorisation Key. 
#Go here to make one if you need: https://auspost.com.au/developers/apps/create
auspostKey = "XXX"

#The DPID is an 8 digit number used by AusPost to identify properties
#This could easily be pulled from a CSV and looped through the below function
DPID = 54516251

def getAddress(_DPID):
    auspostURL = "https://digitalapi.auspost.com.au/address-lookup/v1/addresses/" + str(_DPID) + "/detail"
    head = {'AUTH-KEY': auspostKey}
    r = requests.get(auspostURL, headers=head)
    if r.status_code == 200:
        rJSON = r.json()
        for x in rJSON['data']:
            print (x, ':', rJSON['data'][x])
    else:
        print("Error: " + str(r.status_code))
	print(r.text)
    return r

myAddress = getAddress(DPID)
