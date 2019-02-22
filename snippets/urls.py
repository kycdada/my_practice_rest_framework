from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include


'''for based on def'''
#urlpatterns = [
#    path('snippets/', views.snippet_list),
#    path('snippets/<int:pk>/', views.snippet_detail),
#]

'''for based on view'''
urlpatterns = [
    path('snippets/', views.SnippetList.as_view(), name='snippet-list'),
    path('snippets/<int:pk>/',  views.SnippetDetail.as_view(), name='snippet-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user-detail'),
    
    # ログイン追加
    path('api-auth/', include('rest_framework.urls')),
    
    # root
    path('', views.api_root),
    
    # highlight
    path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-highlight'),
    
]


# add for format suffix accept examurl:sneppet.json
urlpatterns = format_suffix_patterns(urlpatterns)
