from flask import Flask, render_template, request
app = Flask(__name__)

@app.get('/')
def index():
    book = {
        'title': '山田莉央グラビア',
        'price': 1200,
        'arrival_day': '2024/4/16'
    }
    return render_template(
        'index.html',
        book = book
        )


@app.put('/test/<id>')
def put_test(id):
    print(id)
    return 'OK',200

@app.route('/test2', methods=['POST'])
def put_002():
    res = request.form.get("_method")
    if res == 'PUT':
        print('PUT TEST OK')

    return 'OK',200


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='5001' )