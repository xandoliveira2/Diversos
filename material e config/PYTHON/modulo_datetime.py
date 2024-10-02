import datetime as dt
d = dt.date(2024,10,1) 
print(d) # -> cria um objeto datetime.date que representa nossa data (ano,mes,dia)
print(dt.date.today())
data_hora = dt.datetime(2002,9,30,12,57,30,53211,)
print(data_hora)
tz = dt.timezone(dt.timedelta(hours=3))
data_hora = dt.datetime(2002,9,30,12,57,30,53211,tzinfo=tz)
print(data_hora)
delta = dt.timedelta(20.5, 40000,weeks=3)
print(delta)
SP = dt.timezone(dt.timedelta(hours=3))
print(SP)
print(dt.datetime.now())
import time
print(time.time())

