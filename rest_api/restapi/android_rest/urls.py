from django.urls import path,include
from android_rest.views import lists, loginandroid, goodsAndorid, searchProduct
from django.contrib import admin

urlpatterns = [
    path('lists', lists, name="lists"),
    path('loginandroid', loginandroid, name="loginandroid"),
    path('admin/', admin.site.urls),
    path('', include('helpweb.urls')),
    path('goodsandorid', goodsAndorid, name="goodsandroid"),
    path('searchProduct',searchProduct, name="searchProduct")
]

