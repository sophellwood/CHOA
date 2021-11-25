from flask import Flask, render_template, jsonify
  
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

@app1.route('/L2/')
def L2():
    return render_template('L2.html') 

@app1.route('/L3/')
def L3():
    return render_template('L3.html') 

@app1.route('/L4/')
def L4():
    return render_template('L4.html') 

@app1.route('/L3R1/')
def L3R1():
    return render_template('L3R1.html') 

@app1.route('/L1R1/')
def L1R1():
    return render_template('L1R1.html') 

@app1.route('/L1R1L1/')
def L1R1L1():
    return render_template('L1R1L1.html') 

@app1.route('/L1R1L1M1/')
def L1R1L1M1():
    return render_template('L1R1L1M1.html') 

@app1.route('/L1R2/')
def L1R2():
    return render_template('L1R2.html') 

@app1.route('/L1R2L1/')
def L1R2L1():
    return render_template('L1R2L1.html') 

@app1.route('/L1R2L2/')
def L1R2L2():
    return render_template('L1R2L2.html') 

@app1.route('/L1R2L3/')
def L1R2L3():
    return render_template('L1R2L3.html') 

@app1.route('/L1R2L1R1/')
def L1R2L1R1():
    return render_template('L1R2L1R1.html') 

@app1.route('/L1R3/')
def L1R3():
    return render_template('L1R3.html') 

@app1.route('/L1R3L1/')
def L1R3L1():
    return render_template('L1R3L1.html') 

@app1.route('/L1R4/')
def L1R4():
    return render_template('L1R4.html') 

@app1.route('/L1R4L1/')
def L1R4L1():
    return render_template('L1R4L1.html') 

@app1.route('/L1R4M1/')
def L1R4M1():
    return render_template('L1R4M1.html') 
 
@app1.route('/L1R5/')
def L1R5():
    return render_template('L1R5.html') 
   
@app1.route('/L1R5L1/')
def L1R5L1():
    return render_template('L1R5L1.html') 
  
@app1.route('/L1R5M1/')
def L1R5M1():
    return render_template('L1R5M1.html') 
 
@app1.route('/L1R6/')
def L1R6():
    return render_template('L1R6.html') 
  
  
@app1.route('/L1R6L1/')
def L1R6L1():
    return render_template('L1R6L1.html') 
  
@app1.route('/L1R6M1/')
def L1R6M1():
    return render_template('L1R6M1.html') 
 
@app1.route('/L1R7/')
def L1R7():
    return render_template('L1R7.html') 
  
@app1.route('/L1R7L1/')
def L1R7L1():
    return render_template('L1R7L1.html') 
  
@app1.route('/L1R7M1/')
def L1R7M1():
    return render_template('L1R7M1.html') 
 
@app1.route('/L1R8/')
def L1R8():
    return render_template('L1R8.html') 
  
@app1.route('/L1R7L2/')
def L1R7L2():
    return render_template('L1R7L2.html') 
 

  
@app1.route('/L1R8L1/')
def L1R8L1():
    return render_template('L1R8L1.html') 
  
#Ending Options 


  
@app1.route('/L1R7M1L1/')
def L1R7M1L1():
    return render_template('L1R7M1L1.html') 
  
@app1.route('/L1R7M1R1/')
def L1R7M1R1():
    return render_template('L1R7M1R1.html') 

@app1.route('/L1R9/')
def L1R9():
    return render_template('L1R9.html')

@app1.route('/L1R8L2/')
def L1R8L2():
    return render_template('L1R9.html')

@app1.route('/L1R8L1R1/')
def L1R8L1R1():
    return render_template('L1R8L1R1.html')

@app1.route('/L1R7L1R1/')
def L1R7L1R1():
    return render_template('L1R7L1R1.html')

@app1.route('/L1R7L1R1L1/')
def L1R7L1R1L1():
    return render_template('L1R7L1R1L1.html')

@app1.route('/L1R7L1R1M1/')
def L1R7L1R1M1():
    return render_template('L1R7L1R1M1.html')

@app1.route('/L1R7L1R2/')
def L1R7L1R2():
    return render_template('L1R7L1R2.html')
    


@app1.route('/GameOver/')
def GameOver():
    return render_template('GameOver.html')


  
# running application
if __name__ == '__main__':
    app1.run(debug=True)
