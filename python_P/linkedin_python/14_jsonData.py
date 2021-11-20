import urllib.request
import json

def printResult(data):
# Use the json module to load the string data into a dictionary
    JSONdata = json.loads(data)


 # now we can access the contents of the JSON like any other Python object
    if 'title' in JSONdata['metadata']:
        print(JSONdata['metadata']['title'])

 # output the number of events, plus the magnitude and each event name
    count = JSONdata['metadata']['count']
    print("event recorded "+ str(count))

# for each event, print the place where it occurred
    for i in JSONdata['features']:
        print(i['properties']['place'])
    print("----------------\n")

# print the events that only have a magnitude greater than 4
    for i in JSONdata['features']:
        if i['properties']['mag'] >= 4.0:
            print("%2.1f" %i['properties']['mag'], i['properties']['place'])
    print("----------------\n")

# print only the events where at least 1 person reported feeling something
    for i in JSONdata['features']:
        feltReport =i['properties']['felt']
        if feltReport != None:
            if feltReport > 0:
                print("%2.1f" %i['properties']['mag'], i['properties']['place']+" reported "+ str(feltReport) + " times " )





def main():
    webUrl = urllib.request.urlopen("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson")
    # print(webUrl.getcode())
    if(webUrl.getcode() == 200):
        data = webUrl.read()
        # print(data)
        printResult(data)
    else:
        print("Recieved an error frm server:"+str(webUrl.getcode()))
  

















if __name__ == "__main__":
    main()
