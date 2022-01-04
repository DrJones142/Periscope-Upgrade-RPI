import time 
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.IN)
print("Hello world!")

count = 0
count2 = 0
t_start = 0

# def my_callback(channel):
#     global count
#     if(count==0):
#         global t_start
#         t_start = time.perf_counter()
#     count+=1
#     if(count == 1000):
#         global count2
#         count2+=1
#         print(count2, "Elapsed Time: ", time.perf_counter()-t_start)
#         count = 0
    


# GPIO.add_event_detect(37, GPIO.RISING, callback=my_callback)



try:
    while True:
        pass
        t_start = time.perf_counter()
        GPIO.wait_for_edge(37, GPIO.RISING)
        count +=1
        if(count % 1000 == 0):
            count2+=1
            print(count2, "Elapsed Time: ", time.perf_counter()-t_start)

except KeyboardInterrupt:
    GPIO.cleanup()                                                 

