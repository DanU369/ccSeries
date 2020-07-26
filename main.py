from datetime import datetime
from flask import Flask, render_template, url_for, request, session, redirect, flash, Blueprint,jsonify

from data import queries


app = Flask('codecool_series')
app.secret_key = queries.random_api_key()


@app.route('/')
def index():
    shows = queries.get_shows()
    return render_template('index.html', shows=shows)



@app.route('/design')
def design():
    return render_template('design.html')


@app.route('/addComment',methods=['POST'])
def addComment():
    comment=request.form['comment']
    username=session['user_id']
    movie_id=request.form['movieID']
    queries.addComment(username,movie_id,comment)
    return redirect("http://127.0.0.1:8001/tv-show/"+movie_id, code=302)

@app.route('/tv-show/<id>/<commID>/edit',methods=['GET','POST'])
def edit(id,commID):
    if request.method=="POST":
        comment=request.form['comment']
        queries.updateComment(commID,comment)
        return redirect('/tv-show/'+id)
    comment=queries.getCOmmentByID(commID)
    return render_template('edit.html',id=id,commID=commID,comment=comment)

@app.route('/tv-show/<id>/<commID>/delete',methods=['GET'])
def deleteComm(id,commID):
    queries.deleteComment(commID)
    return redirect('/tv-show/'+id)

@app.route('/favorites',methods=['GET'])
def favorites():
    data=queries.getFavorites(session['user_id'])
    return render_template('favorites.html',data=data)

@app.route('/tv-show/<id>',methods=['GET','POST'])
def show_by_id(id):
    if request.is_json and request.method=='POST':
        data = request.get_json()
        queries.addFav(data,session['user_id'])
        data='string'
        return jsonify(data)
    top_3_actors=queries.getTopActors(id)
    print(top_3_actors)
    comments=queries.getComment(id)
    genres = queries.show_genre(id)
    show = queries.get_show_by_id(id)
    try:
        check=len(queries.checkFav(show[1],session['user_id']))
    except:
        check=0
    return render_template('tv-show-id.html',comments=comments, show=show, genres=genres, check=check,top_3_actors=top_3_actors)


@app.route("/shows/most-rated/<pgNumber>/sortBy/<sort>/<order>", methods=['GET'])
def sorting(pgNumber,sort,order):
    pgNumber=int(pgNumber)
    offsetNr = (pgNumber - 1) * 15
    most_rated_15_shows = queries.get_last_15_rated_shows(offsetNr)
    if sort =='title':
        if order =='asc':
            data = sorted(most_rated_15_shows, key=lambda k: k['title'])

        else:
            data = sorted(most_rated_15_shows, key=lambda k: k['title'],reverse=True)
    elif sort =='releaseYear':
        if order =='asc':
            data = sorted(most_rated_15_shows, key=lambda k: k['year'])

        else:
            data = sorted(most_rated_15_shows, key=lambda k: k['year'],reverse=True)
    elif sort =='runtime':
        if order == 'asc':
            data = sorted(most_rated_15_shows, key=lambda k: k['runtime'])

        else:
            data = sorted(most_rated_15_shows, key=lambda k: k['runtime'],reverse=True)
    elif sort =='rating':
        if order == 'asc':
            data = sorted(most_rated_15_shows, key=lambda k: k['rating'])

        else:
            data = sorted(most_rated_15_shows, key=lambda k: k['rating'],reverse=True)
    elif sort == 'genres':
        if order == 'asc':
            data = sorted(most_rated_15_shows, key=lambda k: k['genres'])

        else:
            data = sorted(most_rated_15_shows, key=lambda k: k['genres'],reverse=True)
    return render_template("most-rated.html",pgNumber=pgNumber, most_rated_15_shows=data,sort=sort,order=order)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if 'user_id' in session:
        return redirect(url_for("index"))
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        submission_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if queries.register_user(username, password, submission_time) is False:
            flash('Not registered')
        queries.register_user(username, password, submission_time)
        return redirect(url_for("login"))
    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user_id' in session:
        return redirect(url_for("index"))
    if request.method == 'POST':
        username, typed_password = request.form.get('username'), request.form.get('password')
        user = queries.check_user(username)
        if user and queries.verify_password(typed_password, user[1]):
            session['user_id'] = user[0]
            session['username'] = username
            flash('User logged in!')
            return redirect('/')
        else:
            flash('User or Password do not match')
    return render_template('login.html')


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if 'user_id' not in session:
        flash('You are not logged in!')
    else:
        session.pop('user_id', None)
        session.pop('username', None)
    return redirect(url_for('index'))

@app.route("/actors",methods=["GET","POST"])
def actors():
    actors=queries.get_actors()
    if request.is_json:
        id=request.get_json()

        result=queries.get_movies_by_id(id["name"])
        print(id["name"])
        return jsonify(result)
    return render_template("actors.html",actors=actors)

@app.route("/allActors",methods=["GET","POST"])
def Allactors():
    actors=queries.getActorsInfo()
    return render_template("allActors.html", actors=actors)

@app.route("/actor/<id>",methods=["GET","POST"])
def actorInfor(id):
    actor=queries.getActorInfoById(id)
    return render_template("actorInfo.html", actor=actor)

@app.route("/shows/most-rated/<pgNumber>",methods=['GET'])
@app.route("/shows")
def most_rated(pgNumber=1):
    sortedby = ''
    pgNumber = int(pgNumber)
    offsetNr = (pgNumber - 1) * 15
    most_rated_15_shows = queries.get_last_15_rated_shows(offsetNr)
    for x in  most_rated_15_shows:
        x['rating']=str(x['rating'])
        x['year']=x['year'].year
    if request.is_json:
        return jsonify(most_rated_15_shows)
    return render_template("most-rated.html",pgNumber=pgNumber, most_rated_15_shows=most_rated_15_shows,sortedby=sortedby)





def main():
    app.run(debug=True,
            port=8001)


if __name__ == '__main__':
    main()
