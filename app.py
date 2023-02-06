from flask import Flask,render_template,url_for

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/resume")
def resume():
    return render_template("resume.html")
@app.route("/video")
def video():
    return render_template("video.html")
@app.route("/bank")
def bank():
    return url_for("/bank")



if __name__=="__main__":
    app.run(debug=True)