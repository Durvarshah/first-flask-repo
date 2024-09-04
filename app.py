from flask import Flask

# flask is module or we can say a package
# Flask is a class inside that Module provided to us
#  now to use that class we will need to create a object or App for that so in python we do it by

app = Flask(__name__)

# __name__ => it is the entry point for that class , in python that is done using (__name__)


# Route is just regestring a path that will be redirected to , displayed just after the domain name

# dec0rator
@app.route("/")
def helloworld():
  return "Helloo World !"


# print("Hello from Durva !")


if __name__ =="__main__":
  app.run(host ="0.0.0.0", debug = True)