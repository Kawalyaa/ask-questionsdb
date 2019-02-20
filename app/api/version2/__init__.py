from flask import Blueprint
from flask_restful import Api
from app.api.version2.views.post_views import QuestionBlogs, SingleQuestionBlog

"""Adding blueprint to our app"""
ver2 = Blueprint('api_v2', __name__, url_prefix='/api/v2')

"""We are using Api to make our version2 browsable"""
api = Api(ver2)

"""Registering our app routes by adding resource"""
api.add_resource(QuestionBlogs, '/question')
api.add_resource(SingleQuestionBlog, '/question/<int:post_id>')
