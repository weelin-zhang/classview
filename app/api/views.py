from django.shortcuts import get_object_or_404
from .serializers import AuthorSerializer, BookSerializer
from ..models import Author, Book
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
# from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAdminUser

# 创建视图设置和路由
from rest_framework import viewsets



class AuthorListView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
    
class AuthorDetailView(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    # lookup_field = "name"

# create
class CreateAuthorView(APIView):
    # model = Author
    model_serializer = AuthorSerializer
    # settings中存在全局配置定义时REST_FRAMEWORK.DEFAULT_AUTHENTICATION_CLASSES时,可省去),authentition_class
    #REST_FRAMEWORK = {'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework.authentication.TokenAuthentication', )
    # authentication_classes = (TokenAuthentication,)
    
    permission_classes = (IsAuthenticated,)
    
    def post(self, request):
        serializer = self.model_serializer(data=request.data)
        msg = ""
        if serializer.is_valid():
            serializer.save()
            msg = "succeed add new book to author"
            return Response(data={"msg": msg, "status": "0"}, status=status.HTTP_201_CREATED)
        else:
            for k, v in serializer.errors.items():
                print(k, ''.join(v))
                msg += '{},{}'.format(k, ''.join(v))
            return Response(data={"msg": msg, "status": "1"}, status=status.HTTP_400_BAD_REQUEST)


# 删改
class UpdateDeleteAuthorView(APIView):
    # settings中存在全局配置定义时REST_FRAMEWORK.DEFAULT_AUTHENTICATION_CLASSES时,可省去),authentition_class
    #REST_FRAMEWORK = {'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework.authentication.TokenAuthentication', )
    # authentication_classes = (TokenAuthentication,)
    
    permission_classes = (IsAuthenticated,)
    
    model = Author
    model_serializer = AuthorSerializer
    # def get_object(self, pk):
    #     try:
    #         return self.model.objects.get(pk=pk)
    #     except Book.DoesNotExist:
    #         raise Http404
    
    # 更新
    def put(self, request, pk):
        # instance = self.get_object(pk)
        instance = get_object_or_404(self.model, pk)
        serializer = self.model_serializer(instance, data=request.data)
        msg = ''
        if serializer.is_valid():
            serializer.save()
            return Response(data={"status": "0", "msg": f"{serializer.data}, 资源更新成功"},
                            status=status.HTTP_200_OK)
        else:
            for k, v in serializer.errors.items():
                print(k, ''.join(v))
                msg += '{},{}'.format(k, ''.join(v))
            return Response(data={"status": "1", "msg": f"{msg}"},
                            status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        # instance = self.get_object(pk)
        instance = get_object_or_404(self.model, pk=pk)
        serializer = self.model_serializer(instance)
        instance.delete()
        return Response(data={"status": "0", "msg": f"{serializer.data},资源删除成功"}, status=status.HTTP_204_NO_CONTENT)



# book list
class BookListView(generics.ListAPIView):
    '''
    图书列表
    '''
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailView(generics.RetrieveAPIView):
    '''
    图书详情
    '''
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
# create
class CreateBookView(APIView):
    '''
    新增图书
    '''
    # settings中存在全局配置定义时REST_FRAMEWORK.DEFAULT_AUTHENTICATION_CLASSES时,可省去),authentition_class
    #REST_FRAMEWORK = {'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework.authentication.TokenAuthentication', )
    # authentication_classes = (TokenAuthentication,)
    
    # permission_classes = (IsAuthenticated,)
    
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        msg = ""
        if serializer.is_valid():
            serializer.save()
            msg = "succeed add new book to author"
            return Response(data={"msg": msg, "status": "0"}, status=status.HTTP_201_CREATED)
        else:
            for k, v in serializer.errors.items():
                print(k, ''.join(v))
                msg += '{},{}'.format(k, ''.join(v))
            return Response(data={"msg": msg, "status": "1"}, status=status.HTTP_400_BAD_REQUEST)
        

class UpdateDeleteBookView(APIView):
    # settings中存在全局配置定义时REST_FRAMEWORK.DEFAULT_AUTHENTICATION_CLASSES时,可省去),authentition_class
    #REST_FRAMEWORK = {'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework.authentication.TokenAuthentication', )
    # authentication_classes = (TokenAuthentication,)
    
    # permission_classes = (IsAuthenticated,)
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    # permission_classes = (AllowAny,)
    
    model = Book
    model_serializer = BookSerializer
    # def get_object(self, pk):
    #     try:
    #         return self.model.objects.get(pk=pk)
    #     except Book.DoesNotExist:
    #         raise Http404
    
    # 更新
    def put(self, request, pk):
        '''
        图书修改
        :param request:
        :param pk:
        :return:
        '''
        # instance = self.get_object(pk)
        instance = get_object_or_404(self.model, pk=pk)
        serializer = self.model_serializer(instance, data=request.data)
        msg = ''
        if serializer.is_valid():
            serializer.save()
            return Response(data={"status": "0", "msg": f"{serializer.data}, 资源更新成功"},
                            status=status.HTTP_200_OK)
        else:
            for k, v in serializer.errors.items():
                print(k, ''.join(v))
                msg += '{},{}'.format(k, ''.join(v))
            return Response(data={"status": "1", "msg": f"{msg}"},
                            status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        '''
        图书删除
        :param request:
        :param pk:
        :return:
        '''
        # instance = self.get_object(pk)
        instance = get_object_or_404(self.model, pk=pk)
        serializer = self.model_serializer(instance)
        instance.delete()
        return Response(data={"status": "0", "msg": f"{serializer.data},资源删除成功"}, status=status.HTTP_204_NO_CONTENT)
        
        
# # #  # # # # # #   api v2 使用viewsets实现   # #  # # # # # # # # # #  # # # # # # # # # #  # # # # # # #
class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
# class BookViewSet(viewsets.ReadOnlyModelViewSet):

#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        # 自定义每一个方法的权限
        if self.action == 'list':
            # permission_classes = [IsAuthenticated]
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

