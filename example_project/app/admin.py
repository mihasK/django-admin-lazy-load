from django.contrib import admin
from  admin_lazy_load import LazyLoadAdminMixin

from .models import SomeThing

@admin.register(SomeThing)
class SomeThingAdmin(LazyLoadAdminMixin, admin.ModelAdmin):
    
    lazy_loaded_fields = (
        'exponent', # calculated model-based property
        'count_before', # calculated admin-based property
        'is_ok', # field with special html formatting (in this case - boolean icon)

    )
    list_display = ('id', 
                    
                    'is_ok',  # regular loading of field in single request
                    'is_ok_lazy',  # loads automatically in separate subsequent requests
                    'is_ok_lazy_click',  # loads only on user clicks
                    
                    'number',
                    
                    'exponent_lazy', 
                    'exponent_lazy_click', 
                    
                    'count_before_lazy',
                    'count_before_lazy_click',
                    )
    
    def count_before(self, obj):
        return SomeThing.objects.filter(
            number__lt=obj.number
        ).count()
    
    