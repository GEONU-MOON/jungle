from flask import Flask, render_template, jsonify, request
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

app = Flask(__name__)

client = MongoClient('mongodb+srv://moondy2209:A3ykBYjy9iGaeUF4@cluster0.t0cskbu.mongodb.net/?retryWrites=true&w=majority')
db = client.dbjungle

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/memo', methods=['POST'])
def post_article():
    # 1. 클라이언트로부터 데이터를 받기
    url_receive = request.form['url_give']  # 클라이언트로부터 url을 받는 부분
    comment_receive = request.form['comment_give']  # 클라이언트로부터 comment를 받는 부분

    # 2. meta tag를 스크래핑하기
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    og_image = soup.select_one('meta[property="og:image"]')
    og_title = soup.select_one('meta[property="og:title"]')
    og_description = soup.select_one('meta[property="og:description"]')

    url_title = og_title['content']
    url_description = og_description['content']
    url_image = og_image['content']

    article = {'url': url_receive, 'title': url_title, 'desc': url_description, 'image': url_image,
               'comment': comment_receive}

    # 3. mongoDB에 데이터를 넣기
    db.articles.insert_one(article)

    return jsonify({'result': 'success'})

@app.route('/memo', methods=['GET'])
def read_articles():
    # 1. mongoDB에서 _id 값을 제외한 모든 데이터 조회해오기 (Read)
    result = list(db.articles.find({}, {'_id': 0}))
    # 2. articles라는 키 값으로 article 정보 보내주기
    return jsonify({'result': 'success', 'articles': result})

@app.route('/delete_memo_by_field', methods=['POST'])
def delete_article_by_field():
    # 클라이언트로부터 필드 값 받기 (예: url)
    url_receive = request.form['url_give']

    # 해당 url 값을 가진 데이터를 찾아 삭제
    db.articles.delete_one({'url': url_receive})

    return jsonify({'result': 'success'})

@app.route('/update_memo', methods=['POST'])
def update_article():
    original_url_receive = request.form['original_url_give']
    new_url_receive = request.form['url_give']
    comment_receive = request.form['comment_give']

    # 새 URL에 대한 메타데이터 스크래핑
    headers = {'User-Agent': '...'}
    data = requests.get(new_url_receive, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    # 새로운 메타데이터 추출
    new_og_image = soup.select_one('meta[property="og:image"]')['content']
    new_og_title = soup.select_one('meta[property="og:title"]')['content']
    new_og_description = soup.select_one('meta[property="og:description"]')['content']

    # 데이터베이스 업데이트
    db.articles.update_one({'url': original_url_receive}, 
                           {'$set': {
                               'url': new_url_receive, 
                               'comment': comment_receive,
                               'title': new_og_title,
                               'desc': new_og_description,
                               'image': new_og_image
                           }})

    return jsonify({'result': 'success'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)