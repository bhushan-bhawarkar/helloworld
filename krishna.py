from flask import Flask
prabhu = Flask(__name__)

@prabhu.route('/Company_Name')
def Company_Name():
  return "ABC Corporation"

@prabhu.route('/Location')
def  Location():
  return "India"
@prabhu.route('/Contact_Detail')
def Contact_Detail():
  return "999-999-9999"

if __name__ == "__main__":
  prabhu.run(host="0.0.0.0")
