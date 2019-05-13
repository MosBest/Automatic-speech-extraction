from bottle import Bottle
from bottle import template
root = Bottle()

# my_web.py
from bottle import request
@root.route('/login/', method=['GET', 'POST'])
def login():
    print(request.method)
    if request.method == "GET":
        return template('index.html')
    else:
        # 从input框中取值
        ret = request.forms
        ret = request.query
        ret = request.body
        user = request.forms.get('user')

        return template('<b>hello {{name}}</b>!', name=user)



root.run(host='localhost', port=8091)
