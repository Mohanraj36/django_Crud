from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('reg', views.reg, name='reg'),
    path('login', views.login_page, name='login'),
    path('logout', views.logout_page, name='logout'),
    path('crud', views.crud_page, name='crud'),
    path('crud/<int:id>', views.crud_single, name='crud'),
    path('insert_view', views.info_insert_view, name='insert_view'),
    path('insert', views.info_insert, name='insert'),
    path('update_view/<int:id>', views.info_update_view, name='update'),
    path('update', views.info_update, name='update'),
    path('delete/<int:id>', views.info_delete, name='delete'),
]