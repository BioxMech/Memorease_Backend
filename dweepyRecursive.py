def cycle_from_dweet():
        try:
            for dweet in dweepy.listen_for_dweets_from('memorease'):
                print("Listening to updates from dweet thing 'memorease'...")
                print(dweet)

        except requests.exceptions.ConnectionError as e:
            print(e.response)
            print("Connection closed by dweet, restarting:")
            cycle_from_dweet()
