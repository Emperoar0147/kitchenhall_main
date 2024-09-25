from django.urls import path
from .views import *

urlpatterns = [
    path('register', UserRegistrationView.as_view(), name='registeruser'),
    path('alluser', GetAllUsersView.as_view(), name='gtallusers'), # POST
    path('login', LoginView.as_view(), name='loginpage'), # POST
    path('activateuser', ActivateUserView.as_view(), name='activateuser'),
    path('currentuser/<str:pk>', UserDetailView.as_view(), name='userdetails'), # POST
    path('dashboard:<str:pk>', dashboard_view, name='dashboad_page'), # GET
    path('logout', logout_view, name='logout_page'), # POST
    path('profile/<str:pk>', UserProfileManagementView.as_view(), name='currentuserprofile_page'), # GET, PUT
    # path('requestpasswordreset', current_user, name='requestpasswordreset_page'), # GET, POST
    path('updatepassword:<str:pk>', updatepassword_view, name='authenticatedpasswordrest_page'), #GET, PUT
    path('passwordresetconfirm', changepassword_view, name='changepassword_page'), # POST
    # path('user:<str:pk>', current_user, name='currentuserdetails_page'), # GET
]

    # path('manageitems:<str:pk>', manageitems_view, name='manageitems_page'),
    # path('view_listeditems:<str:pk>', view_listeditems_view, name='viewlisteditem_page'),