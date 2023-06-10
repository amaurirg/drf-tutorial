# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.exceptions import NotFound
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import generics

from rest_framework import viewsets
from app.models import Todo
from app.serializers import TodoSerializer


# Primeira versão da view todo_list
# =================================
# @api_view(["GET", "POST"])
# def todo_list(request):
#     if request.method == "GET":
#         todo = Todo.objects.all()
#         serializer = TodoSerializer(todo, many=True)
#         return Response(serializer.data)
#     elif request.method == "POST":
#         serializer = TodoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Segunda versão da view todo_list
# Primeira versão da view TodoListAndCreate
# =================================
# class TodoListAndCreate(APIView):
#     def get(self, request):
#         todo = Todo.objects.all()
#         serializer = TodoSerializer(todo, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = TodoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Terceira versão da view todo_list
# Segunda versão da TodoListAndCreate
# ==================================
# class TodoListAndCreate(generics.ListCreateAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer


# //////////////////////////////////////////////////////////////////////////////////////


# Primeira versão da view todo_detail_change_and_delete
# =====================================================
# @api_view(["GET", "PUT", "DELETE"])
# def todo_detail_change_and_delete(request, pk):
#     try:
#         todo = Todo.objects.get(pk=pk)
#     except Todo.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == "GET":
#         serializer = TodoSerializer(todo)
#         return Response(serializer.data)
#
#     elif request.method == "PUT":
#         serializer = TodoSerializer(todo, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == "DELETE":
#         todo.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# Segunda versão da view todo_detail_change_and_delete
# Primeira versão da view TodoDetailChangeAndDelete
# ====================================================

# class TodoDetailChangeAndDelete(APIView):
#     def get_object(self, pk):
#         try:
#             return Todo.objects.get(pk=pk)
#         except Todo.DoesNotExist:
#             raise NotFound()
#
#     def get(self, request, pk):
#         todo = self.get_object(pk)
#         serializer = TodoSerializer(todo)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         todo = self.get_object(pk)
#         serializer = TodoSerializer(todo, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         todo = self.get_object(pk)
#         todo.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# Terceira versão da view todo_detail_change_and_delete
# Segunda versão da view TodoDetailChangeAndDelete
# class TodoDetailChangeAndDelete(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer


# //////////////////////////////////////////////////////////////////////////////////////


# Quarta versão da view todo_list
# Quarta versão da view todo_detail_change_and_delete
# Versão final, simplificada e unindo as duas funções numa única função de CRUD
class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
