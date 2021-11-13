from flask import Flask, render_template
  
# Setting up the application
app1 = Flask(__name__)
  
# making route
  
@app1.route('/')
def home():
    return render_template('home.html')


@app1.route('/start/')
def chose_start():
    return render_template('chose_start.html')  



  
# running application
if __name__ == '__main__':
    app1.run(debug=True)