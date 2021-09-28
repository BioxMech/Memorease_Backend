import time
import dweepy
from multiprocessing import pool
from flask import Flask

app = Flask(__name__)

@app.route("/")
def dweet_listener():
    p = pool.Pool()
    p.apply_async(keepalive, args=['memorease'])
    manage('memorease')

def keepalive(id):
    while True:
        time.sleep(45)
        dweepy.dweet_for(thing_name=id,payload={"keepalive": 1}) # This is prone to failure so you have to implement a retry mechanism, but it should work 99.9% of the time 

def manage(id):
    dweepy.dweet_for(thing_name=id, payload={})
    for dweet in dweepy.listen_for_dweets_from(id):
      content = dweet['content']
      if "keepalive" in content:
        pass
      if "data" in content:
        print(content)


if __name__ == "__main__":
  app.run(port=5000, debug=True)