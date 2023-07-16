from bible import Bible
from mail import Mail
import time, os, json
from dotenv import load_dotenv

load_dotenv()

b = Bible()
m = Mail(os.getenv("MAIL"), os.getenv("PWD"))
i = 0
rec = os.getenv("REC")
rcp = json.loads(os.getenv("RCP"))

print(rcp)
while True: 
    i += 1
    data = b.get_vers()

    message = f""" 
Vers: {data[0]} 

Dieses Zitat steht in: {data[1]}.
""".replace("ä", "ae").replace("ö", "oe").replace("ü", "ue").replace("ß", "ss")

    print(f"{i}. " , m.sendEmail(rcp, rec, message))
    time.sleep(86400)

