# Initializing

 
Run following commands to make a virtual environment installing zmq module

```sh

virtualenv -p python3 my-venv
. my-venv/bin/activate
pip3 install -r requirements.txt

```
# Starting Server
```sh

. my-venv/bin/activate
python3 server.py

```
# Starting Client

Open as many terminal as you want. replace `YOUR_NAME` in the code below with different client name to connect it to the server. 
```sh

. my-venv/bin/activate
python3 client.py YOUR_NAME

```
