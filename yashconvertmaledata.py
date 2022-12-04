import re
import json
thing = [
 {
   "FIELD1": "Baseball",
   "FIELD2": 297,
   "FIELD3": "10,820",
   "FIELD4": 36,
   "FIELD5": 265,
   "FIELD6": "11,014",
   "FIELD7": 42,
   "FIELD8": 389,
   "FIELD9": "14,177",
   "FIELD10": 36.4
 },
 {
   "FIELD1": "Basketball",
   "FIELD2": 351,
   "FIELD3": "5,510",
   "FIELD4": 16,
   "FIELD5": 312,
   "FIELD6": "5,523",
   "FIELD7": 18,
   "FIELD8": 423,
   "FIELD9": "7,783",
   "FIELD10": 18.4
 },
 {
   "FIELD1": "Cross Country",
   "FIELD2": 317,
   "FIELD3": "4,906",
   "FIELD4": 16,
   "FIELD5": 275,
   "FIELD6": "3,640",
   "FIELD7": 13,
   "FIELD8": 405,
   "FIELD9": "5,757",
   "FIELD10": 14.2
 },
 {
   "FIELD1": "Fencing*",
   "FIELD2": 21,
   "FIELD3": "396",
   "FIELD4": 18.9,
   "FIELD5": 2,
   "FIELD6": "31",
   "FIELD7": 15.5,
   "FIELD8": 12,
   "FIELD9": "234",
   "FIELD10": 19.5
 },
 {
   "FIELD1": "Football",
   "FIELD2": 254,
   "FIELD3": "29,206",
   "FIELD4": 115,
   "FIELD5": 169,
   "FIELD6": "19,064",
   "FIELD7": 113,
   "FIELD8": 249,
   "FIELD9": "25,442",
   "FIELD10": 102.2
 },
 {
   "FIELD1": "Golf",
   "FIELD2": 299,
   "FIELD3": "2,921",
   "FIELD4": 9.8,
   "FIELD5": 227,
   "FIELD6": "2,353",
   "FIELD7": 10.4,
   "FIELD8": 312,
   "FIELD9": "3,211",
   "FIELD10": 10.3
 },
 {
   "FIELD1": "Gymnastics",
   "FIELD2": 15,
   "FIELD3": "312",
   "FIELD4": 20.8,
   "FIELD5": 0,
   "FIELD6": "0",
   "FIELD7": 0,
   "FIELD8": 1,
   "FIELD9": "21",
   "FIELD10": 21
 },
 {
   "FIELD1": "Ice Hockey",
   "FIELD2": 60,
   "FIELD3": "1,711",
   "FIELD4": 28.5,
   "FIELD5": 7,
   "FIELD6": "215",
   "FIELD7": 30.7,
   "FIELD8": 83,
   "FIELD9": "2,397",
   "FIELD10": 28.9
 },
 {
   "FIELD1": "Lacrosse",
   "FIELD2": 73,
   "FIELD3": "3,489",
   "FIELD4": 47.8,
   "FIELD5": 71,
   "FIELD6": "2,818",
   "FIELD7": 39.7,
   "FIELD8": 242,
   "FIELD9": "8,296",
   "FIELD10": 34.3
 },
 {
   "FIELD1": "Rifle*",
   "FIELD2": 18,
   "FIELD3": "113",
   "FIELD4": 6.3,
   "FIELD5": 2,
   "FIELD6": "12",
   "FIELD7": 6,
   "FIELD8": 3,
   "FIELD9": "21",
   "FIELD10": 7
 },
 {
   "FIELD1": "Skiing*",
   "FIELD2": 11,
   "FIELD3": "149",
   "FIELD4": 13.5,
   "FIELD5": 6,
   "FIELD6": "74",
   "FIELD7": 12.3,
   "FIELD8": 15,
   "FIELD9": "208",
   "FIELD10": 13.9
 },
 {
   "FIELD1": "Soccer",
   "FIELD2": 205,
   "FIELD3": "6,044",
   "FIELD4": 29.5,
   "FIELD5": 215,
   "FIELD6": "6,864",
   "FIELD7": 31.9,
   "FIELD8": 417,
   "FIELD9": "12,591",
   "FIELD10": 30.2
 },
 {
   "FIELD1": "Swimming/Diving",
   "FIELD2": 131,
   "FIELD3": "3,771",
   "FIELD4": 28.8,
   "FIELD5": 75,
   "FIELD6": "1,619",
   "FIELD7": 21.6,
   "FIELD8": 238,
   "FIELD9": "4,409",
   "FIELD10": 18.5
 },
 {
   "FIELD1": "Tennis",
   "FIELD2": 251,
   "FIELD3": "2,539",
   "FIELD4": 10.1,
   "FIELD5": 167,
   "FIELD6": "1,617",
   "FIELD7": 9.7,
   "FIELD8": 331,
   "FIELD9": "3,629",
   "FIELD10": 11
 },
 {
   "FIELD1": "Track, Indoor",
   "FIELD2": 269,
   "FIELD3": "10,286",
   "FIELD4": 38.2,
   "FIELD5": 173,
   "FIELD6": "6,289",
   "FIELD7": 36.4,
   "FIELD8": 292,
   "FIELD9": "9,598",
   "FIELD10": 32.9
 },
 {
   "FIELD1": "Track, Outdoor",
   "FIELD2": 289,
   "FIELD3": "11,228",
   "FIELD4": 38.9,
   "FIELD5": 223,
   "FIELD6": "7,555",
   "FIELD7": 33.9,
   "FIELD8": 322,
   "FIELD9": "10,131",
   "FIELD10": 31.5
 },
 {
   "FIELD1": "Volleyball",
   "FIELD2": 22,
   "FIELD3": "455",
   "FIELD4": 20.7,
   "FIELD5": 24,
   "FIELD6": "420",
   "FIELD7": 17.5,
   "FIELD8": 102,
   "FIELD9": "1,480",
   "FIELD10": 14.5
 },
 {
   "FIELD1": "Water Polo",
   "FIELD2": 25,
   "FIELD3": "603",
   "FIELD4": 24.1,
   "FIELD5": 8,
   "FIELD6": "178",
   "FIELD7": 22.3,
   "FIELD8": 16,
   "FIELD9": "291",
   "FIELD10": 18.2
 },
 {
   "FIELD1": "Wrestling",
   "FIELD2": 75,
   "FIELD3": "2,479",
   "FIELD4": 33.1,
   "FIELD5": 62,
   "FIELD6": "1,884",
   "FIELD7": 30.4,
   "FIELD8": 108,
   "FIELD9": "2,937",
   "FIELD10": 27.2
 }
]
temp = [
  {
   "name": "Baseball",
   "children": [
    {
     "name": "Division 1",
     "children": [
      {"name": "Teams", "size": 254},
      {"name": "Atheletes", "size": 7461},
      {"name": "Avg Squad", "size": 29.4}

     ]
    },
    {
     "name": "Division 2",
     "children": [
      {"name": "Teams", "size": 3938},
      {"name": "Atheletes", "size": 3812},
      {"name": "Avg Squad", "size": 6714}

     ]
    },
    {
     "name": "Division 3",
     "children": [
      {"name": "Teams", "size": 3938},
      {"name": "Atheletes", "size": 3812},
      {"name": "Avg Squad", "size": 6714}

     ]
    }
   ]
  },
  {
   "name": "Basketball",
   "children": [
    {
     "name": "Division 1",
     "children": [
      {"name": "Teams", "size": 3938},
      {"name": "Atheletes", "size": 3812},
      {"name": "Avg Squad", "size": 6714}

     ]
    },
    {
     "name": "Division 2",
     "children": [
      {"name": "Teams", "size": 3938},
      {"name": "Atheletes", "size": 3812},
      {"name": "Avg Squad", "size": 6714}

     ]
    },
    {
     "name": "Division 3",
     "children": [
      {"name": "Teams", "size": 3938},
      {"name": "Atheletes", "size": 3812},
      {"name": "Avg Squad", "size": 6714}

     ]
    }
   ]
  },
  {
   "name": "Cross C",
   "children": [
    {
     "name": "Division 1",
     "children": [
      {"name": "Teams", "size": 3938},
      {"name": "Atheletes", "size": 3812},
      {"name": "Avg Squad", "size": 6714}

     ]
    },
    {
     "name": "Division 2",
     "children": [
      {"name": "Teams", "size": 3938},
      {"name": "Atheletes", "size": 3812},
      {"name": "Avg Squad", "size": 6714}

     ]
    },
    {
     "name": "Division 3",
     "children": [
      {"name": "Teams", "size": 3938},
      {"name": "Atheletes", "size": 3812},
      {"name": "Avg Squad", "size": 6714}

     ]
    }
   ]
  },
  {
   "name": "Fencing",
   "children": [
    {
     "name": "Division 1",
     "children": [
      {"name": "Teams", "size": 3938},
      {"name": "Atheletes", "size": 3812},
      {"name": "Avg Squad", "size": 6714}

     ]
    },
    {
     "name": "Division 2",
     "children": [
      {"name": "Teams", "size": 3938},
      {"name": "Atheletes", "size": 3812},
      {"name": "Avg Squad", "size": 6714}

     ]
    },
    {
     "name": "Division 3",
     "children": [
      {"name": "Teams", "size": 3938},
      {"name": "Atheletes", "size": 3812},
      {"name": "Avg Squad", "size": 6714}

     ]
    }
   ]
  },
  {
   "name": "Football",
   "children": [
    {
     "name": "Division 1",
     "children": [
      {"name": "Teams", "size": 3938},
      {"name": "Atheletes", "size": 3812},
      {"name": "Avg Squad", "size": 6714}

     ]
    },
    {
     "name": "Division 2",
     "children": [
      {"name": "Teams", "size": 3938},
      {"name": "Atheletes", "size": 3812},
      {"name": "Avg Squad", "size": 6714}

     ]
    },
    {
     "name": "Division 3",
     "children": [
      {"name": "Teams", "size": 3938},
      {"name": "Atheletes", "size": 3812},
      {"name": "Avg Squad", "size": 6714}

     ]
    }
   ]
  },
  {
   "name": "Golf",
   "children": [
    {
     "name": "Division 1",
     "children": [
      {"name": "Teams", "size": 3938},
      {"name": "Atheletes", "size": 3812},
      {"name": "Avg Squad", "size": 6714}

     ]
    },
    {
     "name": "Division 2",
     "children": [
      {"name": "Teams", "size": 3938},
      {"name": "Atheletes", "size": 3812},
      {"name": "Avg Squad", "size": 6714}

     ]
    },
    {
     "name": "Division 3",
     "children": [
      {"name": "Teams", "size": 3938},
      {"name": "Atheletes", "size": 3812},
      {"name": "Avg Squad", "size": 6714}

     ]
    }
   ]
  },
  {
   "name": "Gymnastics",
   "children": [
    {
     "name": "Division 1",
     "children": [
      {"name": "Teams", "size": 3938},
      {"name": "Atheletes", "size": 3812},
      {"name": "Avg Squad", "size": 6714}

     ]
    },
    {
     "name": "Division 2",
     "children": [
      {"name": "Teams", "size": 3938},
      {"name": "Atheletes", "size": 3812},
      {"name": "Avg Squad", "size": 6714}

     ]
    },
    {
     "name": "Division 3",
     "children": [
      {"name": "Teams", "size": 3938},
      {"name": "Atheletes", "size": 3812},
      {"name": "Avg Squad", "size": 6714}

     ]
    }
   ]
  },
  {
   "name": "Ice Hockey",
   "children": [
    {
     "name": "Division 1",
     "children": [
      {"name": "Teams", "size": 3938},
      {"name": "Atheletes", "size": 3812},
      {"name": "Avg Squad", "size": 6714}

     ]
    },
    {
     "name": "Division 2",
     "children": [
      {"name": "Teams", "size": 3938},
      {"name": "Atheletes", "size": 3812},
      {"name": "Avg Squad", "size": 6714}

     ]
    },
    {
     "name": "Division 3",
     "children": [
      {"name": "Teams", "size": 3938},
      {"name": "Atheletes", "size": 3812},
      {"name": "Avg Squad", "size": 6714}

     ]
    }
   ]
  },
  {
   "name": "Lacrosse",
   "children": [
    {
     "name": "Division 1",
     "children": [
      {"name": "Teams", "size": 3938},
      {"name": "Atheletes", "size": 3812},
      {"name": "Avg Squad", "size": 6714}

     ]
    },
    {
     "name": "Division 2",
     "children": [
      {"name": "Teams", "size": 3938},
      {"name": "Atheletes", "size": 3812},
      {"name": "Avg Squad", "size": 6714}

     ]
    },
    {
     "name": "Division 3",
     "children": [
      {"name": "Teams", "size": 3938},
      {"name": "Atheletes", "size": 3812},
      {"name": "Avg Squad", "size": 6714}

     ]
    }
   ]
  },
  {
   "name": "Rifle",
   "children": [
    {
     "name": "Division 1",
     "children": [
      {"name": "Teams", "size": 3938},
      {"name": "Atheletes", "size": 3812},
      {"name": "Avg Squad", "size": 6714}

     ]
    },
    {
     "name": "Division 2",
     "children": [
      {"name": "Teams", "size": 3938},
      {"name": "Atheletes", "size": 3812},
      {"name": "Avg Squad", "size": 6714}

     ]
    },
    {
     "name": "Division 3",
     "children": [
      {"name": "Teams", "size": 3938},
      {"name": "Atheletes", "size": 3812},
      {"name": "Avg Squad", "size": 6714}

     ]
    }
   ]
  },
  {
   "name": "Skiing",
   "children": [
    {
     "name": "Division 1",
     "children": [
      {"name": "Teams", "size": 3938},
      {"name": "Atheletes", "size": 3812},
      {"name": "Avg Squad", "size": 6714}
     ]
    },
    {
     "name": "Division 2",
     "children": [
      {"name": "Teams", "size": 3938},
      {"name": "Atheletes", "size": 3812},
      {"name": "Avg Squad", "size": 6714}

     ]
    },
    {
     "name": "Division 3",
     "children": [
      {"name": "Teams", "size": 3938},
      {"name": "Atheletes", "size": 3812},
      {"name": "Avg Squad", "size": 6714}

     ]
    }
   ]
  },
  {
   "name": "Soccer",
   "children": [
    {
     "name": "Division 1",
     "children": [
      {"name": "Teams", "size": 3938},
      {"name": "Atheletes", "size": 3812},
      {"name": "Avg Squad", "size": 6714}

     ]
    },
    {
     "name": "Division 2",
     "children": [
      {"name": "Teams", "size": 3938},
      {"name": "Atheletes", "size": 3812},
      {"name": "Avg Squad", "size": 6714}
     ]
    },
    {
     "name": "Division 3",
     "children": [
      {"name": "Teams", "size": 3938},
      {"name": "Atheletes", "size": 3812},
      {"name": "Avg Squad", "size": 6714}

     ]
    }
   ]
  },
  {
   "name": "Swimming",
   "children": [
    {
     "name": "Division 1",
     "children": [
      {"name": "Teams", "size": 3938},
      {"name": "Atheletes", "size": 3812},
      {"name": "Avg Squad", "size": 6714}

     ]
    },
    {
     "name": "Division 2",
     "children": [
      {"name": "Teams", "size": 3938},
      {"name": "Atheletes", "size": 3812},
      {"name": "Avg Squad", "size": 6714}
     ]
    },
    {
     "name": "Division 3",
     "children": [
      {"name": "Teams", "size": 3938},
      {"name": "Atheletes", "size": 3812},
      {"name": "Avg Squad", "size": 6714}

     ]
    }
   ]
  },
  {
   "name": "Tennis",
   "children": [
    {
     "name": "Division 1",
     "children": [
      {"name": "Teams", "size": 3938},
      {"name": "Atheletes", "size": 3812},
      {"name": "Avg Squad", "size": 6714}

     ]
    },
    {
     "name": "Division 2",
     "children": [
      {"name": "Teams", "size": 3938},
      {"name": "Atheletes", "size": 3812},
      {"name": "Avg Squad", "size": 6714}
     ]
    },
    {
     "name": "Division 3",
     "children": [
      {"name": "Teams", "size": 3938},
      {"name": "Atheletes", "size": 3812},
      {"name": "Avg Squad", "size": 6714}

     ]
    }
   ]
  },
  {
   "name": "Track,In",
   "children": [
    {
     "name": "Division 1",
     "children": [
      {"name": "Teams", "size": 3938},
      {"name": "Atheletes", "size": 3812},
      {"name": "Avg Squad", "size": 6714}

     ]
    },
    {
     "name": "Division 2",
     "children": [
      {"name": "Teams", "size": 3938},
      {"name": "Atheletes", "size": 3812},
      {"name": "Avg Squad", "size": 6714}

     ]
    },
    {
     "name": "Division 3",
     "children": [
      {"name": "Teams", "size": 3938},
      {"name": "Atheletes", "size": 3812},
      {"name": "Avg Squad", "size": 6714}

     ]
    }
   ]
  },
  {
   "name": "Track,Out",
   "children": [
    {
     "name": "Division 1",
     "children": [
      {"name": "Teams", "size": 3938},
      {"name": "Atheletes", "size": 3812},
      {"name": "Avg Squad", "size": 6714}
     ]
    },
    {
     "name": "Division 2",
     "children": [
      {"name": "Teams", "size": 3938},
      {"name": "Atheletes", "size": 3812},
      {"name": "Avg Squad", "size": 6714}

     ]
    },
    {
     "name": "Division 3",
     "children": [
      {"name": "Teams", "size": 3938},
      {"name": "Atheletes", "size": 3812},
      {"name": "Avg Squad", "size": 6714}

     ]
    }
   ]
  },
  {
   "name": "Volleyball",
   "children": [
    {
     "name": "Division 1",
     "children": [
      {"name": "Teams", "size": 3938},
      {"name": "Atheletes", "size": 3812},
      {"name": "Avg Squad", "size": 6714}

     ]
    },
    {
     "name": "Division 2",
     "children": [
      {"name": "Teams", "size": 3938},
      {"name": "Atheletes", "size": 3812},
      {"name": "Avg Squad", "size": 6714}

     ]
    },
    {
     "name": "Division 3",
     "children": [
      {"name": "Teams", "size": 3938},
      {"name": "Atheletes", "size": 3812},
      {"name": "Avg Squad", "size": 6714}

     ]
    }
   ]
  },
  {
   "name": "Waterpolo",
   "children": [
    {
     "name": "Division 1",
     "children": [
      {"name": "Teams", "size": 3938},
      {"name": "Atheletes", "size": 3812},
      {"name": "Avg Squad", "size": 6714}

     ]
    },
    {
     "name": "Division 2",
     "children": [
      {"name": "Teams", "size": 3938},
      {"name": "Atheletes", "size": 3812},
      {"name": "Avg Squad", "size": 6714}

     ]
    },
    {
     "name": "Division 3",
     "children": [
      {"name": "Teams", "size": 3938},
      {"name": "Atheletes", "size": 3812},
      {"name": "Avg Squad", "size": 6714}

     ]
    }
   ]
  },
  {
   "name": "Wrestling",
   "children": [
    {
     "name": "Division 1",
     "children": [
      {"name": "Teams", "size": 3938},
      {"name": "Atheletes", "size": 3812},
      {"name": "Avg Squad", "size": 6714}

     ]
    },
    {
     "name": "Division 2",
     "children": [
      {"name": "Teams", "size": 3938},
      {"name": "Atheletes", "size": 3812},
      {"name": "Avg Squad", "size": 6714}

     ]
    },
    {
     "name": "Division 3",
     "children": [
      {"name": "Teams", "size": 3938},
      {"name": "Atheletes", "size": 3812},
      {"name": "Avg Squad", "size": 6714}

     ]
    }
   ]
  }]

for i in range(len(thing)):

    if type(thing[i]["FIELD2"]) == str:
      if thing[i]["FIELD2"] == "N/A":
        thing[i]["FIELD2"] = 0.0
      else:
        thing[i]["FIELD2"] = float(thing[i]["FIELD2"].replace(',',''))
    if type(thing[i]["FIELD3"]) == str:
      if thing[i]["FIELD3"] == "N/A":
        thing[i]["FIELD3"] = 0.0
      else:
        thing[i]["FIELD3"] = float(thing[i]["FIELD3"].replace(',',''))
    if type(thing[i]["FIELD4"]) == str:
      if thing[i]["FIELD4"] == "N/A":
        thing[i]["FIELD4"] = 0.0
      else:
        thing[i]["FIELD4"] = float(thing[i]["FIELD4"].replace(',',''))
    if type(thing[i]["FIELD5"]) == str:
      if thing[i]["FIELD5"] == "N/A":
        thing[i]["FIELD5"] = 0.0
      else:
        thing[i]["FIELD5"] = float(thing[i]["FIELD5"].replace(',',''))
    if type(thing[i]["FIELD6"]) == str:
      if thing[i]["FIELD6"] == "N/A":
        thing[i]["FIELD6"] = 0.0
      else:
        thing[i]["FIELD6"] = float(thing[i]["FIELD6"].replace(',',''))
    if type(thing[i]["FIELD7"]) == str:
      if thing[i]["FIELD7"] == "N/A":
        thing[i]["FIELD7"] = 0.0
      else:
        thing[i]["FIELD7"] = float(thing[i]["FIELD7"].replace(',',''))
    if type(thing[i]["FIELD8"]) == str:
      if thing[i]["FIELD8"] == "N/A":
        thing[i]["FIELD8"] = 0.0
      else:
        thing[i]["FIELD8"] = float(thing[i]["FIELD8"].replace(',',''))
    if type(thing[i]["FIELD9"]) == str:
      if thing[i]["FIELD9"] == "N/A":
        thing[i]["FIELD9"] = 0.0
      else:
        thing[i]["FIELD9"] = float(thing[i]["FIELD9"].replace(',',''))
    if type(thing[i]["FIELD10"]) == str:
      if thing[i]["FIELD10"] == "N/A":
        thing[i]["FIELD10"] = 0.0
      else:
        thing[i]["FIELD10"] = float(thing[i]["FIELD10"].replace(',',''))

for i in range(len(thing)):
    temp[i]["children"][0]["children"][0]["size"] = float(thing[i]["FIELD2"])
    temp[i]["children"][0]["children"][1]["size"] = float(thing[i]["FIELD3"])
    temp[i]["children"][0]["children"][2]["size"] = float(thing[i]["FIELD4"])
    temp[i]["children"][1]["children"][0]["size"] = float(thing[i]["FIELD5"])
    temp[i]["children"][1]["children"][1]["size"] = float(thing[i]["FIELD6"])
    temp[i]["children"][1]["children"][2]["size"] = float(thing[i]["FIELD7"])
    temp[i]["children"][2]["children"][0]["size"] = float(thing[i]["FIELD8"])
    temp[i]["children"][2]["children"][1]["size"] = float(thing[i]["FIELD9"])
    temp[i]["children"][2]["children"][2]["size"] = float(thing[i]["FIELD10"])

y = json.dumps(temp)
print(y)
