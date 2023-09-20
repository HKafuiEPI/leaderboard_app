from flask_migrate import Migrate
from flask import Flask, render_template, flash
from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from flask_login import login_required
from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import current_user
from flask_login import login_user, current_user
import os
from werkzeug.utils import secure_filename
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static'
app.secret_key = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///teams.db'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
migrate = Migrate(app, db)

@login_manager.user_loader
def load_user(username):
    if username in users:
        user = User(username)
        user.is_admin = users[username].get('is_admin', False)
        return user
    return None

################################################################################

class User(UserMixin):
    def __init__(self, username, is_admin=False):
        self.username = username
        self.is_admin = is_admin

    def get_id(self):
        return self.username
        return self.is_admin

users = {
    'user': {'password': 'password', 'is_admin': False},
    'admin': {'password': 'adminpassword', 'is_admin': True}
}

################################################################################

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    points = db.Column(db.Integer, nullable=False)
    image_path = db.Column(db.String(200)) 
    
    def __init__(self, name, points, image_path): 
        self.name = name
        self.points = points
        self.image_path = image_path


################################################################################

@app.route('/')
def leaderboard():
    teams = Team.query.order_by(Team.points.desc()).all()
    position = 1
    current_points = None
    for team in teams:
        if team.points != current_points:
            team.position = position
            current_points = team.points
        position += 1
    db.session.commit()
    return render_template('leaderboard.html', teams=teams)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            user = User(username)
            login_user(user)
            return redirect(url_for('leaderboard'))
        else :
            flash("Authentification failed")
    return render_template('login.html')

################################################################################

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

################################################################################

@app.route('/update_points', methods=['GET', 'POST'])
@login_required
def update_points():
    if not current_user.is_admin:
        return "Accès refusé. Seul l'administrateur peut effectuer cette action."
    
    if request.method == 'POST':
        team_id = int(request.form['team_id'])  
        new_points = int(request.form['points'])
        if new_points < 0 :
            flash("Error: The point of the team should be positive")
        else :
            team = Team.query.get(team_id)
            if team:
                team.points = new_points
                db.session.commit()
        
            return redirect(url_for('leaderboard'))
    
    team_id = int(request.args.get('team_id'))
    team = Team.query.get(team_id)
    return render_template('update_points.html', team=team, team_points=team.points, teams=Team .query.all())

################################################################################

@app.route('/create_team', methods=['GET', 'POST'])
@login_required
def create_team():
    # if not current_user.is_admin:
    #     return "Accès refusé. Seul l'administrateur peut effectuer cette action."
    
    # if request.method == 'POST':
    #     new_team = Team(
    #         name=request.form['name'], 
    #         points=int(request.form['points']), 
            
    #     )
    #     db.session.add(new_team)
    #     db.session.commit()
    #     return redirect(url_for('leaderboard'))
    
    # return render_template('create_team.html')
    if not current_user.is_admin:
        return "Accès refusé. Seul l'administrateur peut effectuer cette action."
    
    if request.method == 'POST':
        name = request.form['name']
        points = int(request.form['points'])
        
        # Gérer le téléchargement du fichier
        image = request.files['image']
        if image:
            # Obtenir le nom du fichier sécurisé
            filename = secure_filename(image.filename)
            # Enregistrer le fichier dans le dossier "static/images"
            image_path = os.path.join('static/images', filename)
            image.save(image_path)
        else:
            # Gérer le cas où aucun fichier n'est téléchargé
            image_path = 'static/images/default_image.png'

        new_team = Team(
            name=name,
            points=points,
            image_path=image_path
        )
        db.session.add(new_team)
        db.session.commit()
        return redirect(url_for('leaderboard'))
    
    return render_template('create_team.html')



################################################################################

@app.route('/edit_team/<int:team_id>', methods=['GET', 'POST'])
@login_required
def edit_team(team_id):
    team = Team.query.get(team_id)
    if not team:
        return "Team not found"
    
    if request.method == 'POST':
        team.name = request.form['name']
        team.points = int(request.form['points'])
        db.session.commit()
        return redirect(url_for('leaderboard'))
    return render_template('edit_team.html', team=team)

################################################################################

if __name__ == '__main__':
    app.run(debug=True)
