from os import wait

from utilities import launchMenu, launch_place_firefox, press_key, reset_place_firefox, resizeAndPlace, startRoutine, switchToWindow, translate, sync_input, vladi_mir_cache
from flask import Flask, render_template, request, redirect, Blueprint
import time
import chartkick
import random as rd
import subprocess as sp
from pynput.keyboard import Controller
from datetime import datetime
import re
import time
app = Flask(__name__)
ck = Blueprint('ck_page', __name__, static_folder=chartkick.js(), static_url_path='/static')
app.register_blueprint(ck, url_prefix='/ck')
app.jinja_env.add_extension("chartkick.ext.charts")

BASE_INPUTS = {"up":0, "down":0, "right":0, "left":0, "a":0, "b":0}
inputs_ana = BASE_INPUTS
inputs_demo = BASE_INPUTS

DEMO_VOTING_TIME = 5    
ANAR_VOTING_TIME = 5

timer=time.perf_counter()

kbd = Controller()
widFirefox = 0


logs = open("logs.txt", "a")

#Lance un émulateur et echo son Process ID
terminal1 = sp.Popen('mgba Pokemon/saphir.gba & echo $!', shell=True, stdout=sp.PIPE)
#Récupère le PID qui vient de se faire echo, c'est essentiel pour pouvoir changer le focus sur la fenêtre
pidAnarchy = re.sub("[^0-9]","", str(terminal1.stdout.readline()))
print(pidAnarchy)
#
terminal2 = sp.Popen('mgba Pokemon/saphir.gba & echo $!', shell=True, stdout=sp.PIPE)
pidDemocracy = re.sub("[^0-9]","", str(terminal2.stdout.readline()))
print(pidDemocracy)
time.sleep(2)
resizeAndPlace(pidAnarchy, pidDemocracy)
time.sleep(5)


demo_percentages = {}
ana_percentages = {}

ana_cache = []
demo_cache = []

cache_size=5

@app.route('/democracy', methods=['POST', 'GET'])
@app.route('/numerik/democracy', methods=['POST', 'GET'])
def democracy():
        global timer
        global inputs_demo
        global demo_percentages
        global demo_cache
        
        
        total_votes = sum(inputs_demo.values())
        demo_percentages = inputs_demo
 
        if total_votes:
                demo_percentages=  {k: round(v/total_votes*100,1) for k,v in inputs_demo.items()}


        print(timer-time.perf_counter())
        if (time.perf_counter()-timer)>DEMO_VOTING_TIME:
                vote_res = max(inputs_demo.keys(), key=(lambda key: inputs_demo[key]))
                inputs_demo = inputs_demo.fromkeys(inputs_demo, 0) 
                timer=time.perf_counter()
                press_key(pidDemocracy, kbd, translate(str(vote_res)))
                vladi_mir_cache(demo_cache, (str(vote_res), demo_percentages[vote_res]), cache_size)
                print("Democracy VOTE RESULT",(str(vote_res), demo_percentages[vote_res]))
                logs.write("Democracy : "+str(datetime.now())+" : "+str(vote_res) +" "+ str(demo_percentages[vote_res]) +"%\n")
                logs.flush()


        if request.method== 'POST':
                inputs_demo[request.form['controller']]+=1
                print(inputs_demo)
                return redirect('/numerik/democracy')
        else:
                return render_template("democracy.html", percentages=demo_percentages)

@app.route('/anarchy', methods=['POST', 'GET'])
@app.route('/numerik/anarchy', methods=['POST', 'GET'])
def anarchy():
        global timer
        global inputs_ana
        global ana_percentages
        global ana_cache
        print(timer-time.perf_counter())

        total_votes = sum(inputs_ana.values())
        ana_percentages= inputs_ana
 
        if total_votes:
                ana_percentages=  {k: round(v/total_votes*100,1) for k,v in inputs_ana.items()}

        if (time.perf_counter()-timer)>ANAR_VOTING_TIME:
                all_votes = sorted(([k]*v for k,v in inputs_ana.items()))
                print("All votes ", all_votes)
                flat_votes = []
                for line in all_votes:
                        for val in line:
                                flat_votes+=[val]
                if len(flat_votes):
                        vote_res= rd.sample(flat_votes, 1)
                        inputs_ana = inputs_ana.fromkeys(inputs_ana, 0) 
                        timer=time.perf_counter()
                        press_key(pidAnarchy, kbd, translate(str(vote_res[0])))
                        vladi_mir_cache(ana_cache, (str(vote_res[0]), ana_percentages[vote_res[0]]), cache_size)
                        print("Anarchy VOTE RESULT",(str(vote_res[0]), ana_percentages[vote_res[0]]))
                        logs.write("Anarchy : "+str(datetime.now())+" : "+str(vote_res) +" "+ str(ana_percentages[vote_res[0]]) +"%\n")
                        logs.flush()


        if request.method== 'POST':
                inputs_ana[request.form['controller']]+=1
                print(inputs_ana)
                return redirect('/numerik/anarchy')
        else:
                return render_template("anarchy.html")


@app.route("/stats", methods=['POST', 'GET'])
@app.route("/numerik/stats", methods=['POST', 'GET'])
def stats():
        global demo_percentages
        global ana_percentages
        global ana_cache
        global demo_cache

        return render_template("stats.html", ana_percentages=ana_percentages, demo_percentages=demo_percentages, ana_cache=ana_cache, demo_cache=demo_cache)


@app.route("/admin", methods=['POST', 'GET'])
@app.route("/numerik/admin", methods=['POST', 'GET']) #CHANGE
def admin():
        global widFirefox
        if request.method== 'POST':
                if request.form['controller'] == "place":
                        print("place")
                        resizeAndPlace(pidAnarchy, pidDemocracy)
                elif request.form['controller'] == "firefox":
                        widFirefox = launch_place_firefox()
                elif request.form['controller'] == "resetfirefox":
                        widFirefox = reset_place_firefox(widFirefox)
                else:
                        sync_input(pidAnarchy,pidDemocracy,kbd, translate(request.form['controller']))
        return render_template("admin.html")




@app.route('/', methods=['POST', 'GET'])
@app.route('/numerik', methods=['POST', 'GET'])
@app.route('/numerik/', methods=['POST', 'GET'])
def index():
        if request.method == 'POST':
                return redirect('/numerik/'+request.form['mode'])
        else:
                return render_template("index.html")



if __name__  == "__main__":
    app.run(debug=True)