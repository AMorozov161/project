"""interview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from pollingSystem import views

urlpatterns = [
    path('login/', views.login, name='login'),
    # poll
    path('poll/create/', views.poll_create, name='poll_create'),
    path('poll/update/<int:poll_id>/', views.poll_update, name='poll_update'),
    path('poll/view/', views.polls_view, name='polls_view'),
    path('poll/view/active/', views.active_polls_view, name='active_poll_view'),
    # question
    path('question/create/', views.question_create, name='question_create'),
    path('question/update/<int:question_id>/', views.question_update, name='question_update'),
    # choice
    path('choice/create/', views.choice_create, name='choice_create'),
    path('choice/update/<int:choice_id>/', views.choice_update, name='choice_update'),
    # answer
    path('answer/create/', views.answer_create, name='answer_create'),
    path('answer/view/<int:user_id>/', views.answer_view, name='answer_view'),
    path('answer/update/<int:answer_id>/', views.answer_update, name='answer_update')
]
