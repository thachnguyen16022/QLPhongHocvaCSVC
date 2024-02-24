from django.db import models
# Create your models here.
class Phong_base(models.Model):
    id_phongbase=models.AutoField(primary_key=True)
    toa=models.CharField(max_length=10,null=False)
    tang=models.IntegerField(null=False)
    phongg=models.CharField(max_length=10,null=False)

    def __str__(self):
        return f"{self.id_phongbase},{self.toa},{self.tang},{self.phongg}"

class Buoi_Hoc(models.Model):
    id_buoihoc=models.AutoField(primary_key=True)
    ten_buoihoc=models.CharField(max_length=50,null=False)

    def __str__(self):
        return f"{self.id_buoihoc},{self.ten_buoihoc}"

class Loai_CSVC(models.Model):
    id_tencsvc=models.AutoField(primary_key=True)
    ten_loaicsvc=models.CharField(max_length=50,null=False)

    def __str__(self):
        return f"{self.id_tencsvc},{self.ten_loaicsvc}"

class CSVC(models.Model):
    id_csvc=models.AutoField(primary_key=True)
    id_phongbase=models.ForeignKey(Phong_base, default=None,on_delete=models.CASCADE)
    id_tencsvc=models.ForeignKey(Loai_CSVC, default=None,on_delete=models.CASCADE)
    so_luong=models.IntegerField(null=False)

    def __str__(self):
        return f"{self.id_csvc},{self.id_phongbase.phongg},{self.id_tencsvc.ten_loaicsvc},{self.so_luong}"

class phong(models.Model):
    id_phong = models.AutoField(primary_key=True)
    id_phongbase=models.ForeignKey(Phong_base, default=None,on_delete=models.CASCADE)
    luong_nguoi=models.IntegerField(null=False)
    muc_dich=models.CharField(max_length=100,null=False)
    tg_bd=models.DateField(null=True, blank=True)
    tg_kt=models.DateField(null=True, blank=True)
    id_buoihoc=models.ForeignKey(Buoi_Hoc, default=None,on_delete=models.CASCADE)
    lop_hoc=models.CharField(max_length=50,null=False)
    nguoi_dat=models.CharField(max_length=100,null=False)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.id_phong},{self.id_phongbase.phongg},{self.luong_nguoi},{self.muc_dich},{self.tg_bd},{self.tg_kt},{self.id_buoihoc.ten_buoihoc},{self.lop_hoc},{self.nguoi_dat}"
