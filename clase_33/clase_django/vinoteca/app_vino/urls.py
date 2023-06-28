from .views import      VinosListView   \
                    ,   VinosDetailView \
                    ,   VinosCreateView \
                    ,   VinosDeleteView \
                    ,   VinosUpdateView


from django.urls import path
from .router import router

app_name = "vinos"

urlpatterns = [
    path("",VinosListView.as_view(), name="all"),
    path("create/",VinosCreateView.as_view(), name="create"),
    path("<int:pk>/delete/",VinosDeleteView.as_view(), name="delete"),
    path("<int:pk>/udpate/",VinosUpdateView.as_view(), name="update"),
    path("<int:pk>/detail/",VinosDetailView.as_view(), name="detail"),

] 

urlpatterns += router.urls
