# Needed libraries
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def main():
    # Section 3

    # Data Reading
    def getPhoneData():
        phoneData = "/Users/Ryan/Desktop/Python-Archives/Experimentation/Data_Science/phones.txt"
        with open(phoneData, 'r') as data:
            line = "-"
            while line != "":
                line = data.readline().split()
                if line == []:
                    break

                year.append(int(line[0]))
                phones.append(float(line[1].replace(',', '')))
    def getCo2():
        phoneData = "/Users/Ryan/Desktop/Python-Archives/Experimentation/Data_Science/CO2.txt"
        with open(phoneData, 'r') as data:
            line = "-"
            while line != "":
                line = data.readline().split()
                if line == []:
                    break

                co2.append(float(line[1].replace(',', '')))

    year = []  # year
    phones = []  # population size
    co2 = [] # co2 in atmosphere

    getPhoneData()
    getCo2()

    phoneX = np.array(year).reshape((-1, 1))
    phoneY = np.array(phones)

    phoneModel = LinearRegression().fit(phoneX, phoneY)

    x = np.array([2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014,
    2015, 2016, 2017, 2018, 2019, 2020, 2021, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030])

    # Phones linear regression vs bar vs raw
    plt.subplot(1, 3, 1)
    plt.suptitle("Phones sold from 2008 (millions)")
    plt.plot(x, phoneModel.coef_ * x + phoneModel.intercept_)
    plt.xlabel("Year")
    plt.ylabel("Phones Sold in millions")
    plt.subplot(1, 3, 2)
    plt.bar(np.array(year), phoneY)
    plt.xlabel("Year")
    plt.ylabel("Phones Sold in millions")
    plt.subplot(1,3, 3)
    plt.plot(phoneX, phoneY)
    plt.xlabel("Year")
    plt.ylabel("Phones Sold in millions")
    plt.show()

    co2X = np.array(year).reshape((-1, 1))
    co2Y = np.array(co2)

    co2Model = LinearRegression().fit(co2X, co2Y)

    # CO2 lienar regression vs bar vs raw
    plt.subplot(1, 3, 1)
    plt.suptitle("Atmospheric CO2 from 2008 (gigatons)")
    plt.plot(x, co2Model.coef_ * x + co2Model.intercept_)
    plt.xlabel("Year")
    plt.ylabel("Atmospheric CO2 in gigatons")
    plt.subplot(1, 3, 2)
    plt.bar(np.array(year), co2Y)
    plt.xlabel("Year")
    plt.ylabel("Atmospheric CO2 in gigatons")
    plt.subplot(1, 3, 3)
    plt.plot(co2X, co2Y)
    plt.xlabel("Year")
    plt.ylabel("Atmospheric CO2 in gigatons")
    plt.show()

    # Phones regression vs CO2 regression
    plt.subplot(1, 2, 1)
    plt.suptitle("Phones sold vs atmospheric CO2 from 2008")
    plt.plot(x, phoneModel.coef_ * x + phoneModel.intercept_)
    plt.xlabel("Year")
    plt.ylabel("Phones Sold in millions")
    plt.subplot(1, 2, 2)
    plt.plot(x, co2Model.coef_ * x + co2Model.intercept_)
    plt.xlabel("Year")
    plt.ylabel("Atmospheric CO2 in gigatons")
    plt.show()

    # Exponential regression, graph values get too large to graph with matplotlib
    x = np.array([2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014,
    2015, 2016, 2017, 2018, 2019, 2020])
    fit = np.polyfit(year, np.log(phoneY), 1)

main()