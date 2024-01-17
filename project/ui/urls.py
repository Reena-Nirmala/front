from django import views
from django.urls import path
from . import views

app_name = 'ui'
urlpatterns = [
    # path('',views.home,name="home"),
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('output', views.output,name='output'),
    path('texttospeech',views.texttospeech,name='texttospeech'),
    path('translate-summary', views.translate_summary, name='translate_summary'),
    # path('correct_grammar',views.correct_grammar,name='correct_grammar'),
    path('grammar_checker',views.grammar_checker,name="grammar_checker"),
    path('registration/',views.registration,name='registration'),
    # path('registration/registration',views.registration,name='registration'),
    path('pdf1',views.pdf1,name='pdf1'),
    path('pdf_summary_view',views.pdf_summary_view,name="pdf_summary_view"),
    # path('pdf',views.pdf,name='pdf'),
    path('grammar',views.grammar,name='grammar'),
    path('profile',views.profile,name='profile'),
    path('history',views.history,name='history'),
    path('home',views.home,name="home"),
    path('summarease',views.summarease,name="summarease"),
    path('forgotpassword',views.forgotpassword,name='forgotpassword'),
    # path('login/summarease',views.summarease,name='summarease'),
    # path('forgotpassword/',views.forgotpassword,name='forgotpassword'),
    # path('login/summarease/home',views.home,name='home'),
    # path('registration/login',views.login,name='login'),
    # path('registration/summarease',views.summarease,name='summarease'),
    # path('registration/home',views.home,name='home'),
    # path('login/home',views.home,name="home"),
    # path('login/registration',views.registration,name ="registration"),
    # path('login/forgotpassword',views.forgotpassword,name='forgotpassword'),
    
]
