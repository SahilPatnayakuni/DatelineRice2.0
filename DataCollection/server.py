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

# Code to handle requests from UI:
def handle_request(shared_queue):
    while True:
        client_info = []
        client_info = shared_queue.get()

        client_socket = client_info[0]
        client_addr = client_info[1]

        client_socket.

        return

# Procedure to put requests into the bounded buffer that the consumer threads will take from:
def producer(port_num, shared_queue):


    # Create socket
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    # Bind to port_num
    serversocket.bind((host, port_num))

    # Here we allow as many possible unaccepted connections before starting to reject new connections
    # TODO this is probably a security concern - will want to change this to a reasonable number to prevent overloading the server
    serversocket.listen(float("inf"))

    while True:
        # Accept a request
        client_socket, client_addr = serversocket.accept()

        client_socket.

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
    print("main\n")

    if len(sys.argv) != 2 or not sys.argv[1].isigit():
        print("Usage: python server.py [port number]")

    request_queue = multiprocessing.dummy.Queue()

    # Spawn off NUM_CONSUMER threads for servicing individual URL requests from the user
    # pool = multiprocessing.dummy.Pool(NUM_CONSUMER)
    # numbers = range(NUM_CONSUMER)
    # pool.map(handle_request, numbers)
    consumer_threads = []
    for i in range(NUM_CONSUMER):
        new_thread = multiprocessing.dummy.Process(target=handle_request, args=request_queue)
        consumer_threads.append(new_thread)
        new_thread.run()

    # Spawn off a singular producer thread for accepting individual URL requests from the user
    prod = multiprocessing.dummy.Process(target=producer, args=(sys.argv[1], request_queue))
    prod.run()
    # And then use this thread to do the chron job functionality
    chron_job()
