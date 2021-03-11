from app import app
from views import *
from my_func import *
if __name__ == '__main__':
    app.run(port=5000,debug=True)