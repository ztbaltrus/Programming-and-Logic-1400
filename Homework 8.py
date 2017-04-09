# Conversions between feet and meters
# This program will ask the user if they would like to convert foot
# to meters or convert meters to foot.
#
#
# Zachary Baltrus
#
# Assignment 8
# CIT 1400

conversionLoop = 0
terminationLoop = 0
footAmount = 1
meterAmount = 20

def footToMeter(foot):
    meter = 0.305 * foot
    return meter

def meterToFoot(meter):
    foot = meter / 0.305
    return foot

while conversionLoop == 0:
    conversionChoice = input("Would you like to convert foot to meters, or meters to foot?: ")
    
    if conversionChoice == "foot to meters":
        print("Feet\t", "Meters")
        while footAmount <=10:
            print(footAmount, "\t", footToMeter(footAmount))
            footAmount += 1
        terminationLoop = 0
        conversionLoop = 1

    elif conversionChoice == "meters to foot":
        print("Meters\t", "Foot")
        while meterAmount <= 66:
            print(meterAmount, "\t", meterToFoot(meterAmount))
            if meterAmount % 10:
                meterAmount += 4
            else:
                meterAmount += 6
                
            terminationLoop = 0
            conversionLoop = 1
    
    while terminationLoop == 0:
        terminationChoice = input("Would you like to run the program again?:(y/n) ")
        if terminationChoice == "y" or terminationChoice == "yes":
            conversionLoop = 0
            terminationLoop = 1
        elif terminationChoice == "n" or terminationChoice == "no":
            conversionLoop = 1
            terminationLoop = 1
        else:
            conversionLoop = 1
            terminationLoop = 0
                

