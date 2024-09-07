from flask import Flask, render_template, jsonify

# flask is module or we can say a package
# Flask is a class inside that Module provided to us
#  now to use that class we will need to create a object or App for that so in python we do it by

app = Flask(__name__)
JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000'
}, {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': 'Rs. 15,00,000'
}, {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote'
}, {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary': '$150,000'
}]
# __name__ => it is the entry point for that class , in python that is done using (__name__)

# Route is just regestring a path that will be redirected to , displayed just after the domain name


# dec0rator
@app.route("/")
def helloworld():
  return render_template('home.html', jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


# print("Hello from Durva !")

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
