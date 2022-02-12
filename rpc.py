# THIS IS TO SHOW ACTIVITY ON DISCORD
from pypresence import Presence

client_id = "rpc client id"
RPC = Presence(client_id)
RPC.connect()
while True:
    info = open('info.txt', 'r')
    lines = info.readlines()
    line = lines[0]
    i = line.split('!@!')
    RPC.update(state=f"Listening to Stalkify with {i[0]}",
               details=f"Vibing to {i[1]} By {i[2]}", large_image=i[-1])
