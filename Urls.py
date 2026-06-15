from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import PostViewSet, DashboardView

router = DefaultRouter()
router.register(r'blog', PostViewSet, basename='blog-posts')

urlpatterns = [
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_login'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/dashboard/', DashboardView.as_view(), name='user_dashboard'),
    
    path('api/', include(router.urls)),
]
