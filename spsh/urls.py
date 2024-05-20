
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('',include("hesab.urls")),
    path('',include("home.urls")),
    path('',include("category.urls")),
    path('',include("buy.urls")),
    path('',include("Product.urls")),
    
    path('',include("wallet.urls")),

#    path('api-auth/', include('rest_framework.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# handler404 = "home.views.error404"
# handler500 = "home.views.error500"
