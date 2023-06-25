from django.urls import path
from.import views

urlpatterns = [
    
    path('', views.index, name="index"),
    path('blog/', views.blog, name="blog"),
    path('main/', views.mainPage, name="main"),
    path('myprofile/', views.myprofile, name="myprofile"),
    path('profile/', views.profile, name="profile"),


    path('signup/', views.signup_view, name="signup"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('', views.login_view, name="Index"),

    
    path('createbiodata/', views.biodata_create, name="createbiodata"),
    path('biodatalist/', views.biodata_list, name="biodatalist"),
    path('biodatadetail/<BiodataModel_id>', views.biodata_detail, name="biodatadetail"),
    
    path('searchbio/', views.search_bio, name="searchbio"),
    path('news/', views.news, name="news"),
    path('pricing/', views.pricing_view, name="pricing"),
    
    
   





]






