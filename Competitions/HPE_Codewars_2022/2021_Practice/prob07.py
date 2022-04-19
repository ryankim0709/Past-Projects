import numpy

surface = {"CONCRETE": 0, 'WOOD': 1, 'STEEL': 2, 'RUBBER': 3, 'ICE': 4}
material = {"RUBBER": 0, "WOOD": 1, "STEEL": 2}

thingList = [["0.90", "0.62", "0.57"], ["0.80", "0.42", "0.30"],
			 ["0.70", "0.30", "0.74"], ["1.15", "0.80", "0.70"],
			 ["0.15", "0.05", "0.03"]]

[mtr, sfc] = input().split()

friction = thingList[surface[sfc]][material[mtr]]

print(f"{friction} {round(float(numpy.degrees(numpy.arctan(float(friction)))),1)}")