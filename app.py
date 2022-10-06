from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from datetime import datetime
import os

app = Flask(__name__, static_folder='static')

# WEBSITE_HOSTNAME exists only in production environment
if not 'WEBSITE_HOSTNAME' in os.environ:
   # local development, where we'll use environment variables
   print("Loading config.development and environment variables from .env file.")
   app.config.from_object('azureproject.development')
else:
   # production
   print("Loading config.production.")
   app.config.from_object('azureproject.production')

app.config.update(
    SQLALCHEMY_DATABASE_URI=app.config.get('DATABASE_URI'),
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)

# Initialize the database connection
db = SQLAlchemy(app)

# Enable Flask-Migrate commands "flask db init/migrate/upgrade" to work
migrate = Migrate(app, db)

# Create databases, if databases exists doesn't issue create
# For schema changes, run "flask db migrate"

db.create_all()
db.session.commit()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/index.html', methods=['GET'])
def id0():
    return render_template('index.html')

@app.route('/school.html', methods=['GET'])
def id1():
    return render_template('school.html')

@app.route('/about.html', methods=['GET'])
def id2():
    return render_template('about.html')

@app.route('/admin.html', methods=['GET'])
def id3():
    return render_template('admin.html')

@app.route('/blog.html', methods=['GET'])
def id4():
    return render_template('blog.html')

@app.route('/buddy.html', methods=['GET'])
def id5():
    return render_template('buddy.html')

@app.route('/buddy-confirm.html', methods=['GET'])
def id6():
    return render_template('buddy-confirm.html')

@app.route('/causes.html', methods=['GET'])
def id7():
    return render_template('causes.html')

@app.route('/contact.html', methods=['GET'])
def id8():
    return render_template('contact.html')

@app.route('/donate.html', methods=['GET'])
def id9():
    return render_template('donate.html')

@app.route('/event.html', methods=['GET'])
def id10():
    return render_template('event.html')

@app.route('/login.html', methods=['GET'])
def id11():
    return render_template('login.html')

@app.route('/school-confirm.html', methods=['GET'])
def id12():
    return render_template('school-confirm.html')

@app.route('/service.html', methods=['GET'])
def id13():
    return render_template('service.html')

@app.route('/signup.html', methods=['GET'])
def id14():
    return render_template('signup.html')

@app.route('/single.html', methods=['GET'])
def id15():
    return render_template('single.html')

@app.route('/team.html', methods=['GET'])
def id16():
    return render_template('team.html')

@app.route('/volunteer.html', methods=['GET'])
def id17():
    return render_template('volunteer.html')

@app.route('/letters.html', methods=['GET'])
def id18():
    return render_template('letters.html')

@app.route('/children.html', methods=['GET'])
def id19():
    return render_template('children.html')

@app.route('/sponsor.html', methods=['GET'])
def id20():
    return render_template('sponsor.html')

@app.route('/create/', methods=['GET','POST'])
def add_school():
    if request.method == 'POST':
        print(request.form)
    from models import School
    try:
        school_name = request.values.get('school_name')
        school_registration = request.values.get('school_registration')
        school_address = request.values.get('school_address')
        primary_name = request.values.get('primary_name')
        primary_email = request.values.get('primary_email')
        primary_role = request.values.get('primary_role')
        secondary_name = request.values.get('secondary_name')
        secondary_email = request.values.get('secondary_email')
        secondary_role = request.values.get('secondary_role')

        school = School()
        school.school_name = school_name
        school.school_registration = school_registration
        school.school_address = school_address
        school.primary_contact_name = primary_name
        school.primary_contact_email = primary_email
        school.primary_contact_position = primary_role
        school.secondary_contact_name = secondary_name
        school.secondary_contact_email = secondary_email
        school.secondary_contact_position = secondary_role
        db.session.add(school)
        db.session.commit()

        return render_template('school-confirm.html')
    except (KeyError):
        print (KeyError)
        # Redisplay the question voting form.
        return render_template('school.html', {
            'error_message': "You must fill in all fields",
        })



# @app.route('/<int:id>', methods=['GET'])
# def details(id):
#     from models import Restaurant, Review
#     restaurant = Restaurant.query.where(Restaurant.id == id).first()
#     reviews = Review.query.where(Review.restaurant==id)
#     return render_template('details.html', restaurant=restaurant, reviews=reviews)
#
# @app.route('/create', methods=['GET'])
# def create_restaurant():
#     print('Request for add restaurant page received')
#     return render_template('create_restaurant.html')

# @app.route('/add', methods=['POST'])
# @csrf.exempt
# def add_restaurant():
#     from models import Restaurant
#     try:
#         name = request.values.get('restaurant_name')
#         street_address = request.values.get('street_address')
#         description = request.values.get('description')
#     except (KeyError):
#         # Redisplay the question voting form.
#         return render_template('add_restaurant.html', {
#             'error_message': "You must include a restaurant name, address, and description",
#         })
#     else:
#         restaurant = Restaurant()
#         restaurant.name = name
#         restaurant.street_address = street_address
#         restaurant.description = description
#         db.session.add(restaurant)
#         db.session.commit()
#
#         return redirect(url_for('details', id=restaurant.id))
#
# @app.route('/review/<int:id>', methods=['POST'])
# @csrf.exempt
# def add_review(id):
#     from models import Review
#     try:
#         user_name = request.values.get('user_name')
#         rating = request.values.get('rating')
#         review_text = request.values.get('review_text')
#     except (KeyError):
#         #Redisplay the question voting form.
#         return render_template('add_review.html', {
#             'error_message': "Error adding review",
#         })
#     else:
#         review = Review()
#         review.restaurant = id
#         review.review_date = datetime.now()
#         review.user_name = user_name
#         review.rating = int(rating)
#         review.review_text = review_text
#         db.session.add(review)
#         db.session.commit()
#
#     return redirect(url_for('details', id=id))

@app.context_processor
def utility_processor():
    def star_rating(id):
        from models import Review
        reviews = Review.query.where(Review.restaurant==id)

        ratings = []
        review_count = 0;        
        for review in reviews:
            ratings += [review.rating]
            review_count += 1

        avg_rating = sum(ratings)/len(ratings) if ratings else 0
        stars_percent = round((avg_rating / 5.0) * 100) if review_count > 0 else 0
        return {'avg_rating': avg_rating, 'review_count': review_count, 'stars_percent': stars_percent}

    return dict(star_rating=star_rating)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
   app.run()
