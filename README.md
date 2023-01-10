# websockets-demos
## Instructions
1. Run the file `S-OnltRecievesMessage.py` file which runs the websockets server and then run `C-ConnCLosedImmediately.py` file to observe a client make a websocket connection, send a message to the server and then close the connection.
2. Run the file `S-OnltRecievesMessage.py` file which runs the websockets server and then run `C-OnlySendsMessage.py` file to observe a client send messages continuously while keeping the connection open with the server.
3. Run the file `S-RecievesSendsSequentially.py` file which runs the websockets server that recieves and then sends messages, and then run `C-SendsRecievesSequentially.py` which sends and then recieves messages to and from the server while keeping the connection open.
4. Run the file `S-RecievesSendsConcurrently.py` file which runs the websockets server that recieves and then concurrently sends messages, and then run `C-SendsRecievesConcurrently.py` which sends and then concurrently recieves messages to and from the server while keeping the connection open.
