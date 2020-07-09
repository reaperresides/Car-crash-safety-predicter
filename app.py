from flask import Flask,render_template,request,redirect
import pickle
import numpy as np



app=Flask(__name__)


@app.route("/",methods=["GET","POST"])
def Home():    
    if request.method=="POST":  
        predicter=[val for val in request.form.values()]
        predicter_data=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        if predicter[0]=="low":predicter_data[0]=1
        if predicter[0]=="med":predicter_data[1]=1
        if predicter[0]=="high":predicter_data[0]=0;predicter_data[1]=0;predicter_data[2]=0
        if predicter[0]=="v-high":predicter_data[2]=1

        if predicter[1]=="low":predicter_data[3]=1
        if predicter[1]=="med":predicter_data[4]=1
        if predicter[1]=="high":predicter_data[3]=0;predicter_data[4]=0;predicter_data[5]=0
        if predicter[1]=="v-high":predicter_data[5]=1

        if int(predicter[2])==3:predicter_data[6]=1
        if int(predicter[2])==4:predicter_data[7]=1
        if int(predicter[2])>4:predicter_data[8]=1
        if int(predicter[2])==2:predicter_data[6]=0;predicter_data[7]=0;predicter_data[8]=0

        if int(predicter[3])==4:predicter_data[9]=1
        if int(predicter[3])>4:predicter_data[10]=1
        if int(predicter[3])==2:predicter_data[9]=0;predicter_data[10]=0
            
        if predicter[4]=="med":predicter_data[11]=1
        if predicter[4]=="small":predicter_data[12]=1
        if predicter[4]=="big":predicter_data[11]=0;predicter_data[12]=0

        if predicter[5]=="med":predicter_data[13]=1
        if predicter[5]=="low":predicter_data[14]=1
        if predicter[5]=="high":predicter_data[13]=0;predicter_data[14]=0

        data=np.array(predicter_data)
        model=pickle.load(open("carpred.pkl","rb"))
        predicted_result=model.predict(data.reshape(1,-1))
        return render_template("result.html",posts=predicted_result)
    else:
        return render_template("home1.html")





if __name__=="__main__":
    app.run(debug=1)

