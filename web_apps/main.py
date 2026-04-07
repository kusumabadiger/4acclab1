from flask import Flask,render_template
app=Flame(__name__)
@app_route("/")
def home():
  return render_template('index.html',title="Home page")
if __name__=='__main__':
  app.run(host='',port=8080,debug=True)
