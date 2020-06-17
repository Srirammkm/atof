from flask import Flask,request,render_template
from fscraper import find_productF
from ascraper import find_productA

app = Flask(__name__)
@app.route('/', methods=['GET','POST'])
def product():
    search = ''
    dic1 = []
    dic2 = []
    if request.method == 'POST' and 'pro' in request.form:
        search = request.form.get('pro')
        dic1=find_productF(search)
        dic2=find_productA(search)
    return render_template("index.html",
                            dic1=dic1,dic2=dic2)
app.run()