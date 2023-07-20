from flask import Flask, request, render_template, redirect, flash, jsonify, session
from flask_debugtoolbar import DebugToolbarExtension
from random import randint, choice, sample


app = Flask(__name__)

app.config['SECRET_KEY'] = "123"
app.debug= True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
# debug = DebugToolbarExtension(app)

MOVIES = {'Amadeus', 'Monsters Inc', 'Chicken Run'}

@app.route('/')
def hello():
    """shows home page"""
    return render_template("hello.html")
    
@app.route('/old-home-page')
def redirect_to_home():
    """redirects to the new home page"""
    flash('this is the new home page!!', "error")
    return redirect('/') 


@app.route('/movies')
def show_movies():
    """returns a list of movies in fake DB"""
    
    return render_template('movies.html', movies=MOVIES)

@app.route('/movies/new', methods=["POST"])
def add_movies():
    title = request.form['title']
    #add to pretend DB
    if title in MOVIES:
        flash('Movie already exists', 'error')
    else:
        MOVIES.add(title)
        flash('created your movie!!')
        
    # import pdb
    # pdb.set_trace()
    return redirect('/movies')

@app.route('/movies/json')
def movies_json():
    movies = list(MOVIES)
    raise
    return jsonify(movies)
    
@app.route('/form')
def show_form():
    return render_template("form.html")

@app.route('/form-2')
def form_2():
    return render_template("form_2.html")


COMPLIMENTS = ["cool", "clean", "clever", "awesome"]
@app.route('/greet')
def show_greet():
    username = request.args['username']
    nice_thing = choice(COMPLIMENTS)
    return render_template("greet.html", username=username, compliment=nice_thing)

@app.route('/greet-2')
def greet2():
    username = request.args['username']
    checkbox = request.args.get('wants_compliments')
    nice_things = sample(COMPLIMENTS, 3)
    return render_template('greet_2.html', username=username, wants_compliments=checkbox, compliments=nice_things)
    

@app.route('/lucky')
def lucky_num():
    number = randint(1,20)
    return render_template("lucky.html", lucky_num=number)

@app.route('/spell/<word>')
def spell_word(word):
    caps = word.upper()
    return render_template("spell_word.html", word=caps)

@app.route('/project')
def startLogin():
    return render_template("project.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/main_page')
def show_home():
    return render_template("home.html")

@app.route('/somer-route')
def some_route():
    """ set fav_number in session"""
    print("***********SESSION***************")
    print(session['fav_number'])
    # session['fav_number'] = 42
    # session['leaderboard'] = ['first', 'second', 'third']
    return render_template("hello.html")

#cookies would be set as follows
# html = render_template  response=make_response(html)  response.set_cookie('userID', user) return response

