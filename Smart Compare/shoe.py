from flask import Flask, render_template, request, jsonify
import RPi.GPIO as GPIO
import time
app = Flask(__name__)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.IN) 
GPIO.setup(11,GPIO.IN)

@app.route("/sensor")
def sensor():
	if(GPIO.input(7)==0 and GPIO.input(11)==0):
		state = "shoes"
	elif(GPIO.input(7)==1 and GPIO.input(11)==0): 
		state  = "nike"
	elif(GPIO.input(7)==0 and GPIO.input(11)==1): 
		state  = "puma"	
	else:
		state = "compare"
	
	return jsonify(sensorState=state)


@app.route("/shoes")
def home():
	templateData={
             'title' : 'SHOES UP'            
	}		    
	return render_template('home.html', **templateData)	
  
@app.route("/nike")
def nike():
	templateData={
             'title' : 'SHOES UP'            
	}	    
	return render_template('nike.html', **templateData)

@app.route("/puma")
def puma():
	templateData={
             'title' : 'SHOES UP'            
	}	    
	return render_template('puma.html', **templateData)	

@app.route("/compare")
def compare():
	templateData={
             'title' : 'SHOES UP'            
	}	    
	return render_template('compare.html', **templateData)
	

  
if __name__ == "__main__":
	app.run(host='10.0.0.107', port=80, debug=True)
