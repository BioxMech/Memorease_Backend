import dweepy

def cycle_from_dweet():
  try:
    for dweet in dweepy.listen_for_dweets_from('memorease'):
      print("Listening to updates from dweet thing 'memorease'...")
      print(dweet)
      location = dweet["content"]["location"] 
      execution(location)
      raise ConnectionError()        


  except requests.exceptions.ConnectionError as e:
    print(e.response)
    print("Connection closed by dweet, restarting:")
    cycle_from_dweet()

def execution(location):
  if location == "stop":
    ...
  else:
    ...
  cycle_from_dweet()

cycle_from_dweet()