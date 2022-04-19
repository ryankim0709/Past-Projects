# This project is to do a little bit of data science

# This section will calculate various data science related values
# Mean, Median, Mode, Variance, Standard Deviation, Margin of error
# From https://www.dummies.com/article/academics-the-arts/math/statistics/top-10-statistical-formulas-142647

# Needed libraries
def main():
    # Section 1
    phoneData = "./phones.txt"
    year = []  # year
    phones = []  # population size

    with open(phoneData, 'r') as data:
        line = "-"
        while line != "":
            line = data.readline().split()
            if line == []:
                break

            year.append(float(line[0]))
            phones.append(float(line[1].replace(',', '')))

    # All calculations will be rounded to two decimal places so it is easy to read
    print("Mean:", getMean(phones))
    print("Median:", getMedian(phones))
    print("Mode:", getMode(phones))
    print("Variance:", getVariance(phones))
    print("Standard Deviation:", getStandardDeviation(phones))
    print("Percentile", getPercentile(phones[0], phones)) # Calculates which percentile an element is in
    # Use https://www.mymathtables.com/statistic/z-score-percentile-normal-distribution.html
    # To find which percentile this is in. IDK how to code this except hardcoding, which I don't want to do 
    print("P-value",getPVal(phones, 30)) # Tells you whether you should use 2 points of data or not
    print("\n")

def getMean(phones):
    # Sum/length
    return round(sum(phones)/len(phones),2)
def getMedian(phones):
    temp = phones
    temp.sort()
    if len(temp) % 2 == 1:
        # If there an even number of items, return center
        return temp[int(len(temp)/2)]
    else:
        # Else, return the average of the two middle items
        return round((temp[int(len(temp)/2)] + temp[int(len(temp)/2) - 1])/2,2)
def getMode(phones):
    percents = {} # Map for occurances
    maxOccurence = 1
    for x in phones: # Accumulate data
        if x in percents:
            maxOccurence = max(maxOccurence, percents[x] + 1)
            percents[x] = percents[x] + 1
        else:
            percents[x] = 1
    mode = []
    for key in percents:
        if percents[key] == maxOccurence:
            mode.append(key)

    mode.sort()

    if(len(mode) == len(percents)): 
        # If mode is the whole array and there is only one occurence there is no mode
        return "NONE"
    return mode
def getVariance(phones):
    mean = getMean(phones) # Mean
    variance = 0 # Variance
    for data in phones: # Get variance
        variance += (data - mean) ** 2
    return round(variance/len(phones), 2)
def getStandardDeviation(phones):
    # Standard Deviation = square root of variance
    return round(getVariance(phones) ** 0.5, 2)
def getPercentile(x, phones):
    mean = getMean(phones)
    deviation = getStandardDeviation(phones)
    z = (x-mean)/deviation
    return round(z, 2)
    
def getPVal(phones, hypothesis):
    # P-value for hypothesis is checking the probability that a point of data is greater than hypothesis
    # P-value give the probability that we get a sample mean that is more than N
    p_val = 0
    for x in phones:
        p_val += x if x > hypothesis else 0
    p_val = len(phones)
    return p_val

def getCovariance(data1, data2):
    m1 = getMean(data1) # Mean for data 1
    m2 = getMean(data2) # Mean for data 2

    covaraiance = 0
    for x in range(0, len(data1)): # Get covariance
        covaraiance += (data1[x] - m1) * (data2[x] - m2)
    return round(covaraiance/(len(data1)-1),2) 
def getCorrelationCoefficient(data1, data2):
    # Correlation Coefficient = Product of standard deviation's/covariance of two data
    return round((getStandardDeviation(data1) * getStandardDeviation(data2))/getCovariance(data1, data2),2)
main()