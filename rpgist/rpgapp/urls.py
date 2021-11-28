from django.urls import path
from . import views
app_name = 'rpgapp'
urlpatterns = [
      path('', views.index, name='index'),
      path('Character/<int:id>', views.character, name='character'),
      path('Create/Character', views.character_creator, name='create'),
      path('Login', views.Login, name='login'),
      path('Create/Hab',views.CreateHab,name='habs'),
      path('Update/<int:id>',views.updateCharacter,name='update'),
]