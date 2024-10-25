from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get('name', 'Recruto')
    message = request.args.get('message', 'Давай дружить')
    response = make_response(f"Hello {name}! {message}!")
    response.headers['Cache-Control'] = 'no-store'
    return response

if __name__ == '__main__':
    app.run(debug=True)