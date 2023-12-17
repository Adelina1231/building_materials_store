from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ('product',)


# class OrderStatusAdmin(admin.ModelAdmin):
#     model = OrderStatus
#     fields = ('name',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email',
                    'address', 'postal_code', 'status',
                    'created')
    list_filter = ('status', 'created')
    inlines = (OrderItemInline,)


admin.site.register(Order, OrderAdmin)
# admin.site.register(OrderStatus, OrderStatusAdmin)
