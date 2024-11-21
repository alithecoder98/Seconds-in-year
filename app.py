def sec():
    year=int(input("Enter the number of years:"))
    Days=365*year
    month=12*year
    weeks=52*year
    hours=24*365*year
    minutes=60*hours
    seconds=60*minutes
    print(f"in {year} are {Days} Days, {month} Months, {weeks} weeks, {hours} hours {minutes} Minutes and {seconds} Seconds")
if __name__=="__main__":
    sec()
