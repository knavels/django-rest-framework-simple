from django.urls import path
from .views import article_list, article, ArticleListAPIView, ArticleShowAPIView, ArticleGenericAPIView

urlpatterns = [
    # path('articles/', article_list),
    path('articles/', ArticleListAPIView.as_view()),
    path('gen-articles/', ArticleGenericAPIView.as_view()),
    path('gen-articles/<int:id>', ArticleGenericAPIView.as_view()),
    # path('articles/<int:pk>', article),
    path('articles/<int:id>', ArticleShowAPIView.as_view()),

]