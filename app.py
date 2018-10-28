from menu import Menu
from models.post import Post
from database import Database
from models.blog import Blog
Database.initialize()

menu = Menu()

menu.run_menu()


#
# blog = Blog(author="Lizzy",
#             title="Lizzy's Python Blog",
#             description="You can call me tututhegreat")
#

# blog.new_post()
#
# blog.save_to_mongo()
#
# from_database = Blog.from_mongo(blog.id)
#
# print(blog.get_posts())  #Post.from_blog(id)
#


#
# post = Post(blog_id="123",
#             title="A dumb post",
#             content="some content",
#             author="Hoffman")
#
# post.save_to_mongo()

# post = Post("title1","content1", "lizzy")
# post2 = Post("title2", "content2", "hoffman")
#
# print(post.author)
# print(post2.author)
