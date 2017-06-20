import os

from flask import Flask
from flask_restful import Api
from flask_login import LoginManager

from models import User
from resources import SigninResource, UserResource, PostResource, UserPostsResource, LikeResource, \
    LikesResource, SignoutResource, TestResource, PostsResource, CreateUserResource

app = Flask(__name__)
api = Api(app)

app.config['UPLOAD_FOLDER'] = 'uploads/'

app.config['ALLOWED_EXTENSIONS'] = (['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', "JPG"])

login_manager = LoginManager()
# TODO: Revisit to what extent you need session strength
# login_manager.session_protection = 'strong'
login_manager.login_view = 'login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


# GET - Test an API call
api.add_resource(TestResource, "/puppies/api/v1.0/test", endpoint="test")

# POST - Sign in a user
api.add_resource(SigninResource, "/puppies/api/v1.0/signin", endpoint="login")

# GET - Sign out a user
api.add_resource(SignoutResource, "/puppies/api/v1.0/logout", endpoint="logout")

# GET - Get user profile
api.add_resource(UserResource, "/puppies/api/v1.0/users/<int:user_id>", endpoint="user_by_id")

# POST - Create a user
api.add_resource(CreateUserResource, "/puppies/api/v1.0/users", endpoint="user")

# GET - Get post details
api.add_resource(PostResource, "/puppies/api/v1.0/posts/<int:post_id>", endpoint="post_by_id")

# GET - Get list of posts a user made
api.add_resource(UserPostsResource, "/puppies/api/v1.0/users/<int:user_id>/posts", endpoint="user_posts")

# GET - Get all posts
# POST - Create a post
api.add_resource(PostsResource, "/puppies/api/v1.0/posts", endpoint="posts")

# NOTE: For all apis related to likes, it should be further extended to reactions instead of likes if we are to support
# multiple reactions in the future. Following changes are needed ->
# * Remove is_liked column from Post model
# * Create a Reactions table with FK to Post and User table
# * All reactions will be added/updated in this table

# PUT - Like a post <- NOTE: Should it be a PATCH?
api.add_resource(LikeResource, "/puppies/api/v1.0/posts/<int:post_id>/like", endpoint="like_post")

# GET - Return posts that have been liked by a user
api.add_resource(LikesResource, "/puppies/api/v1.0/users/<int:user_id>/posts/likes", endpoint="likes_posts")

if __name__ == '__main__':
    app.secret_key = os.urandom(24)

    # NOTE: Add host="0.0.0.0" as a param
    app.run(debug=True)
