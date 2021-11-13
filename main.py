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

@app1.route('/R1/')
def R1():
    return render_template('R1.html') 

@app1.route('/L1/')
def L1():
    return render_template('L1.html') 


  
# running application
if __name__ == '__main__':
    app1.run(debug=True)