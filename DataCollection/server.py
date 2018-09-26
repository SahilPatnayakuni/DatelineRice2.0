import time
# import run
# import threading
import multiprocessing.dummy
import subprocess
import sys
import socket

# arbitrarily chosen number of threads to use for
# handling outside requests, low number should probably suffice
# because of the nature of this endpoint (only being used by UI
# for about one URL at a time)
# TODO: pull this number from the config database instead of having it hardcoded
NUM_CONSUMER = 4

# Just in case this file ever grows to reference the data collection and metadata extraction file more than once:
DCSCRIPT = "run.py"

# Set this to six hours by default
# TODO: pull a custom value from the config database
CHRON_TIME = 21600

# Code to access the config DB to change config on behalf of the UI
def handle_config(param): #TODO: implement :x
    pass

# Code to handle requests from UI:
def handle_request(shared_queue):
    print("Running consumer")
    while True:
        client_info = []
        client_info = shared_queue.get()

        client_socket = client_info[0]
        client_addr = client_info[1]

        req_line = ""
        buf = client_socket.recv(4096)
        req_line += buf.decode("ascii")
        while '\n' not in buf.decode("ascii"):
            print("looping: " + buf.decode("ascii"))
            req_line += buf.decode("ascii")
            buf = client_socket.recv(4096)

        if len(req_line.split()) != 3:
            print("Received malformed request from remote client: " + str(client_addr))
            client_socket.send("HTTP/1.1 400 Bad Request\r\n")
            continue

        req_type, resource, version = req_line.split(" ")

        print("New " + req_type + " request on resource \"" + resource + "\" HTTP version: " + version)

        if version != "HTTP/1.1\n":
            # print(version+"!!!")
            print("Received wrong version request from remote client: " + str(client_addr))
            client_socket.send("HTTP/1.1 400 Bad Request\r\n")
            continue

        if resource[0:3] == "/url":
            db_id = run.single_url(resource[4:])
            if (db_id != -1): # TODO add something like this functionality to run.py
                print("Serviced url " + resource[4:] + " successfully for remote client: " + str(client_addr))
                client_socket.send("HTTP/1.1 200 Success\r\n")
                client_socket.send(db_id+"\r\n")
            else:
                print("Failed to service url " + resource[4:] + " for remote client: " + str(client_addr))
                client_socket.send("HTTP/1.1 500 Internal Server Error\r\n")
                continue
        elif resource[0:6] == "/config":
            if (handle_config(resource[7:])):
                print("Changed configuration " + resource[7:] + " successfully for remote client: " + str(client_addr))
                client_socket.send("HTTP/1.1 200 Success\r\n")
            else:
                print("Failed to change configuration " + resource[7:] + " for remote client: " + str(client_addr))
                client_socket.send("HTTP/1.1 500 Internal Server Error\r\n")
                continue
        else:
            print("Received request from invalid resource (" + resource + ") from remote client: " + str(client_addr))
            client_socket.send("HTTP/1.1 404 Not Found\r\n")



    return # Never reaches this statement

# Procedure to put requests into the bounded buffer that the consumer threads will take from:
def producer(port_num, shared_queue):
    print("Running producer")

    # Create socket
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    # Bind to port_num
    serversocket.bind((host, port_num))


    # Here we allow very many unaccepted connections before starting to reject new connections
    # TODO this is probably a security concern - will want to change this to a reasonable number to prevent overloading the server
    serversocket.listen(4096)
    print("Listening on port " + str(port_num))
    print("hostname: " + host)
    while True:
        # Accept a request
        client_socket, client_addr = serversocket.accept()
        print("new request accepted")
        # Add it to the shared buffer:
        client_info = {client_socket, client_addr}
        shared_queue.put([client_socket, client_addr])


# Code to run "chron"-type invocation of the
# data collection and extraction process.
def chron_job():
    while True:
        # spawn off new process with arguments to open the chron script:
        p = subprocess.Popen(["python3", DCSCRIPT])
        print("Running Dateline data collection and metadata extraction script.")
        print(p.poll())
        time.sleep(CHRON_TIME)
    return # should never get to this return

# The main function runs a thread that handles
# the chron function, and spawns off multiple threads
# that service requests
if __name__ == "__main__":
    print(sys.argv)

    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python server.py [port number]")
        exit()

    request_queue = multiprocessing.dummy.Queue()


    # Spawn off NUM_CONSUMER threads for servicing individual URL requests from the user
    # pool = multiprocessing.dummy.Pool(NUM_CONSUMER)
    # numbers = range(NUM_CONSUMER)
    # pool.map(handle_request, numbers)
    consumer_threads = []
    for i in range(NUM_CONSUMER):
        new_thread = multiprocessing.dummy.Process(target=handle_request, args=[request_queue])
        consumer_threads.append(new_thread)
        new_thread.start()

    # Spawn off a singular producer thread for accepting individual URL requests from the user
    prod = multiprocessing.dummy.Process(target=producer, args=(int(sys.argv[1]), request_queue))
    prod.start()
    # And then use this thread to run the chron job functionality
    chron_job()
