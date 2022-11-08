from flask import render_template # ,request

from application import app
# from application.forms import BasicForm


@app.route('/')
@app.route('/splash')
def splash():
    return render_template('splash.html', title='Welcome')


@app.route('/home')
def home():
    return render_template('home.html', title='CCBG Racing')


@app.route('/about')
def about():
    return render_template('about.html', title='About Us')


@app.route('/register')
def register():
    return render_template('register.html', title='Register')


@app.route('/schedules')
def schedules():
    return render_template('schedules.html', title='Upcoming Races')


# @app.route('/favourites')
# def favourites():
#     cars = ['Porsche 918', 'Jaguar XJR12', 'Aston Martin Vantage', 'Alfa Romeo Brera', 'Volkswagon Golf Mk1']
#     return render_template('favourites.html', title='Favourites', cars_list=cars)


# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     error = ""
#     # instantiating an object of type BasicForm
#     form = BasicForm()
#     if request.method == 'POST':
#         first_name = form.first_name.data
#         last_name = form.last_name.data
#         if len(first_name) == 0 or len(last_name) == 0:
#             error = "Please supply both first and last name"
#         else:
#             return 'Thank you!'
#     return render_template('person.html', form=form, message=error)
