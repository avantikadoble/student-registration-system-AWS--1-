from flask import Flask ,render_template, request
import boto3 
import mysql.connector 
app = Flask(__name__)
db =mysql.connector.connect(
   host="localhost",
   user="root",
   password="",
   database="student_registration"
)
s3 = boto3.client("s3")
@app.route("/")
def home():
    return render_template("home.html")
@app.route("/registration",methods=["POST"])
def register():
   name = request.form["name"]
   student_class = request.form["class"]
   section = request.form["section"]
   gender = request.form["Gender"]
   email = request.form["email"]
   phone = request.form["number"]
   document = request.files["file"]
   s3.upload_fileobj(document ,"student-registration-avantika-2026","documents/"+document.filename)
   photo = request.files["photo"]
   s3.upload_fileobj(photo ,"student-registration-avantika-2026","photos/"+photo.filename)
   cursor = db.cursor()
   sql = """
   INSERT INTO students(name,student_class,section,gender,email,phone,document_name,photo_name)
   values(%s,%s,%s,%s,%s,%s,%s,%s)
   """ 
   values = (name,student_class,section,gender,email,phone,document.filename,photo.filename)
   cursor.execute(sql,values)
   db.commit()
   cursor.close()
   return f""" 
   Name :{name}<br>
   Class : {student_class}<br>
   Section:{section}<br>
   Gender:{gender}<br>
   
   Email:{email}<br>
   Phone:{phone}<br>
   Document:{document.filename}<br>
   Photo:{photo.filename}<br>
   """
   
   
if __name__ == "__main__" :
 app.run(debug=True)
 