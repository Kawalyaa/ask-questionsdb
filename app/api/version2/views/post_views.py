from flask_restful import Resource
from flask import request, make_response, jsonify
from app.api.version2.models.post_model import PostModel


class QuestionBlogs(Resource):
    """class to handle question views without id request """
    def post(self):
        pass

    def get(self):
        res = PostModel().get_posts()
        if not res:
            return make_response(jsonify({"message": "Database is empty"}), 200)
        return make_response(jsonify({
            "message": "ok",
            "posts": res
        }), 200)


class SingleQuestionBlog(Resource):
    """class to handle views which require id"""

    def get(self, id):
        pass

    def put(self, id):
        pass

    def delete(self, id):
        pass
