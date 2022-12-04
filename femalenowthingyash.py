import json
import re

thing = [
 {
   "FIELD1": "Basketball",
   "FIELD2": "5,042",
   "FIELD3": "4,779",
   "FIELD4": "6,688"
 },
 {
   "FIELD1": "Cross Country",
   "FIELD2": "5,978",
   "FIELD3": "3,829",
   "FIELD4": "5,817"
 },
 {
   "FIELD1": "Fencing*",
   "FIELD2": "437",
   "FIELD3": "30",
   "FIELD4": "236"
 },
 {
   "FIELD1": "Golf",
   "FIELD2": "2,196",
   "FIELD3": "1,547",
   "FIELD4": "1,693"
 },
 {
   "FIELD1": "Gymnastics",
   "FIELD2": "1,105",
   "FIELD3": "148",
   "FIELD4": "289"
 },
 {
   "FIELD1": "Ice Hockey",
   "FIELD2": "860",
   "FIELD3": "110",
   "FIELD4": "1,561"
 },
 {
   "FIELD1": "Lacrosse",
   "FIELD2": "3,661",
   "FIELD3": "2,634",
   "FIELD4": "6,157"
 },
 {
   "FIELD1": "Rifle*",
   "FIELD2": "179",
   "FIELD3": "7",
   "FIELD4": "8"
 },
 {
   "FIELD1": "Skiing*",
   "FIELD2": "153",
   "FIELD3": "61",
   "FIELD4": "174"
 },
 {
   "FIELD1": "Soccer",
   "FIELD2": "9,446",
   "FIELD3": "7,609",
   "FIELD4": "11,255"
 },
 {
   "FIELD1": "Swimming/Diving",
   "FIELD2": "5,751",
   "FIELD3": "2,101",
   "FIELD4": "5,128"
 },
 {
   "FIELD1": "Tennis",
   "FIELD2": "2,836",
   "FIELD3": "1,901",
   "FIELD4": "3,859"
 },
 {
   "FIELD1": "Track, Indoor",
   "FIELD2": "13,296",
   "FIELD3": "6,088",
   "FIELD4": "8,597"
 },
 {
   "FIELD1": "Track, Outdoor",
   "FIELD2": "13,511",
   "FIELD3": "7,530",
   "FIELD4": "9,285"
 },
 {
   "FIELD1": "Volleyball",
   "FIELD2": "5,550",
   "FIELD3": "5,031",
   "FIELD4": "7,199"
 },
 {
   "FIELD1": "Water Polo",
   "FIELD2": "713",
   "FIELD3": "235",
   "FIELD4": "269"
 }
]
temp = [{'name': 'Baseball', 'children': [{'name': 'Division 1', 'children': 0}, {'name': 'Division 2', 'children': 0}, {'name': 'Division 3', 'children': 0}]}, {'name': 'Basketball', 'children': [{'name': 'Division 1', 'children': 0}, {'name': 'Division 2', 'children': 0}, {'name': 'Division 3', 'children': 0}]}, {'name': 'Cross C', 'children': [{'name': 'Division 1', 'children': 0}, {'name': 'Division 2', 'children': 0}, {'name': 'Division 3', 'children': 0}]}, {'name': 'Fencing', 'children': [{'name': 'Division 1', 'children': 0}, {'name': 'Division 2', 'children': 0}, {'name': 'Division 3', 'children': 0}]}, {'name': 'Football', 'children': [{'name': 'Division 1', 'children': 0}, {'name': 'Division 2', 'children': 0}, {'name': 'Division 3', 'children': 0}]}, {'name': 'Golf', 'children': [{'name': 'Division 1', 'children': 0}, {'name': 'Division 2', 'children': 0}, {'name': 'Division 3', 'children': 0}]}, {'name': 'Gymnastics', 'children': [{'name': 'Division 1', 'children': 0}, {'name': 'Division 2', 'children': 0}, {'name': 'Division 3', 'children': 0}]}, {'name': 'Ice Hockey', 'children': [{'name': 'Division 1', 'children': 0}, {'name': 'Division 2', 'children': 0}, {'name': 'Division 3', 'children': 0}]}, {'name': 'Lacrosse', 'children': [{'name': 'Division 1', 'children': 0}, {'name': 'Division 2', 'children': 0}, {'name': 'Division 3', 'children': 0}]}, {'name': 'Rifle', 'children': [{'name': 'Division 1', 'children': 0}, {'name': 'Division 2', 'children': 0}, {'name': 'Division 3', 'children': 0}]}, {'name': 'Skiing', 'children': [{'name': 'Division 1', 'children': 0}, {'name': 'Division 2', 'children': 0}, {'name': 'Division 3', 'children': 0}]}, {'name': 'Soccer', 'children': [{'name': 'Division 1', 'children': 0}, {'name': 'Division 2', 'children': 0}, {'name': 'Division 3', 'children': 0}]}, {'name': 'Swimming', 'children': [{'name': 'Division 1', 'children': 0}, {'name': 'Division 2', 'children': 0}, {'name': 'Division 3', 'children': 0}]}, {'name': 'Tennis', 'children': [{'name': 'Division 1', 'children': 0}, {'name': 'Division 2', 'children': 0}, {'name': 'Division 3', 'children': 0}]}, {'name': 'Track,In', 'children': [{'name': 'Division 1', 'children': 0}, {'name': 'Division 2', 'children': 0}, {'name': 'Division 3', 'children': 0}]}, {'name': 'Track,Out', 'children': [{'name': 'Division 1', 'children': 0}, {'name': 'Division 2', 'children': 0}, {'name': 'Division 3', 'children': 0}]}, {'name': 'Volleyball', 'children': [{'name': 'Division 1', 'children': 0}, {'name': 'Division 2', 'children': 0}, {'name': 'Division 3', 'children': 0}]}, {'name': 'Waterpolo', 'children': [{'name': 'Division 1', 'children': 0}, {'name': 'Division 2', 'children': 0}, {'name': 'Division 3', 'children': 0}]}, {'name': 'Wrestling', 'children': [{'name': 'Division 1', 'children': 0}, {'name': 'Division 2', 'children': 0}, {'name': 'Division 3', 'children': 0}]}]

cool = [1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17]

counter = 0
for i in range(len(thing)):

    temp[cool[counter]]["children"][0]["children"] = float(thing[i]["FIELD2"].replace(',',''))
    temp[cool[counter]]["children"][1]["children"] = float(thing[i]["FIELD3"].replace(',',''))
    temp[cool[counter]]["children"][2]["children"] = float(thing[i]["FIELD4"].replace(',',''))
    counter+=1
y = json.dumps(temp)
print(y)