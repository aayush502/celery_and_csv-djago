from django.core.checks import messages
from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.serializers import Serializer
from .serializers import UserSerializer, PostSerializer, CommentSerializer
from . import models
from rest_framework.response import Response
from rest_framework.decorators import action, api_view, permission_classes


class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = UserSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def create(self,request):
        serializer = PostSerializer(data=request.data, context = {'request':request})
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data)

    @action(detail=False, methods=['POST', 'GET'])
    def comments(self, requset, pk):
        post = models.User.objects.get(pk=pk)
        if requset.method=="GET":
            self.serializer_class = CommentSerializer
            queryset = models.Comment.objects.filter(post=post)
            serializer = CommentSerializer(queryset, many=True, context = {'request':requset})
            return Response(serializer.data)
        else:
            self.serializer_class = CommentSerializer
            queryset = models.Comment.objects.filter(post=post)
            serializer = CommentSerializer(queryset, many=True, context = {'request':requset})
            serializer.is_valid(raise_exception=True)
            serializer.save(user = requset.user, post=post)
            return Response(serializer.data)

    @action(detail=False, methods=['DELETE'])
    def remove_comment(self, request, pk, comment):
        comment = models.Comment.objects.get(pk=comment)
        if comment.delete():
            return Response({'message':'comment deleted'})
        else:
            return Response({'message':'unable to delete comment'})
