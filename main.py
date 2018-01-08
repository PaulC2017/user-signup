from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too


@app.route("/")
def index():
  return render_template("sign_up.html")

@app.route("/Reqs", methods = ["GET", "POST"])
def reqs():
  return render_template("input_req.html")

def check_user_name(un):
    
   if un == "":
     return False
   elif un.count(" ") != 0:
     return False
   elif len(un) < 3 or len(un) > 20:
     return False

def check_pass_word(pw ):
    
   if pw == "":
     return False
   elif pw.count(" ") != 0:
     return False
   elif len(pw) < 3 or len(pw) > 20:
     return False
    
def verify_pass_word(vpw,pw):  
    if pw == vpw:
      return True
    else:
       return False

def verify_email(em):
    if em.count(" ") != 0 or em.count("@") != 1 or em.count(".") != 1:
      return False
    elif len(em) < 3 or len(em) > 20:
      return False
    
     

@app.route("/Add",methods =["GET","POST"])
def sign_up():
     input_error = False
     un_message = ""
     pw_message = ""
     vp_message = ""
     em_message = ""
     user_Name = cgi.escape(request.form["user_name"], quote = True)
     p_Word = request.form["p_word"]
     ver_P_Word = request.form["ver_password"]
     e_Mail = request.form["e_mail"]
     
     if check_user_name(user_Name) == False:
         un_message =  "That is not a valid username"
         
         input_error = True

     if check_pass_word(p_Word ) == False:
         pw_message =     "That is not a valid password"
         input_error = True
     
     if verify_pass_word(p_Word, ver_P_Word) == False:
         vp_message =   "The passwords do not match"
         input_error = True

     if e_Mail != "":
     
         if verify_email(e_Mail) == False:
             em_message =   "That is not a valid email"
             input_error = True


     if input_error:
         
         return render_template("sign_up.html" , un_error = un_message, pw_error = pw_message, vp_error = vp_message,   em_error = em_message, uName = user_Name, eMail = e_Mail )
     else:
         
        welcome_message = "Welcome " + user_Name

        return  render_template("welcome.html", hello = welcome_message)



app.run()