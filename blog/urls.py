# @Author: Ibrahim Salihu Yusuf <yusuf>
# @Date:   2020-03-20T15:00:08+02:00
# @Email:  sibrahim1396@gmail.com
# @Last modified by:   yusuf
# @Last modified time: 2020-03-25T15:42:46+02:00
from . import views
from django.urls import path
from .feeds import LatestPostsFeed
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap

sitemaps = {
    "posts": PostSitemap,
}

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path("about/", views.AboutView.as_view(), name="about"),
    path("projects/", views.ProjectView.as_view(), name="projects"),
    path("projects/<slug:slug>", views.project_detail_view, name="project_detail"),
    path("translate/<slug:slug>", views.translate, name="translate"),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path("feed/rss", LatestPostsFeed(), name="post_feed"),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
]
