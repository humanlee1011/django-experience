from django.conf.urls import include, url
from . import views as Question_views

urlpatterns = [
    url(r'^ask_question$', Question_views.ask_question, name = 'ask_question'),
    url(r'^question_info$', Question_views.question_info, name = 'question_info'),
]
