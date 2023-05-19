from django.urls import path

urlpatterns = [
    path('',name="dashboard"),     
    path('add/<int:id>',name="add-transaction"),
    path('update/<int:id>',name='update-transaction'),
    path('delete/<int:id>',name='delete-transaction'),                                         
]
