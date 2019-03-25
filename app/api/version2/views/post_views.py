from flask_restful import Resource
# import json
from flask import request, make_response, jsonify
from app.api.version2.models.post_model import PostModel


class QuestionBlogs(Resource):
    """class to handle question views without id request """
    def post(self):
        """creating a blog and protecting routes"""
        auth = request.headers.get('Authorization')
        if not auth:
            return make_response(jsonify({
                "message": "No authorization header provided. This resource is secured"
            }), 403)
        auth_t_oken = auth.split(" ")[1]
        response = PostModel().decode_token(auth_t_oken)
        if isinstance(response, int):
            created_by = response
            req = request.get_json()
            data = {
                "title": req["title"],
                "description": req["description"],
                "created_by": int(created_by)
            }
            requester = PostModel(**data)
            check = requester.check_exists('posts', 'title', data["title"])
            if check:
                return("question already exists")
            post_id = requester.save()
            if isinstance(post_id, int):
                return make_response(jsonify({
                    "message": "Created",
                    "post_id": post_id
                }), 201)
        else:
            return make_response(jsonify({
                "message": response
            }), 401)

    def get(self):
        auth = request.headers.get('Authorization')
        if not auth:
            return make_response(jsonify({
                "message": "No authorization header provided. This resource is secured"
            }), 403)
        auth_t_oken = auth.split(" ")[1]
        response = PostModel().decode_token(auth_t_oken)
        if isinstance(response, int):
            res = PostModel().get_posts()
            if res:
                return make_response(jsonify({
                    "message": "ok",
                    "post": res
                }), 200)

            else:
                return make_response(jsonify({"message": "Database is empty"}))

        else:
            return make_response(jsonify({
                "message": response
            }), 401)


class SingleQuestionBlog(Resource):
    """class to handle views which require id"""

    def get(self, post_id):
        auth = request.headers.get('Authorization')
        if not auth:
            return make_response(jsonify({
                "message": "No authorization header provided. This resource is secured"
            }), 403)
        auth_t_oken = auth.split(" ")[1]
        response = PostModel().decode_token(auth_t_oken)
        if isinstance(response, int):
            res = PostModel().get_one_post(post_id)
            # if res == 'Not found':
            #    return make_response(jsonify({"message": "Not found"}), 404)
            if res:
                return make_response(jsonify({
                    "message": "ok",
                    "post": res
                }), 200)
        else:
            return make_response(jsonify({
                "message": response
            }), 401)

    def put(self, post_id):
        auth = request.headers.get('Authorization')
        if not auth:
            return make_response(jsonify({
                "message": "No authorization header provided. This resource is secured"
            }), 403)
        auth_t_oken = auth.split(" ")[1]
        response = PostModel().decode_token(auth_t_oken)
        if isinstance(response, int):
            data = request.get_json()
            # for key, value, in data.items():
            title = data['title']
            description = data['description']
            res = PostModel().update_question(title, description, post_id)
            if res == "Updated":
                return make_response(jsonify({
                    "message": "question with id {} is updated".format(post_id)
                }), 200)
        else:
            return make_response(jsonify({
                "message": response
            }), 401)

    def delete(self, post_id):
        auth = request.headers.get('Authorization')
        if not auth:
            return make_response(jsonify({
                "message": "No authorization header provided. This resource is secured"
            }), 403)
        auth_t_oken = auth.split(" ")[1]
        response = PostModel().decode_token(auth_t_oken)
        if isinstance(response, int):
            deleted = PostModel()
            res = deleted.delete_tb_value("posts", "post_id", post_id)
            if res == "Deleted":
                message = "question with id {} is Deleted".format(post_id)
                return make_response(jsonify({"message": message}), 200)
        else:
            return make_response(jsonify({
                "message": response
            }), 401)
            # return make_response(jsonify({"message": "Not found"}), 404)
