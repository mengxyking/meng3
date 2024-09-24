from flask import Flask
from flask import Flask,redirect,url_for,request
count = 0
app = Flask(__name__)

@app.route("/hello/<name>")
def hello_wolrd(name):
    addr = request.args.get("addr")
    print(addr)
    #flask_dem.addAddr(addr)
    return "wolrd=%s"%addr

@app.route("/aaa")
def hello_wolrd1():
    global count
    count += 1
    print(count)
    return "hello wolrd:"+str(count)

@app.route('/blog/<int:postID>')
def show_blog(postID):
    return 'Blog Number %d' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
    return 'Revision Number %f' % revNo




if __name__ == "__main__":
    app.run(debug=True)



