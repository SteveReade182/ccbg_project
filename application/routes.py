from flask import render_template, request

from application import app
from application.forms import BasicForm

# needed to connect to database
from application.data_provider_service import DataProviderService
# instantiating an object of DataProviderService
DATA_PROVIDER = DataProviderService()


@app.route('/')
@app.route('/splash')
def splash():
    return render_template('splash.html', title='CCBG Racing')




@app.route('/home')
def home():
    return render_template('home.html', title='CCBG Racing')


# @app.route('/register')
# def register():
#     return render_template('register.html', title='Register a')


@app.route('/schedules')
def schedules():
    return render_template('schedules.html', title='Upcoming Races')

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = ""
    # instantiating an object of type BasicForm
    form = BasicForm()
    if request.method == 'POST':
        firstname = form.firstname.data
        surname = form.surname.data
        age = form.age.data
        email = form.email.data
        iracing_id = form.iracing_id.data
        if len(firstname) == 0 or len(surname) == 0 or len(age) == 0 or len(email) == 0 or len(iracing_id) == 0:
            error = "Please input data into all required fields"
        else:
            new_person_id = DATA_PROVIDER.add_person(firstname, surname, age, email, iracing_id)
            success = 'Recruit Number:  ' + str(new_person_id) + ' data received. Thank you!'
            return render_template('success.html', success_message=success)
    return render_template('recruits.html', title='registration', form=form, message=error)


@app.route('/people', methods=['GET'])
def get_people():
    all_people = DATA_PROVIDER.get_people()
    return render_template('people.html', title="Recruits", people=all_people)


@app.route('/driver_profile')
def driver_profile():
    return render_template('driver_profile.html', title='Profiles')

@app.route('/contactus')
def contact_us():
    return render_template('contact_us1.html', title='Contact Us')


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
