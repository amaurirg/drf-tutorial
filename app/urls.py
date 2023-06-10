# from django.urls import path

# from app.views import todo_list, todo_detail_change_and_delete
# from app.views import TodoListAndCreate, TodoDetailChangeAndDelete

# Versão anterior ao viewset
"""
urlpatterns = [
    # Primeira versão da view todo_list
    # path('', todo_list),
    path('', TodoListAndCreate.as_view()),

    # Primeira versão da view todo_detail_change_and_delete
    # path('<int:pk>/', todo_detail_change_and_delete)
    path('<int:pk>/', TodoDetailChangeAndDelete.as_view())
]
"""

from rest_framework.routers import DefaultRouter
from app.views import TodoViewSet

router = DefaultRouter()
router.register(r'', TodoViewSet)
urlpatterns = router.urls
