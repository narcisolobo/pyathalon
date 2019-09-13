from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^questions/(?P<question_number>\d+)$', views.question),
    url(r'^questions/submit_choice/(?P<question_number>\d+)$', views.submit_choice),
    url(r'^total$', views.total),
]
# /questions/submit_choice/{{ question.id }}