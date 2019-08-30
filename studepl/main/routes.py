from flask import render_template, request, Blueprint

main = Blueprint('main', __name__)

th = "Rappels théoriques"
ms = "Énoncé de la mission"
cr = "Correctif de la mission"

@main.route("/")
@main.route("/home")
def home():
    return render_template('layout.html')

@main.route("/margaux")
def margaux():
    return render_template('margaux.html')



@main.route("/s1_theorie")
def s1_theorie():
    return render_template('S1/theorie.html', title=th, week='1')
@main.route("/s1_mission")
def s1_mission():
    return render_template('S1/mission.html', title=ms, week='1')
@main.route("/s1_correctif")
def s1_correctif():
    return render_template('S1/correction.html', title=cr, week='1')


@main.route("/s2_theorie")
def s2_theorie():
    return render_template('S2/theorie.html', title=th, week='2')
@main.route("/s2_mission")
def s2_mission():
    return render_template('S2/mission.html', title=ms, week='2')
@main.route("/s2_correctif")
def s2_correctif():
    return render_template('S2/correction.html', title=cr, week='2')


@main.route("/s3_theorie")
def s3_theorie():
    return render_template('S3/theorie.html', title=th, week='3')
@main.route("/s3_mission")
def s3_mission():
    return render_template('S3/mission.html', title=ms, week='3')
@main.route("/s3_correctif")
def s3_correctif():
    return render_template('S3/correction.html', title=cr, week='3')


