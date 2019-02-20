from flask_restful import Resource
from flask import request, make_response, jsonify
from app.api.version2.models.post_model import PostModel


class QuestionBlogs(Resource):
    """class to handle question views without id request """
    def post(self):
        req = request.get_json()
        data = {
            "title": req["title"],
            "description": req["description"],
            "created_by": req["created_by"]
        }
        requester = PostModel(**data)
        res = requester.save()
        if isinstance(res, int):
            return make_response(jsonify({
                "message": "Created",
                "post_id": res
            }), 201)
        return make_response(jsonify({"message": "Post already exists"}), 409)

    def get(self):
        res = PostModel().get_posts()
        if not res:
            return make_response(jsonify({"message": "Database is empty"}), 200)
        return make_response(jsonify({
            "message": "ok",
            "post": res
        }), 200)


class SingleQuestionBlog(Resource):
    """class to handle views which require id"""

    def get(self, post_id):
        res = PostModel().get_one_post(post_id)
        if res == 'Not found':
            return make_response(jsonify({"message": "Not found"}), 404)
        return make_response(jsonify({
            "message": "ok",
            "post": res
        }), 200)

    def put(self, post_id):
        data = request.get_json()
        for key, value in data.items():
            res = PostModel().update_question("posts", key, value, "post_id", post_id)
            if res == "Updated":
                return make_response(jsonify({
                    "message": "question with id {} is updated".format(post_id)
                }), 200)
            return make_response(jsonify({
                "message": "Not found"
            }), 404)

    def delete(self, post_id):
        deleted = PostModel()
        res = deleted.delete_tb_value("posts", "post_id", post_id)
        if res == "Deleted":
            message = "question with id {} is Deleted".format(post_id)
            return make_response(jsonify({"message": message}), 200)
        return make_response(jsonify({"message": "Not found"}), 404)
