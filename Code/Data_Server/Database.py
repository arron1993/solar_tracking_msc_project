import sqlite3
class Database:
    def __init__(self,file_name):
        self.conn = sqlite3.connect(file_name+".db")
        self.c = self.conn.cursor()

        # Create table
        self.c.execute('''CREATE TABLE if not exists readings(time text,channel text, gpio_pin text, angle_mode text, angle text, voltage text)''')
        self.conn.commit()


    def insert(self,reading):
        per_channel_reading = reading.split("/")
        for channel in per_channel_reading:
            print(channel)
            values = channel.split(",")
            if(len(values) >= 6):
                time = values[0]
                read_channel = values[1]
                gpio_pin = values[2]
                angle_mode = values[3]
                angle = values[4]
                voltage = values[5]

                insert_sql = "INSERT INTO readings VALUES ('{}','{}','{}','{}','{}','{}')".format(time,read_channel,gpio_pin,angle_mode,angle,voltage)

                self.c.execute(insert_sql )
            self.conn.commit()

    def __del__(self):
        self.conn.close()


