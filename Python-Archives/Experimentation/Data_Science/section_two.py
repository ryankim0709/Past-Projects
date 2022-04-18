from hashlib import new
import math
import statistics as stats

def main():
    def getPhoneData():
        phoneData = "./phones.txt"
        with open(phoneData, 'r') as data:
            line = "-"
            while line != "":
                line = data.readline().split()
                if line == []:
                    break

                year.append(float(line[0]))
                phones.append(float(line[1].replace(',', '')))
    def getCO2Data():
        COTwoData = "./CO2.txt"
        with open(COTwoData, 'r') as data:
            line = "-"
            while line != "":
                line = data.readline().split()
                if line == []:
                    break

                year.append(float(line[0]))
                co2.append(float(line[1].replace(',', '')))
    def getSizeData():
        sizeData = "./size.txt"
        with open(sizeData, 'r') as data:
            line = "-"
            while line != "":
                line = data.readline().split()
                if line == []:
                    break

                year.append(float(line[0]))
                newHouses.append(float(line[1].replace(',', '')))
    def getGamerData():
        gamerData = "./gamers.txt"
        with open(gamerData, 'r') as data:
            line = "-"
            while line != "":
                line = data.readline().split()
                if line == []:
                    break

                year.append(float(line[0]))
                gamers.append(float(line[1].replace(',', '')))
    year = []  # year
    phones = []  # population size
    co2 = [] # co2 levels
    newHouses = [] # Number of new houses
    gamers = [] # Percent of gamers that are male
    
    getPhoneData()
    getCO2Data()
    getSizeData()
    getGamerData()

    print("Covariance",getCovariance(phones, co2))
    print("Correlation",getCorrelationCoefficient(phones, co2))
    print("\n")
    print("Covariance",getCovariance(phones, newHouses))
    print("Correlation",getCorrelationCoefficient(phones, newHouses))
    print("\n")
    print("Covariance",getCovariance(phones, gamers))
    print("Correlation",getCorrelationCoefficient(phones, gamers))

def getMean(set):
    # Sum/length
    return round(sum(set)/len(set),2)

def getVariance(set):
    mean = getMean(set) # Mean
    variance = 0 # Variance
    for data in set: # Get variance
        variance += (data - mean) ** 2
    return round(variance/len(set), 2)
def getStandardDeviation(set):
    # Standard Deviation = square root of variance
    return round(getVariance(set) ** 0.5, 2)

def getCovariance(data1, data2):
    m1 = getMean(data1) # Mean for data 1
    m2 = getMean(data2) # Mean for data 2

    covaraiance = 0
    for x in range(0, len(data1)): # Get covariance
        covaraiance += (data1[x] - m1) * (data2[x] - m2)
    return round(covaraiance/(len(data1)),2) 
def getCorrelationCoefficient(data1, data2):
    # Correlation Coefficient = Product of standard deviation's/covariance of two data
    prod = getStandardDeviation(data1) * getStandardDeviation(data2)
    return round(getCovariance(data1, data2)/prod,2)

main()