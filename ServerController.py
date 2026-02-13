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




# Subscriber Model Onboarding 
# Intergrates Clients To Customer Base List  
# Should Have A Db Impl of Storing  Reg - Subscribers 
class Onboarding_Platform(View): 
    methods = ['GET', 'POST']  

    def dispatch_request(self) -> str :
      
    
        if request.method == 'POST':
            EmailAddress = request.form.get("Email")
            Phone = request.form.get("Contact")
            Subject = """ Thank you for joining Osefa homes & Developers . You registered with phone [ {0} ] . Kindly usse that to log in """.format(Phone)
            Body = """ Welcome to Osefa Homes & Devs  """ 
          
            base.Create_Email(EmailAddress , Subject , Body)
            return redirect(url_for('Home' , CompanyID = CompanyID , Info = Info  ))

        else: 
            # Return requested profile thru client connect 
            return redirect(url_for('Home' , CompanyID = CompanyID , Info = Info  , ))




# Contact Us Master Form Submission Protocol
# Relays Feedback Thru Email After Supply Of Neck Creds




# Base Route Address For Campaign/Landing Page Scenarios 
# Initial Page 
class Dash_Page_Context(View):
   methods = ['GET']  
   def Render_Year(self):
        Current_Year = str(2025)
        return Current_Year

   def dispatch_request(self) -> str :
        
        YEAR = self.Render_Year()
        if request.method == 'GET':
            return render_template("Company_Display_Profile.html" , CompanyID = CompanyID  , YEAR = YEAR  )
        else: 
            # Return requested profile thru client connect 
            return render_template("Company_Display_Profile.html" , CompanyID = CompanyID , YEAR = YEAR   )
        



# Registering App Urls Routes 
# (1 - Campaign Route Company Portal )
app.add_url_rule('/', view_func=Dash_Page_Context.as_view('Home'))


if __name__=='__main__':
   app.run(host="0.0.0.0" , debug="False" )
    
