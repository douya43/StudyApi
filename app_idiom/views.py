import json

from django.shortcuts import render
from ninja import Router, router
from app_idiom.models import Member,Exam


# Create your views here.
router = Router(tags=["idiom"])

@router.get('/test')
def get_teams(request):
    """
    获取团队列表
    """
    return "hello world"

@router.post('/exams')
def get_exam(request):
    sesion = request.values['sesion']
    try:
        exam = Exam.query.filter_by(id=sesion).first()
        result = {
            "code": 1,
            "data": {
                    "answer": exam.answer,
                    "candidates": exam.candidates.split(","),
                    "image": exam.pictureUrl
                },
            "message": "请求成功"
        }
    except:
        result = {
            "code": 0,
            "data": {},
            "message": "请求失败"
        }
    return json.dump(result)
