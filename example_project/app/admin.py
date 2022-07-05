from django.contrib import admin
from  admin_lazy_load import LazyLoadAdminMixin
from django.utils.html import format_html
from .models import SomeThing

@admin.register(SomeThing)
class SomeThingAdmin(LazyLoadAdminMixin, admin.ModelAdmin):
    
    lazy_loaded_fields = (
        'model_calculated_field', # calculated model-based property
        'count_before', # calculated admin-based property, with arbitrary html formatting
        'is_ok', # field with special html formatting (in this case - boolean icon)

    )
    
    # 1. Lazy loading works on list admin page!
    list_display = ('id', 
                    
                    'is_ok',  # regular loading of field in single request
                    'is_ok_lazy',  # loads automatically in separate subsequent requests
                    'is_ok_lazy_click',  # loads only on user clicks
                    
                    'number',
                    
                    'model_calculated_field_lazy', 
                    'model_calculated_field_lazy_click', 
                    
                    'count_before_lazy',
                    'count_before_lazy_click',
    )
    
    
    # 2. We use readonly_fields to show that lazy-loading works also on change-object admin page!
    readonly_fields = (   
                            
        'model_calculated_field_lazy', 
        'model_calculated_field_lazy_click', 
        
        'count_before_lazy',
        'count_before_lazy_click',
    )
    
    def count_before(self, obj):   
        result = SomeThing.objects.filter(
            number__lt=obj.number
        ).count()
        
        return format_html('<strong>Result is {}</strong>', result)

    
    