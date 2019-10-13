import datetime
 
start = datetime.datetime.strptime("2016-06-15", "%Y-%m-%d")
end = datetime.datetime.strptime("2016-06-30", "%Y-%m-%d")
date_array = \
    (start + datetime.timedelta(days=x) for x in range(0, (end-start).days))
 
for date_object in date_array:
    print(date_object.strftime("%Y-%m-%d"))