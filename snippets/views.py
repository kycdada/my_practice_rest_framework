'''based on def'''
#from django.shortcuts import render
#from django.http import HttpResponse, JsonResponse
## templateにcsrf トークンがなくても動くように
#from django.views.decorators.csrf import csrf_exempt
#from rest_framework.renderers import JSONRenderer
#from rest_framework.parsers import JSONParser
#from snippets.models import Snippet
#from snippets.serializers import SnippetSerializer

'''based on def with Response,api_view '''
#from rest_framework import status
#from rest_framework.decorators import api_view
#from rest_framework.response import Response
#from snippets.models import Snippet
#from snippets.serializers import SnippetSerializer

#'''based on view'''
#from snippets.models import Snippet
#from snippets.serializers import SnippetSerializer
#from django.http import Http404
#from rest_framework.views import APIView
#from rest_framework.response import Response
#from rest_framework import status

#'''based on view with Mixin'''
#from snippets.models import Snippet
#from snippets.serializers import SnippetSerializer
#from rest_framework import mixins
#from rest_framework import generics

'''based on generic class view'''
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics


'''add endpoint to user'''
from django.contrib.auth.models import User
from snippets.serializers import UserSerializer

'''add permissions'''
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly


'''root endpoint for api'''
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


'''endpoint for highlightsnippet'''
from rest_framework import renderers


''' based on def '''
#@csrf_exempt
#def snippet_list(request):
#    ''' list all code snippets, or create a new snippet. '''
#    
#    if request.method == "GET":
#        snippets = Snippet.objects.all()
#        serializer = SnippetSerializer(snippets, many=True)
#        return JsonResponse(serializer.data, safe=False)
#    elif request.method == "POST":
#        data = JSONParser().parse(request)
#        serializer = SnippetSerializer(data=data)
#        if serializer.iis_valid():
#            serializer.save()
#            return JsonResponse(serializer.data,status=201)
#            
#        return JsonResponse(serializer.errors, status=400)
#        
#@csrf_exempt
#def snippet_detail(request, pk):
#    ''' Retrieve, update or delete a code snippet. '''
#    
#    try:
#        snippet = Snippet.objects.get(pk=pk)
#    except Snippet.DoesNotExist:
#        return HttpResponse(status=404)
#    
#    if request.method == 'GET':
#        serializer = SnippetSerializer(snippet)
#        return JsonResponse(serializer.data)
#    
#    if request.method == 'PUT':
#        data = JSONParser().parse(request)
#        serializer = snippetSerializer(snippet, data=data)
#        if serializer.isvalid():
#            serializer.save()
#            return JsonResponse(serializer.data)
#        return JsonResponse(serializer,errors, status=400)
#        
#    elif request.method == "DELETE":
#        snippet.delete()
#        return HttpResponse(status=204)
#        


'''based on def with Response, api_view'''
## hoge=hoge is default set
#@api_view(['GET','POST'])
#def snippet_list(request, format=None):
#    '''list all code snippets, or create a new snippet.'''
#    
#    if request.method == 'GET':
#        snippets = Snippet.objects.all()
#        serializer = SnippetSerializer(snippets, many=True)
#        return Response(serializer.data)
#        
#    elif request.method == 'POST':
#        serializer = SnippetSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#@api_view(['GET', 'PUT', 'DELETE'])
#def snippet_detail(request, pk, format=None):
#    ''' Retrieve, update or delete a code snippet.'''
#    
#    try:
#        snippet = Snippet.objects.get(pk = pk)
#    except Snippet.DoesNotExist:
#        return Response(status= status.HTTP_404_NOT_FOUND)
#        
#    if request.method == 'GET':
#        serializer = SnippetSerializer(snippet)
#        return Response(serializer.data)
#        
#    elif request.method == 'PUT':
#        serializer = SnippetSerializer(snippet, data= request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#        
#    elif request.method == 'DELETE':
#        snippet.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)


''' based on view '''
#class SnippetList(APIView):
#    '''LIst all snippets, or create new snippet.'''
#    
#    # format=None is format suffix
#    def get(self, request, format=None):
#        snippets = Snippet.objects.all()
#        serializer = SnippetSerializer(snippets, many=True)
#        return Response(serializer.data)
#        
#    def post(self, request, format=None):
#        serializer = SnippetSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#        
#class SnippetDetail(APIView):
#    '''Retrieve, update or delete a snippet instance.'''
#    
#    def get_object(self, pk):
#        try:
#            return Snippet.objects.get(pk=pk)
#        # if not hit models, it happen
#        except Snippet.DoesNotExist:
#            # happen exception 404
#            raise HTTP404
#            
#    def get(self, request, pk, format=None):
#        snippet = self.get_object(pk)
#        serializer = SnippetSerializer(snippet)
#        return Response(selializer.data)
#        
#    def put(self, request, pk, format=None):
#        snippet = self.get_object(pk)
#        snippet.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)


#''' based on view with Mixin'''
#
#class SnippetList(mixins.ListModelMixin,
#                  mixins.CreateModelMixin,
#                  generics.GenericAPIView):
#    queryset = Snippet.objects.all()
#    serializer_class = SnippetSerializer
#    
#    def get(self, request, *args, **kwargs):
#        # self.list by mixin
#        return self.list(request, *args, **kwargs)
#    
#    def post(self, request, *args, **kwargs):
#        # self.create by mixin
#        return self.create(request, *args, **kwargs)
#        
#class SnippetDetail(mixins.RetrieveModelMixin,
#                    mixins.UpdateModelMixin,
#                    mixins.DestroyModelMixin,
#                    generics.GenericAPIView
#                    ):
#    queryset = Snippet.objects.all()
#    serializer_class = SnippetSerializer
#    
#    def get(self, request, *args, **kwargs):
#        return self.retrieve(request, *args, **kwargs)
#        
#    def put(self, request, *args, **kwargs):
#        return self.update(request, *args, **kwargs)
#        
#    def delete(self, request, *args, **kwargs):
#        return self.destroy(request, *args, **kwargs)


''' based on generic class view '''

class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    
    # relation  of snippet to user
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
    # add permission
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    
    # add permission
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                         IsOwnerOrReadOnly)
    

''' add endpoint to user '''
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

'''root end point for api'''
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })
    
'''endpoint for highlightsnippet'''
class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    # for return by html
    renderer_classes = (renderers.StaticHTMLRenderer,)
    
    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

