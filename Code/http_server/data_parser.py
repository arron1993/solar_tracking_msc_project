#0,1471574671.2409966,1.173,-20.98724579872984/1,1471574671.2461786,1.1046,45/\n



data = "0,1471574671.2409966,1.173,-20.98724579872984/1,1471574671.2461786,1.1046,45/\n"

per_channel_reading = data.split("/")


for channel in per_channel_reading:
    readings = channel.split(",")
    if(len(readings) >= 4):
        read_channel = readings[0]
        time = readings[1]
        voltage = readings[2]
        angle = readings[3]
        print("{}{}{}{}".format(read_channel,time,voltage,angle))



