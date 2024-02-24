from django.contrib import admin
from .models import Phong_base,Buoi_Hoc,Loai_CSVC,CSVC,phong
# Register your models here.
class phongbaseAdmin(admin.ModelAdmin):
    list_display=('id_phongbase','toa','tang','phongg')
    search_fields=['toa','tang','phongg']
    list_filter=('toa','tang','phongg')

class BuoiHocAdmin(admin.ModelAdmin):
    list_display=('id_buoihoc','ten_buoihoc')

class LoaiCSVCAdmin(admin.ModelAdmin):
    list_display=('id_tencsvc','ten_loaicsvc')

class CSVCAdmin(admin.ModelAdmin):
    list_display=('id_csvc','id_phongbase','id_tencsvc','so_luong')

class phongAdmin(admin.ModelAdmin):
    list_display=('id_phong','id_phongbase','luong_nguoi','muc_dich','tg_bd','tg_kt','id_buoihoc','lop_hoc','nguoi_dat')

admin.site.register(Phong_base,phongbaseAdmin)
admin.site.register(Buoi_Hoc,BuoiHocAdmin)
admin.site.register(Loai_CSVC,LoaiCSVCAdmin)
admin.site.register(CSVC,CSVCAdmin)
admin.site.register(phong,phongAdmin)