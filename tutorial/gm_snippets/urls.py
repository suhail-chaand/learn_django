from django.urls import path
from cb_snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('snippets/',views.SnippetList.as_view()),
    path('snippets/<int:pk>',views.SnippetDetails.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)