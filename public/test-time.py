import datetime

now =  datetime.datetime.now()
timestr = str(now).replace(' ','-').replace(':','-')
print now
print timestr[0:16]