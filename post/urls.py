from django.urls import path
from .views import list_view, detail_view, post_share

app_name = "post"

urlpatterns = [
	path('<int:id>/share/', post_share, name="post_share"),
	path('<int:id>/<slug:slug>/', detail_view, name='post_detail'),
	path('', list_view, name='post_list'),
]

