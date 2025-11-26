import zmq
import json


notes = {}
id_num = 1

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://127.0.0.1:5560")

print("Note Service running on port 5560...")

while True:
    message = socket.recv_json()
    command = message.get("command")

    if command == "add":
        note = message.get("note")

        notes[id_num] = note
        socket.send_json({"status": "success", "message": "note added", "id": id_num})
        id_num += 1

    elif command == "show_all":
        socket.send_json(notes)

    elif command == "get_note":
        note_id = message.get("id")
        note_value = notes.get(note_id)
        socket.send_json({"id": note_id, "note": note_value})

    elif command == "delete":
        note_id = message.get("id")
        if note_id in notes:
            del notes[note_id]
            socket.send_json({"status": "success", "message": "Note deleted"})
        else:
            socket.send_json({"status": "error", "message": "Note not found"})

    else:
        socket.send_json({"status": "error", "message": "unknown command"})
