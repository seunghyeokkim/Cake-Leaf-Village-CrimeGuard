from django.urls import path

from survey import views

urlpatterns=[
    path('', views.home),
    path('save_survey',views.save_survey),
    path('show_result', views.show_result),
    path('list', views.list),
    path('write', views.write),
    path('insert', views.insert),
    path('detail', views.detail),
    path('update', views.update),
    path('delete', views.delete),
]