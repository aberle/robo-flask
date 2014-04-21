from flask import Flask, request
app = Flask(__name__)

@app.route('/go/')
@app.route('/go/<feet>')
def go(feet = None):
    if feet == None:
        return 'No argument specified, please try again'

    # 1 foot is about 2 seconds on slow speed
    pause = int(feet) * 2000

    return "; Drive forward for "+feet+" feet<br>"\
            +"forward A<br>"\
            +"forward B<br>"\
            +"pause " + str(pause)\
            +"<br>halt A <br> halt B"



@app.route('/square/')
@app.route('/square/<feet>')
def square(feet = None):
    if feet == None:
        return 'No argument specified, please try again'

    # 1 foot is about 2 seconds on slow speed
    pause = int(feet) * 2000

    return "main:<br>"\
            +"; Set Motor Speed Low<br>"\
            +"output C.5<br><br>"\
            +"; Drive forward " +feet+" feet<br>"\
            +"forward A<br>"\
            +"forward B<br>"\
            +"pause + "+str(pause)+"<br><br>"\
            +"; Right turn<br>"\
            +"goto doRight<br>"\
            +"halt A<br>"\
            +"halt B<br><br>"\
            +"doRight:<br>"\
            +"halt A<br>"\
            +"halt B<br>"\
            +"forward A<br>"\
            +"pause 1000<br>"\
            +"halt A<br>"\
            +"goto main<br>"

if __name__ == '__main__':
    app.run(debug=True)