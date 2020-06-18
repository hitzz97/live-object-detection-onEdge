from flask import Flask, render_template, redirect, url_for, request, jsonify,Response,send_file
import os,sys
import pandas as pd 

app = Flask(__name__)
# PORT = int(os.getenv('PORT', 8000))
data = pd.read_csv("dataBase.csv")
@app.route("/api",methods=['GET'],)    
def api():
	try:
		age_group = [10,20,30,40,50]
		dress = request.args.get('type')
		color = request.args.get('color')
		gender = request.args.get('gender')
		age = request.args.get('age')
		for i in age_group: 
			if i>=int(age): 
				grp=i
				break
		else:
			grp=50
		print(dress,color,gender,age,grp)
		images=data[data['type']==dress][data['color']==color][data['gender']==gender][data['age']==grp]['image']
		images=['/static/'+i for i in images]
		valid=[i for i in images if os.path.isfile(i)]
		return " ".join(images)
	except Exception as e:
		return str(e)

@app.route("/per_rec",methods=['GET'],)
def per_rec():                               #returns dress urls matching to the required parameters 
	try:
		dress = request.args['type']
		color = request.args['color']
		print(dress,color)
		images=list(data[data['type']==dress][data['color']==color]['image'])
		images=['/static/'+i for i in images]
		print(images[:5])
		valid=[i for i in images if os.path.isfile('.'+i)]
		print(len(valid))
		return " ".join(valid)
	except Exception as e:
		return str(e)

@app.route("/rec",methods=['GET'])            #returns similar electronics products(HARD CODED FOR PHONES ONLY)
def rec():
	try:
		files = []
		files.extend(os.listdir('./static/cell_phone/'))
		return " ".join(["/static/cell_phone/"+i for i in files])
	except:
		return "Failed";
		
@app.route("/getpara",methods=['POST'])           
def getf():                                     #returns the model to detect dress
	file = open('./static/model.json','r')
	text = file.read()
	return text

@app.route("/",methods=['GET','POST'])
def page():
    try:
        return render_template('test.html')
        # return "worked"
    except Exception as e:
        return "ERROR: "+str(e)

if __name__ == '__main__':
	app.run()

# app.run(host='0.0.0.0',port=PORT)