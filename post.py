import requests


class Post:
    def __init__(self):
        self.blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'

    def post_details(self):
        response = requests.get(self.blog_url)
        all_posts = response.json()
        return all_posts

# ob = Post()
# res = ob.post_details()
# print(type(res))