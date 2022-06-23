# Change.py
# calculates the average of several numbers

import math
def main():
    #input
    years = eval(input("For how many years do you have data? "))
    
    #process
    temp = 0
    for i in range(years):
        permits = eval(input("How many permits were issued this year? "))
        temp = permits + temp
    average = temp / years
    #output
    print("On average", round(average), "burials were performed each year")

main()
