from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)


@app.route('/')
def home():
    posts = Post()
    all_posts = posts.post_details()
    return render_template('index.html', posts=all_posts)


@app.route('/post/<int:num>')
def blog_post(num):
    posts = Post()
    all_posts = posts.post_details()
    print(num)
    print(type(num))
    print(type(all_posts[0]['id']))
    return render_template('post.html', num=num, posts=all_posts)


#
# @app.route('/<name>')
# def name_api(name):
#
#     age_point = "https://api.agify.io"
#     gender_point = "https://api.genderize.io"
#
#     params = {
#         'name': name
#     }
#
#     age_data = requests.get(age_point, params=params)
#     gender_data = requests.get(gender_point, params=params)
#
#     print(age_data.text)
#     print(gender_data.text)
#
#     return render_template('index.html', age = age_data.json()['age'], gender=gender_data.json()['gender'], name=name)
#
# @app.route('/blog')
# def blog():
#     blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
#     response = requests.get(blog_url)
#     all_posts = response.json()
#     return render_template('index.html', posts = all_posts)
#

if __name__ == "__main__":
    app.run(debug=True)
