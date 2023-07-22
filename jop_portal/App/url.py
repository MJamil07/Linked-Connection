from django.urls import path;
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('' , views.chooseUser)  ,
    path('signin/<str:types>' , views.signIn) ,
    path('signup/' , views.signUp),
    path('home/' , views.home),
    path('logout/' , views.logout),
    path('apply/<int:id>' , views.view_job),
    path('jopapply/' , views.jop_apply), 
    path('viewedapply/<int:id>' , views.viewed_appply), 
    path('user/<int:id>' , views.user_view), 
    path('company/' , views.company_profile), 
    path('choose_profile/' , views.choose_profile), 
    path('follow/<int:id>' , views.follow),
    path('posts/' , views.post),
    path('jops/' , views.jops),
    path('companies/' , views.companies)





] + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)