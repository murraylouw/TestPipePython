
import time
import struct

pipeFile = open(r'\\.\pipe\ik_pipe', 'r+b', 0)

while True:
    jointValues = "1 2 3 4 5 6"
    message_from_python = '<joint_values>{0}<joint_values/>'.format(jointValues).encode('ascii')
        
    pipeFile.write(struct.pack('I', len(message_from_python)) + message_from_python)   # Write str length and str
    pipeFile.seek(0)                               # EDIT: This is also necessary

    print('Python sent: ', message_from_python)

    received_str_length = struct.unpack('I', pipeFile.read(4))[0]    # Read str length
    message_from_dotnet = pipeFile.read(received_str_length).decode('ascii')           # Read str
    pipeFile.seek(0)                               # Important!!!

    print('Received from .NET: ', message_from_dotnet)

    time.sleep(2)