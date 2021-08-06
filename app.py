from flask import Flask, render_template, request, redirect, Blueprint
import time
import chartkick
import random as rd
import subprocess as sp


app = Flask(__name__)
ck = Blueprint('ck_page', __name__, static_folder=chartkick.js(), static_url_path='/static')
app.register_blueprint(ck, url_prefix='/ck')
app.jinja_env.add_extension("chartkick.ext.charts")

BASE_INPUTS = {"up":0, "down":0, "right":0, "left":0, "a":0, "b":0}
inputs = BASE_INPUTS
DEMO_VOTING_TIME = 8
ANAR_VOTING_TIME = 2
timer=time.perf_counter()

sp.run('mgba /home/lucastrg/Desktop/Pokemon/saphir.gba', shell=True)


@app.route('/democracy', methods=['POST', 'GET'])
def democracy():
        global timer
        global inputs
        print(timer-time.perf_counter())
        if (time.perf_counter()-timer)>DEMO_VOTING_TIME:
                vote_res = max(inputs.keys(), key=(lambda key: inputs[key]))
                print("Democracy VOTE RESULT", vote_res)
                inputs = inputs.fromkeys(inputs, 0) 
                timer=time.perf_counter()
                sp.run('echo "$key"', shell=True, env={'key': vote_res})


        total_votes = sum(inputs.values())
        percentages = inputs
 
        if total_votes:
                percentages=  {k: round(v/total_votes*100,1) for k,v in inputs.items()}


        if request.method== 'POST':
                inputs[request.form['controller']]+=1
                print(inputs)
                return redirect('/democracy')
        else:
                return render_template("democracy.html", percentages=percentages)


@app.route('/anarchy', methods=['POST', 'GET'])
def anarchy():
        global timer
        global inputs
        print(timer-time.perf_counter())
        if (time.perf_counter()-timer)>ANAR_VOTING_TIME:
                all_votes = sorted(([k]*v for k,v in inputs.items()))
                print("All votes ", all_votes)
                flat_votes = []
                for line in all_votes:
                        for val in line:
                                flat_votes+=[val]
                if len(flat_votes):
                        vote_res= rd.sample(flat_votes, 1)
                        print("Anarchy VOTE RESULT",vote_res)
                        sp.run('echo "$key"', shell=True, env={'key': str(vote_res[0])})
                        inputs = inputs.fromkeys(inputs, 0) 
                        timer=time.perf_counter()


        total_votes = sum(inputs.values())
        percentages= inputs
 
        if total_votes:
                percentages=  {k: round(v/total_votes*100,1) for k,v in inputs.items()}


        if request.method== 'POST':
                inputs[request.form['controller']]+=1
                print(inputs)
                return redirect('/anarchy')
        else:
                return render_template("anarchy.html", percentages=percentages)







@app.route('/', methods=['POST', 'GET'])
def index():
        if request.method == 'POST':
                return redirect('/'+request.form['mode'])
        else:
                return render_template("index.html")



if __name__  == "__main__":
    app.run(debug=True)