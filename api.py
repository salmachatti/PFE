from flask import Flask, request
from datetime import datetime

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/sql', methods=['POST'])
def home():
   cont = request.json
   with open("data.csv","a+") as fo:
      current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
      x = cont["temperature"]
      fo.write("%s;%s\n"%(current_time,x))
   return({"status":200})

app.run(host="192.168.100.19",port=1234)

