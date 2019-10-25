import socket
import os
import time
import redis
from flask import Flask

app = Flask(__name__)

socket_host = input('Please enter the IP of the socket host mahcine in XXX.XXX.XX.XXX format: ')
socket_port = input('Please enter the Port of the socket host machine in XXXX format: ')

redis_host = input('Please enter the IP of the Redis host in format XXX.XXX.XX.XXX: ')
redis_port = input('Please enter the Port of the Redis host is using in format XXXX')
redis_db_num = input('Please enter the number associated with the Redis instance: ')

HOST = str(socket_host)
PORT = int(socket_port)

class SocketReceive:

    def receive_timeout(self):

        s = socket.socket()
        s.connect((HOST, PORT))
        s.setblocking(True)
        data_received = []
        data = ''

        start = time.time()
        while 1:
            if data_received and time.time():
                break

        try:
            data = s.recv(10000)
            if data:
                data_received.append(data)
                start = time.time()
            else:
                time.sleep(0.1)
        except:
            pass

        return data_received

class RedisConnect:

    def connect_db(self):

        data = SocketReceive()
        data_id = 0
        r = redis.Redis(redis_host, redis_port, redis_db_num)
        r.set(data_id, data.receive_timeout())
        data_id +=1

@app.route("/")
def main():

    redis = RedisConnect()
    socketrec = SocketReceive()

    redis.connect_db()
    print (socketrec.receive_timeout())

if __name__ == '__main__':
    app.run()