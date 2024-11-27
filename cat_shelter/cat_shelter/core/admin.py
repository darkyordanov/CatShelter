from django.contrib import admin

from cat_shelter.cats.models import \
    OurBoy, OurGirl, Kitten


@admin.register(OurBoy)
class OurBoyAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'available')
    search_fields = ('name', 'color', 'blood_type', 'color', 'available', 'created_at',)
    list_filter = ('color', 'available')
    readonly_fields = ('created_at', 'modified_at')

@admin.register(OurGirl)
class OurGirlAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'available')
    search_fields = ('name', 'color', 'blood_type', 'color', 'available', 'created_at',)
    list_filter = ('color', 'available')
    readonly_fields = ('created_at', 'modified_at')

@admin.register(Kitten)
class KittenAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'available')
    search_fields = ('name', 'color', 'blood_type', 'color', 'available', 'created_at',)
    list_filter = ('color', 'available')
    readonly_fields = ('created_at', 'modified_at')
