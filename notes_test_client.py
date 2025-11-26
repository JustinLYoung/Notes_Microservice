import zmq
import json

def call(command):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://127.0.0.1:5560")

    socket.send_json(command)
    return socket.recv_json()


# add a note
print(call({"command": "add", "note": "Remember to do x next time"}))

# add a note
print(call({"command": "add", "note": "Review all notes on Saturday"}))

# show all notes
print(call({"command": "show_all"}))

# delete note with ID 2
print(call({"command": "delete", "id": 2}))

# show all notes
print(call({"command": "show_all"}))

# get note by id
print(call({"command": "get_note", "id": 1}))
