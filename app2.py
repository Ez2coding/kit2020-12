from flask import Flask, request, render_template, redirect, url_for, abort


# import game

app = Flask(__name__)

@app.route('/')
def index():
    return "메인페이지123456"

@app.route('/hello')
def hello():
    return 'Hello, world!'

@app.route('/form')
def login():
    return render_template('test1.html')
    return redirect(url_for('login'))

@app.route('/hello/<name>')
def hellovar(name):
    character = game.set_character(name)
    return "{0}님 반갑습니다. (HP {1}으로 게임을 시작합니다.)" .format(character["닉네임"], [character["체력"]]) 

@app.route('/gamestart')
def gamestart():
    with open("static/save1.txt", "r", encoding='utf-8') as f:
        data = f.read()
        character = json.loads(data)
        print(character)
    return render_templates('gamestart.html')


# @app.route('/method', methods=['GET', 'POST']) 
# def method(): 
#     if request.method == 'GET': 
#         return 'GET 으로 전송이다.' 
#     else: 
#         num = request.form["num"] 
#         name = request.form["name"] 
#         return 'POST 이다. 학번은: {} 이름은: {}'.format(num, name)

@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'GET':
        return 'GET으로 전송이다'
    else:
        num = request.form['num']
        name = request.form['name']
        print(num, name)
        with open("static/save.txt", "w", encoding='utf-8') as f:
            f.write("%s,%s" % (num, name))
        return 'POST 이다 학번은: {} 이름은: {} '.format(num, name)


@app.errorhandler(404)
def page_not_found(error):
    return "페이지가 없습니다. URL을 확인하세요." , 404


if __name__ == '__main__':
    # with app.test_request_context():
    #     print(url_for('daum'))
    #     print(url_for('naver'))
    app.run(debug=True)