from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route('/add/',methods=['GET',"POST"])
def add():
    args = request.args
    url = request.url
    le = len(url)
    try: 
        s = sum(list(map(float,args.values())))

        return jsonify({"url":url,"char":le,"sum":s,'data':args})
    except:
        return jsonify({"url":url,"char":le,"error":"Please give numbers as value","data":args})


if __name__=='__main__':
    app.run(debug=True)