import pigpio 
import time

pi = pigpio.pi()

count = 0

def cbf(gpio,level,tick):
    global count
    count+=1

def cbf2(gpio,level,tick):
    global count
    count+=1


cb1 = pi.callback(26,pigpio.RISING_EDGE,cbf)

cb2 = pi.callback(26,pigpio.FALLING_EDGE,cbf2)


userInput = ""
while(userInput!="quit"):
    print("Type inputs")
    userInput = input()
    if(userInput=="c"):
        print(count)

print("Quiting")
cb1.cancel()
cb2.cancel()
exit()

# try:
#     while True:
#         pass

# except KeyboardInterrupt:
#     cb1.cancel()
#     exit()
