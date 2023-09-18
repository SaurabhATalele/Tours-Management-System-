
from django.contrib import admin
from django.urls import path
from Traveler import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("ad/", views.users),
    path("od/", views.orders),
    path("pc/", views.packages),
    path("addpc/", views.addpackages),
    path("addpc/addpc", views.addpackages),
    path("",views.home,name="home"),
    path("login",views.Login,name="Login"),
    path("profile",views.profile_info,name="Profile"),
    path("signup",views.Signup,name="signup"),
    path("logout",views.Logout,name="logout"),
    path("book-now/<name>",views.book_now,name="book now"),
    path("search-book-now",views.search_book_now,name="Search book now"),
    path("book/<name>/<num>/<date>",views.book_now_package,name="Search book now package"),
    path("book/<name>",views.search_book_now,name="Book"),
    path("cancle-order/<int:id>",views.cancle_order,name="cancle order",),
    path("success/<str:total>",views.success),
    path("supdate-profile",views.update_profile),
    path("payment", views.razorpayPayment, name='payment'),
    path("itenary-planner", views.itenary_planner, name='itenary_planner'),
     
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
