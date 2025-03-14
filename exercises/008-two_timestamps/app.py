def two_timestamp(hr1, min1, sec1, hr2, min2, sec2):
    time1=hr1*3600+min1*60+sec1
    time2=hr2*3600+min2*60+sec2
    return time2 - time1


# Invoke the function and pass two timestamps(6 intergers) as its arguments
print(two_timestamp(1,2,30,1,3,20))
