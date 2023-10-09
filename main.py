import flask
from flask import jsonify
from flask import request
from sql import create_connection
from sql import execute_query
from sql import execute_read_query
import datetime
from datetime import date

# creating connection to mysql database
conn = create_connection("cis4375.cpbp75z8fnop.us-east-2.rds.amazonaws.com", "admin", "password", "DaviNails")

# setting up an application name
app = flask.Flask(__name__)  # sets up the application
app.config["DEBUG"] = True  # allow to show errors in browser

today = date.today()  # sets today as today's date

authorizedusers = [
    {  # Creates user with username admin and password cars2000
        # admin user
        'username': 'admin',
        'password': 'password',
        'role': 'admin',
        'token': '1234657890',
        'admininfo': 'something super secret nobody can know'
    },
]


@app.route('/customers', methods=['GET'])  # Endpoint to return all customers
def api_get_customers():
    conn = create_connection("cis4375.cpbp75z8fnop.us-east-2.rds.amazonaws.com", "admin", "password",
                             "DaviNails")
    sql = "SELECT * FROM customer_information ORDER BY cust_ID"
    printlogs = execute_read_query(conn, sql)

    return jsonify(printlogs)  # Prints all logs

@app.route('/allreviews', methods=['GET'])  # Endpoint to return all review
def api_get_reviews():
    conn = create_connection("cis4375.cpbp75z8fnop.us-east-2.rds.amazonaws.com", "admin", "password",
                             "DaviNails")
    sql = "SELECT * FROM reviews ORDER BY rev_date DESC"
    printlogs = execute_read_query(conn, sql)

    return jsonify(printlogs)  # Prints all logs

@app.route('/activepromos', methods=['GET'])  # Endpoint to return all review
def api_get_activepromos():
    conn = create_connection("cis4375.cpbp75z8fnop.us-east-2.rds.amazonaws.com", "admin", "password",
                             "DaviNails")
    sql = "SELECT * FROM promotions WHERE promo_status = 'Active' ORDER BY promo_cost"
    printlogs = execute_read_query(conn, sql)

    return jsonify(printlogs)  # Prints all logs

@app.route('/allpromos', methods=['GET'])  # Endpoint to return all review
def api_get_allpromos():
    conn = create_connection("cis4375.cpbp75z8fnop.us-east-2.rds.amazonaws.com", "admin", "password",
                             "DaviNails")
    sql = "SELECT * FROM promotions ORDER BY promo_cost"
    printlogs = execute_read_query(conn, sql)

    return jsonify(printlogs)  # Prints all logs

@app.route('/addreview', methods=['POST'])  # endpoint to submit a review
def post_create_review():
    conn = create_connection("cis4375.cpbp75z8fnop.us-east-2.rds.amazonaws.com", "admin", "password",
                             "DaviNails")

    request_data = request.get_json()  # provids json inputs for the needed data to be inputted
    customerphone = request_data['phone_number']
    revdescription = request_data['rev_description']
    revrating = request_data['rev_rating']
    get_id = "SELECT cust_ID FROM customer_information WHERE phone_number = '%s'" % (customerphone)
    cust_id = execute_read_query(conn, get_id)
    addreview = "INSERT INTO reviews (cust_ID, rev_date, rev_description, rev_rating) VALUES (%s, '%s', '%s',%s)" % (
    cust_id[0]['cust_ID'], today, revdescription, revrating)
    execute_query(conn, addreview)  # executes above query to add the provided data to table
    return 'Thank You for the Review!'

@app.route('/addpromotion', methods=['POST'])  # endpoint to submit a review
def post_create_promo():
    conn = create_connection("cis4375.cpbp75z8fnop.us-east-2.rds.amazonaws.com", "admin", "password",
                             "DaviNails")

    request_data = request.get_json()  # provids json inputs for the needed data to be inputted
    promoname = request_data['promo_name']
    promodescription = request_data['promo_description']
    promostatus = request_data['promo_status']
    promocost = request_data['promo_cost']
    addreview = "INSERT INTO promotions (promo_name, promo_description, promo_status, promo_cost) VALUES ('%s', '%s', '%s',%s)" % (
    promoname, promodescription, promostatus, promocost)
    execute_query(conn, addreview)  # executes above query to add the provided data to table
    return 'Promotion Added'


@app.route('/api/addcar', methods=['POST'])  # endpoint to add a car
def post_add_car():
    conn = create_connection("cis4375.cpbp75z8fnop.us-east-2.rds.amazonaws.com", "admin", "password",
                             "DaviNails")
    sql = "SELECT * FROM car"

    username = request.headers[
        'username']  # get the header parameters. request headers are interpreted as dictionaries, so value access is easy and direct
    password = request.headers['password']

    for au in authorizedusers:  # loop over all users and find one that is authorized to access
        if au['username'] == username and au['password'] == password:
            request_data = request.get_json()  # provids json inputs for the needed data to be inputted
            newvin = request_data['vin']
            newmake = request_data['make']
            newmodel = request_data['model']
            newyear = request_data['year']
            addquery = "INSERT INTO car (vin, make, model, year) VALUES ('%s', '%s', '%s',%s)" % (
            newvin, newmake, newmodel, newyear)
            execute_query(conn, addquery)  # executes above query to add the provided data to table
            newmessage = "Added car " + newmake + " " + newmodel
            logquery = "INSERT INTO logs (date, name, message) VALUES ('%s', '%s', '%s')" % (
            today, username, newmessage)
            execute_query(conn, logquery)  # executes above query to write to the table log
            return 'POST REQUEST WORKED'
    return 'SECURITY ERROR'

@app.route('/api/deletecar', methods=['DELETE'])  # endpoint to delete a car
def api_delete_car():
    conn = create_connection("cis4375.cpbp75z8fnop.us-east-2.rds.amazonaws.com", "admin", "password",
                             "DaviNails")
    sql = "SELECT * FROM exam1"

    username = request.headers[
        'username']  # get the header parameters. request headers are interpreted as dictionaries, so value access is easy and direct
    password = request.headers['password']

    for au in authorizedusers:  # loop over all users and find one that is authorized to access
        if au['username'] == username and au['password'] == password:
            request_data = request.get_json()
            id_num = request_data['id']  # json input for postman
            car = "SELECT make, model FROM car WHERE id = '%s'" % (id_num)
            cartobe = execute_read_query(conn, sql)  # Takes make and model from table using ID
            results = []

            results.append(cartobe[0])  # Appends make and model to dictionary
            cartobe = execute_read_query(conn, car)
            newmessage = "Deleted car " + cartobe[0]['make'] + " " + cartobe[0][
                'model']  # adds make and model to message
            logquery = "INSERT INTO logs (date, name, message) VALUES ('%s', '%s', '%s')" % (
            today, username, newmessage)
            execute_query(conn, logquery)  # Executes above query to add date, username, and message to logs table
            delete_statement = "DELETE FROM car WHERE id = '%s'" % (id_num)  # deletes the inputted id
            execute_query(conn, delete_statement)
            return 'DELETE REQUEST WORKED'
    return 'SECURITY ERROR'


@app.route('/api/addmechanic', methods=['POST'])  # endpoint to add a mechanic
def post_add_mechanic():
    conn = create_connection("cis4375.cpbp75z8fnop.us-east-2.rds.amazonaws.com", "admin", "password",
                             "DaviNails")
    sql = "SELECT * FROM mechanic"

    username = request.headers[
        'username']  # get the header parameters. request headers are interpreted as dictionaries, so value access is easy and direct
    password = request.headers['password']

    for au in authorizedusers:  # loop over all users and find one that is authorized to access
        if au['username'] == username and au['password'] == password:
            request_data = request.get_json()  # provids json inputs for the needed data to be inputted
            newfirst = request_data['firstname']
            newlast = request_data['lastname']
            newtitle = request_data['title']
            newcar = request_data['currentcar']
            addquery = "INSERT INTO mechanic (firstname, lastname, title, currentcar) VALUES ('%s', '%s', '%s', '%s')" % (
            newfirst, newlast, newtitle, newcar)
            execute_query(conn, addquery)  # executes above query to add the provided data to table
            newmessage = "Added mechanic " + newfirst + " " + newlast
            logquery = "INSERT INTO logs (date, name, message) VALUES ('%s', '%s', '%s')" % (
            today, username, newmessage)
            execute_query(conn, logquery)  # executes above query to write to the table log
            return 'POST REQUEST WORKED'
    return 'SECURITY ERROR'


@app.route('/api/deletemechanic', methods=['DELETE'])  # endpoint to delete a mechanic
def api_delete_mechanic():
    conn = create_connection("cis4375.cpbp75z8fnop.us-east-2.rds.amazonaws.com", "admin", "password",
                             "DaviNails")
    sql = "SELECT * FROM exam1"

    username = request.headers[
        'username']  # get the header parameters. request headers are interpreted as dictionaries, so value access is easy and direct
    password = request.headers['password']

    for au in authorizedusers:  # loop over all users and find one that is authorized to access
        if au['username'] == username and au['password'] == password:
            request_data = request.get_json()
            id_num = request_data['id']  # json input for postman
            mech = "SELECT firstname, lastname FROM mechanic WHERE id = '%s'" % (id_num)
            mechtobe = execute_read_query(conn, mech)  # Takes first name and last name from ID
            results = []

            results.append(mechtobe[0])  # adds first name and last name to dictionary
            mechtobe = execute_read_query(conn, mech)
            newmessage = "Deleted mechanic " + mechtobe[0]['firstname'] + " " + mechtobe[0]['lastname']
            logquery = "INSERT INTO logs (date, name, message) VALUES ('%s', '%s', '%s')" % (
            today, username, newmessage)
            execute_query(conn, logquery)  # logs the above query
            delete_statement = "DELETE FROM mechanic WHERE id = '%s'" % (id_num)  # deletes the inputted id
            execute_query(conn, delete_statement)
            return 'DELETE REQUEST WORKED'
    return 'SECURITY ERROR'


@app.route('/api/assigncar', methods=['PUT'])  # endpoint to assign a car to a mechanic
def api_assign_car():
    conn = create_connection("cis4375.cpbp75z8fnop.us-east-2.rds.amazonaws.com", "admin", "password",
                             "DaviNails")

    username = request.headers[
        'username']  # get the header parameters. request headers are interpreted as dictionaries, so value access is easy and direct
    password = request.headers['password']

    for au in authorizedusers:  # loop over all users and find one that is authorized to access
        if au['username'] == username and au['password'] == password:
            request_data = request.get_json()
            mechanic_id = request_data['mechanic_id']  # Takes json input for the 2 ids
            car_id = request_data['car_id']

            sql = "SELECT make, model FROM car where id = '%s' " % (
                car_id)  # orders the table by distance from top down
            car = execute_read_query(conn, sql)  # Takes make and model from car table by ID
            results = []
            results.append(car[0])  # adds make and model to dictionary
            newcar = car[0]['make'] + " " + car[0]['model']  # combines make and model into 1 string

            assignquery = "UPDATE mechanic SET currentcar = '%s' WHERE id = '%s'" % (newcar, mechanic_id)
            execute_query(conn, assignquery)  # Executes above query to update mechanic's currentcar
            return 'PUT REQUEST WORKED'
    return 'SECURITY ERROR'

'''
@app.route('/api/unassigncar', methods=['PUT'])  # endpoint to unassign a car
def api_unassign_car():
    conn = create_connection("cis4375.cpbp75z8fnop.us-east-2.rds.amazonaws.com", "admin", "password",
                             "DaviNails")

    username = request.headers[
        'username']  # get the header parameters. request headers are interpreted as dictionaries, so value access is easy and direct
    password = request.headers['password']

    for au in authorizedusers:  # loop over all users and find one that is authorized to access
        if au['username'] == username and au['password'] == password:
            request_data = request.get_json()
            mechanic_id = request_data['mechanic_id']

            unassignquery = "UPDATE mechanic SET currentcar = NULL WHERE id = '%s'" % (mechanic_id)
            execute_query(conn, unassignquery)  # executes above query to set given mechanics currentcar to NULL
            return 'PUT REQUEST WORKED'
    return 'SECURITY ERROR'
'''



app.run()