from django.urls import path
from status import views

urlpatterns = [
    path('',views.StatusAllListView.as_view()),
    # path('create/',views.AddNewStatusView.as_view()),
    # path('<int:id>/',views.OnestatusApiView.as_view()),
    path('flights/',views.flightsListCreateApiView.as_view()),
    path('<int:id>/',views.StatusRetrieveUpdateDestroyAPIView.as_view()),


   
]

