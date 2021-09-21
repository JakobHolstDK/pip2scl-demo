import flask
print(flask.__version__)
from flask import Flask

app = Flask(__name__)

body = ["Versions<HR>"]
body.append("<TABLE>")
body.append("<TR><TH>Module</TH><TH>Version</TH></TR>")

f = open("requirements.txt", "r")
for line in f:
    module = line.split("==")[0]
    version = line.split("==")[1]
    body.append("<TR><TD>%s</TD><TD>%s</TD></TR>" % ( module, version ))
body.append("</TABLE>")
body.append("<HR>EOM")
body = ''.join(body)

@app.route('/')
def versions():
    return body
