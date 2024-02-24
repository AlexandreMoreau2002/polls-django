from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"), # index = index du dossier dans le site, soit polls/
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"), # polls/24/results/
    path("<int:question_id>/vote", views.vote, name="vote") # polls/24/vote/
]