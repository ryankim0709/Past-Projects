birthday = input().split("-")

dict = {
    2008:"Rat",
    2009:"Ox",
    2010:"Tiger",
    2011: "Rabbit",
    2012: "Dragon",
    2013: "Snake",
    2014: "Horse",
    2015: "Sheep",
    2016: "Monkey",
    2017: "Rooster",
    2018: "Dog",
    2019:"Pig"
}

animals = [
    ("3/21", "4/19","Aries"), 
    ("4/20", "5/20", "Tarus"),
    ("5/21", "6/20", "Gemini"),
    ("6/21","7/22", "Caner"),
    ("7/23", "8/22", "Leo"),
    ("8/23", "9/22", "Virgo"),
    ("9/23","10/22", "Libra"),
    ("10/23","11/21", "Scorpio"),
    ("11/22","12/21", "Sagittarius"),
    ("12/22","1/19", "Capricorn"),
    ("1/20, 2/18", "Aquarius"),
    ("2/19", "3/20", "Pisces")
]
months = [
    "",
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

year = birthday[0]
month = birthday[1]
day = birthday[2]
if day[0] == "0":
    day = day[1]

print("If you were born on "+months[int(month)]+" "+day+", your sign is")
print(year+" is the year of the "+dict[int(year)])