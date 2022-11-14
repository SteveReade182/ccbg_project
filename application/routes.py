from flask import render_template, request, redirect, url_for

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
            error = "Please input data into all required fields, and for iRacing Subscriber please enter: [Y or N] "
        else:
            new_person_id = DATA_PROVIDER.add_person(firstname, surname, age, email, iracing_id)
            success = 'Recruit Number:  ' + str(new_person_id) + ' data received. Thank you!'
            return render_template('success.html', title='Registered', success_message=success)
    return render_template('recruits.html', title='Registration', form=form, message=error)


@app.route('/people', methods=['GET'])
def get_people():
    all_people_with = DATA_PROVIDER.get_people_by_racingID("Y")
    all_people_without = DATA_PROVIDER.get_people_by_racingID("N")
    # return render_template('people.html', title="Recruits", people_with=all_people_with)
    return render_template('people.html', title="Recruits", people_with=all_people_with, people_without=all_people_without)


@app.route('/driver_profile')
def driver_profile():
    return render_template('driver_profile.html', title='Current Driver Profiles')


@app.route('/contactus')
def contact_us():
    return render_template('contact_us1.html', title='Contact Us')


# routing and GET/POST and simple error check for login page. added url_for and redirect from flask
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'Racecar!':
            error = 'Invalid username or password. Please try again.'
        else:
            return redirect(url_for('get_people'))
    return render_template('login.html', error=error, title='Login')



