from flask_restful import Resource
from flasgger import swag_from
from flask import request, make_response, jsonify
from app.api.version2.models.post_model import PostModel


class QuestionBlogs(Resource):
    """class to handle question views without id request """

    @swag_from('../docs/postquestion.yml')
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
            PostModel().validate(data)
            requester = PostModel(**data)
            check = requester.check_exists('posts', 'title', data["title"])
            if check:
                return("question already exists"), 409
            post_id = requester.save()
            if isinstance(post_id, int):
                return make_response(jsonify({
                    "message": "Question Created successfully",
                    "post_id": post_id
                }), 201)
        else:
            return make_response(jsonify({
                "message": response
            }), 401)

    @swag_from('../docs/getallquestions.yml')
    def get(self):
        """getting all questions"""
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

    @swag_from('../docs/getonequestion.yml')
    def get(self, post_id):
        """get aquestion by id """
        auth = request.headers.get('Authorization')
        if not auth:
            return make_response(jsonify({
                "message": "No authorization header provided. This resource is secured"
            }), 403)
        auth_t_oken = auth.split(" ")[1]
        response = PostModel().decode_token(auth_t_oken)
        if isinstance(response, int):
            result = PostModel().get_one_post(post_id)
            if result:
                return make_response(jsonify({
                    "message": "ok",
                    "post": result
                }), 200)
            else:
                return make_response(jsonify({"message": "Item not found in the database"}))
        else:
            return make_response(jsonify({
                "message": response
            }), 401)

    @swag_from('../docs/editquestion.yml')
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
            title = data['title']
            description = data['description']
            res = PostModel().update_question(title, description, post_id)
            if res == "Updated":
                return make_response(jsonify({
                    "message": "question with id {} is updated".format(post_id)
                }), 200)
            else:
                return make_response(jsonify({"message": "Item  is not found in the database"}))
        else:
            return make_response(jsonify({
                "message": response
            }), 401)

    @swag_from('../docs/deletequestion.yml')
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
                return make_response(jsonify({"message": "Item is not found in the database"}))
        else:
            return make_response(jsonify({
                "message": response
            }), 401)
