from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'publishers', PublisherViewSet)
router.register(r'faculties', FacultyViewSet)
router.register(r'languages', LanguageViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'sections', SectionViewSet)
router.register(r'books', BookViewSet)
router.register(r'ebooks', EBookViewSet)
router.register(r'copies', CopyViewSet)
router.register(r'libraries', LibrariesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
