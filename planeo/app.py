import flask
import logging

app = flask.Flask(__name__)

# stomach ache remover
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
# works great!

@app.route('/', methods=['GET', 'POST'])
def index():
    if flask.request.method == 'POST': # logging in
        form = flask.request.form.get

        resp = flask.make_response(flask.redirect('/dash'))
        resp.set_cookie('name', form('name'))
        resp.set_cookie('password', form('password'))

        return resp 

    if flask.request.cookies.get('password'): # already logged in
        return flask.redirect('/dash')

    return flask.render_template('index.html')

@app.route('/dash')
def dash():
    cookie = flask.request.cookies.get
    return flask.render_template('dash.html', name=cookie('name'))

@app.route('/logout')
def logout():
    resp = flask.make_response(flask.redirect('/'))
    resp.set_cookie('name', '')
    resp.set_cookie('password', '')

    return resp

app.run(port=2024, debug=True)
