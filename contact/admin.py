from django.contrib import admin
from contact import models

# Register your models here.


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone','show',
    ordering = '-id',
# -id é para ordenar decrescente para visualizar os mais recentes
    list_filter = 'created_date',
# pesquisar contatos ->
    search_fields = 'id', 'first_name', 'last_name'
    list_per_page = 10
    list_max_show_all = 100
    list_editable = 'show',
    list_display_links = 'id', 'first_name','phone',


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = '-id',
