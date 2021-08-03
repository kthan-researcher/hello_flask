from flask import Flask, g, request, Response, make_response

app = Flask(__name__)
app.debug = True


# app.config['SERVER_NAME'] = 'local.com:4000'

# @app.route('/sd')
# def helloworld_local():
    # return 'hello local.com'

# @app.route('/sd', subdomain='g')
# def helloworld_sub():
#     return 'hello g.local.com!'


@app.route('/rp')
def rp():
    # q = request.args.get('q')
    q = request.args.getlist('q')
    return 'q=%s' % str(q)


@app.route('/test_wsgi')
def wsgi_test():
    def application(environ, start_respones):
        body = 'The request method was %s' %(environ['REQUEST_METHOD'])
        Headers = [
            ('Content-Type', 'text/plain'),
            ('Content-Length', str(len(body)))
        ]
        start_respones('200 OK', Headers)
        return [body]
    return make_response(application)


@app.route('/res_1')
def res_1():
    custom_res = Response('Custom Respones', 200, {'test': 'ttt'})
    return make_response(custom_res)

# @app.before_request
# def before_request():
#     print('before request!')
#     g.str = '한글'


@app.route('/gg')
def helloworld2():
    return 'hello world.' + getattr(g, 'str', '111')


@app.route('/')
def helloworld():
    return 'hello flask world.'