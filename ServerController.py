import asyncio
from flask import Flask , url_for , render_template , request , redirect , send_from_directory
from jinja2 import Environment , FileSystemLoader
from flask.views import View
from flask import g
import os , random , string 
import time
from flask_cors import CORS 
import uuid
import datetime




#import Twilio_Content_Provider as Twilio_Service
app=Flask(__name__)
#sslify = SSLify(app)
app.config.update(
    PERMANENT_SESSION_LIFETIME = 600 ,
)
cors = CORS(app , resources = {r"/*" : {"origins" : "*" }})



# Erro Handler Protocol Environs 
# Auto Redirect To 404.Html 
@app.errorhandler(404)
# inbuilt function which takes error as parameter
def not_found(error):
  return render_template("404.html" , error = error)

CompanyID = "PointCare"




class Company_Display_Profile(View):
   methods = ['GET']  
   def dispatch_request(self) -> str :
        CompanyID = "DensoTechnologies"
        if request.method == 'GET':
            return render_template('Company_Display_Profile.html' , CompanyID = CompanyID  )
        else: 
            # Return requested profile thru client connect 
            return render_template('Company_Display_Profile.html' , CompanyID = CompanyID  )
        





app.add_url_rule('/', view_func=Company_Display_Profile.as_view('Home'))



if __name__=='__main__':
   app.run(host="0.0.0.0" , debug="False" )
    