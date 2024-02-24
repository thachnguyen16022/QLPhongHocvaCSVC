import re

from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import phong as phong_model
from .models import CSVC as csvc_model
from .models import Phong_base as Phong_base_model
from .models import Buoi_Hoc as Buoi_Hoc_model
from .models import Loai_CSVC as Loai_CSVC_model
# Create your views here.
def get_suaPhong(request,id):
    phong_list=Phong_base_model.objects.filter(id_phongbase=id)
    return render(request,'Sua_tenPhong.html',{'phong_list':phong_list})
def get_suacsvc(request,id):
    csvc_list=Loai_CSVC_model.objects.filter(id_tencsvc=id)
    return render(request,'Sua_tenCSVC.html',{'csvc_list':csvc_list})
def get_taocsvc(request):
    csvc_list=Loai_CSVC_model.objects.filter()
    return render(request,'tao_csvc.html',{'csvc_list':csvc_list})
def get_taophong(request):
    phong_list=Phong_base_model.objects.filter().order_by('phongg')
    return render(request,'tao_phong.html',{'phong_list':phong_list})
def get_404(request):
    return render(request,'pages-error-404.html')
#Trang views các bảng
def get_home(request):
    phong_list=phong_model.objects.filter().order_by('lop_hoc')
    csvc_list= csvc_model.objects.filter().order_by('id_csvc')
    return render(request, 'home.html',{'phong_list':phong_list,'csvc_list':csvc_list})
#Trang thêm mới phòng
def get_phong(request):
    phong_list=Phong_base_model.objects.filter().order_by('phongg')
    buoi_list=Buoi_Hoc_model.objects.filter().order_by('id_buoihoc')
    return render(request,'Them.html',{'phong_list':phong_list,'buoi_list':buoi_list})
#Trang thêm mới csvc cho phòng
def get_csvc(request):
    phong_list=Phong_base_model.objects.filter().order_by('phongg')
    loai_list=Loai_CSVC_model.objects.filter().order_by('id_tencsvc')
    return render(request,'them_csvc.html',{'phong_list':phong_list,'loai_list':loai_list})
#Chức năng thêm phòng
def add_phong(request):
    if request.method=='POST':
        id_phongbase=request.POST['id_phongbase']
        luong_nguoi=request.POST['luong_nguoi']
        muc_dich=request.POST['muc_dich']
        tg_bd=request.POST['tg_bd']
        tg_kt=request.POST['tg_kt']
        id_buoihoc=request.POST['id_buoihoc']
        lop_hoc=request.POST['lop_hoc']
        nguoi_dat=request.POST['nguoi_dat']

        
        existing_phong = phong_model.objects.filter(id_phongbase=id_phongbase,tg_bd__lte=tg_kt,tg_kt__gte=tg_bd,id_buoihoc=id_buoihoc).exclude(id_phong=None).first()
        if existing_phong:
            messages.error(request, "Phòng đã được đăng ký rồi hãy đăng ký phòng khác hoặc thời gian khác")
            return redirect('/them-phong')
        existing_phong2 = phong_model.objects.filter(tg_bd__lte=tg_kt,tg_kt__gte=tg_bd,id_buoihoc=id_buoihoc,lop_hoc=lop_hoc).exclude(id_phong=None).first()
        if existing_phong2:
            messages.error(request, f"Lớp {lop_hoc} đã có lịch từ ngày {tg_bd} đến ngày {tg_kt} rồi")
            return redirect('/them-phong')
        if not (tg_bd and tg_kt):
            messages.error(request, "Thời gian bắt đầu và kết thúc không được để trống")
            return redirect('/them-phong')
        if tg_bd > tg_kt:
            messages.error(request, "Thời gian bắt đầu không được lớn hơn thời gian kết thúc")
            return redirect('/them-phong')

        phong=Phong_base_model.objects.get(id_phongbase=id_phongbase)
        time=Buoi_Hoc_model.objects.get(id_buoihoc=id_buoihoc)

        try:
            phongmoi = phong_model.objects.create(
                id_phongbase=phong,
                luong_nguoi=luong_nguoi,
                muc_dich=muc_dich,
                tg_bd=tg_bd,
                tg_kt=tg_kt,
                id_buoihoc=time,
                lop_hoc=lop_hoc,
                nguoi_dat=nguoi_dat
            )
            phongmoi.save()
            return redirect('/')
        except Exception as e:
            messages.error(request, f"Có lỗi xảy ra: {e}")
            return redirect('/them-phong')
    messages.error(request,"Thêm phòng không thành công")
    return redirect('/them-phong')
#Chức năng thêm csvc
def add_csvc(request):
     if request.method=='POST':
        id_phongbase=request.POST['id_phongbase']
        id_tencsvc=request.POST['id_tencsvc']
        so_luong=request.POST['so_luong']
        
        existing_csvc = csvc_model.objects.filter(id_phongbase=id_phongbase, id_tencsvc=id_tencsvc).exclude(id_csvc=None).first()
        if existing_csvc:
            messages.error(request, f"Phòng này đã có rồi")
            return redirect('/them-csvc')
        
        phong=Phong_base_model.objects.get(id_phongbase=id_phongbase)
        csvc=Loai_CSVC_model.objects.get(id_tencsvc=id_tencsvc)

        csvcmoi=csvc_model.objects.create(id_phongbase=phong,id_tencsvc=csvc,so_luong=so_luong)
        csvcmoi.save()

        return redirect('/')    

#Chức năng xóa phòng   
def delete_phong(request,id):
        phong_xoa=get_object_or_404(phong_model,id_phong=id)
        phong_xoa.delete()

        return redirect('/')

#Xóa csvc    
def delete_csvc(request,id):
        csvc_xoa=get_object_or_404(csvc_model,id_csvc=id)
        csvc_xoa.delete()
                
        return redirect('/')

#View sửa phòng
def view_phong(request,id):
    phong_list=phong_model.objects.filter(id_phong=id)
    phongbase_list=Phong_base_model.objects.filter()
    buoihoc_list=Buoi_Hoc_model.objects.filter()
    return render(request,'phong.html',{'phong_list':phong_list,'phongbase_list':phongbase_list,'buoihoc_list':buoihoc_list})
#View sửa csvc
def view_csvc(request,id):
    csvc_list=csvc_model.objects.filter(id_csvc=id)
    phongbase_list=Phong_base_model.objects.filter()
    loaicsvc_list=Loai_CSVC_model.objects.filter()
    return render(request,'csvc.html',{'csvc_list':csvc_list,'phongbase_list':phongbase_list,'loaicsvc_list':loaicsvc_list})
#Chức năng sửa phòng    
def edit_phong(request):
    if request.method=='POST':
        id=request.POST['id_phong']
        id_phongbase=request.POST['id_phongbase']
        luong_nguoi=request.POST['luong_nguoi']
        muc_dich=request.POST['muc_dich']
        tg_bd=request.POST['tg_bd']
        tg_kt=request.POST['tg_kt']
        id_buoihoc=request.POST['id_buoihoc']
        lop_hoc=request.POST['lop_hoc']
        nguoi_dat=request.POST['nguoi_dat']
        
        a=id_buoihoc.split(',')[1]

        existing_phong = phong_model.objects.filter(id_phongbase=id_phongbase[0],tg_bd__lte=tg_kt,tg_kt__gte=tg_bd,id_buoihoc=id_buoihoc[0]).exclude(id_phong=id).first()
        if existing_phong:
            messages.error(request, "Phòng đã được đăng ký rồi hãy đăng ký phòng khác hoặc thời gian khác")
            return redirect(f'/phong/{id}')
        existing_phong2 = phong_model.objects.filter(tg_bd__lte=tg_kt,tg_kt__gte=tg_bd,lop_hoc=lop_hoc,id_buoihoc=id_buoihoc[0]).exclude(id_phong=id).first()
        if existing_phong2:
            messages.error(request, f"Lớp {lop_hoc} đã có lịch vào buổi {a} từ ngày {tg_bd} đến ngày {tg_kt} rồi")
            return redirect(f'/phong/{id}')
        if not (tg_bd and tg_kt):
            messages.error(request, "Thời gian bắt đầu và kết thúc không được để trống")
            return redirect(f'/phong/{id}')
        if tg_bd > tg_kt:
            messages.error(request, "Thời gian bắt đầu không được lớn hơn thời gian kết thúc")
            return redirect(f'/phong/{id}')


        # Lấy đối tượng phong cần chỉnh sửa
        phong_can_chinh_sua = get_object_or_404(phong_model, id_phong=id)

        # Cập nhật các trường của đối tượng phong
        id_phong_parts = id_phongbase.split(',')
        if len(id_phong_parts) >= 1:
            # Lấy phần tử đầu tiên, có thể là id_phong hợp lệ
            id_phong_value = id_phong_parts[0]

            try:
                # Cố gắng chuyển đổi thành integer
                id_phong_int = int(id_phong_value)

                # Tìm đối tượng phong_model theo id_phong
                phong_instance = Phong_base_model.objects.get(id_phongbase=id_phong_int)

                # Gán đối tượng phong_model cho csvc_to_edit.id_phong
                phong_can_chinh_sua.id_phongbase = phong_instance
            except (ValueError, phong_model.DoesNotExist):
                # Xử lý trường hợp giá trị không thể chuyển đổi hoặc không tìm thấy đối tượng phong_model
                pass
        phong_can_chinh_sua.luong_nguoi = luong_nguoi
        phong_can_chinh_sua.muc_dich = muc_dich
        phong_can_chinh_sua.tg_bd = tg_bd
        phong_can_chinh_sua.tg_kt = tg_kt

        id_bh_parts = id_buoihoc.split(',')
        if len(id_bh_parts) >= 1:
            # Lấy phần tử đầu tiên, có thể là id_phong hợp lệ
            id_bh_value = id_bh_parts[0]

            try:
                # Cố gắng chuyển đổi thành integer
                id_bh_int = int(id_bh_value)

                # Tìm đối tượng phong_model theo id_phong
                bh_instance = Buoi_Hoc_model.objects.get(id_buoihoc=id_bh_int)

                # Gán đối tượng phong_model cho csvc_to_edit.id_phong
                phong_can_chinh_sua.id_buoihoc = bh_instance
            except (ValueError, phong_model.DoesNotExist):
                # Xử lý trường hợp giá trị không thể chuyển đổi hoặc không tìm thấy đối tượng phong_model
                pass
        phong_can_chinh_sua.lop_hoc = lop_hoc
        phong_can_chinh_sua.nguoi_dat = nguoi_dat

        # Lưu các thay đổi
        phong_can_chinh_sua.save()
        return redirect('/')
    
#Chức năng sửa csvc     
def edit_csvc(request):
    if request.method == 'POST':
        csvc_id = request.POST['id_csvc']
        id_phong_str = request.POST['id_phong']
        loai_csvc = request.POST['loai_csvc']
        so_luong = request.POST['so_luong']

        a=id_phong_str.split(',')[3]

        existing_csvc = csvc_model.objects.filter(id_phongbase=id_phong_str[0], id_tencsvc=loai_csvc[0]).exclude(id_csvc=csvc_id).first()
        if existing_csvc:
            messages.error(request, f"Phòng {a} đã có csvc này rồi")
            return redirect(f'/csvc/{csvc_id}')
        
        # Tìm đối tượng csvc_model cần chỉnh sửa
        csvc_to_edit = get_object_or_404(csvc_model, id_csvc=csvc_id)

        # Phân tích chuỗi để lấy một giá trị có thể đại diện cho id_phong
        id_phong_parts = id_phong_str.split(',')
        if len(id_phong_parts) >= 1:
            # Lấy phần tử đầu tiên, có thể là id_phong hợp lệ
            id_phong_value = id_phong_parts[0]

            try:
                # Cố gắng chuyển đổi thành integer
                id_phong_int = int(id_phong_value)

                # Tìm đối tượng phong_model theo id_phong
                phong_instance = Phong_base_model.objects.get(id_phongbase=id_phong_int)

                # Gán đối tượng phong_model cho csvc_to_edit.id_phong
                csvc_to_edit.id_phongbase = phong_instance
            except (ValueError, phong_model.DoesNotExist):
                # Xử lý trường hợp giá trị không thể chuyển đổi hoặc không tìm thấy đối tượng phong_model
                pass
        id_loai_parts = loai_csvc.split(',')
        if len(id_loai_parts) >= 1:
            # Lấy phần tử đầu tiên, có thể là id_phong hợp lệ
            id_loai_value = id_loai_parts[0]

            try:
                # Cố gắng chuyển đổi thành integer
                id_loai_int = int(id_loai_value)

                # Tìm đối tượng phong_model theo id_phong
                loai_instance = Loai_CSVC_model.objects.get(id_tencsvc=id_loai_int)

                # Gán đối tượng phong_model cho csvc_to_edit.id_phong
                csvc_to_edit.id_tencsvc = loai_instance
            except (ValueError, phong_model.DoesNotExist):
                # Xử lý trường hợp giá trị không thể chuyển đổi hoặc không tìm thấy đối tượng phong_model
                pass        
        csvc_to_edit.so_luong = so_luong

        # Lưu lại sự thay đổi
        csvc_to_edit.save()

        return redirect('/')

#Chức năng tạo phòng
def create_phong(request):
    if request.method=='POST':
        toa=request.POST['toa']
        tang=request.POST['tang']
        phongg=request.POST['phongg']
        
        if toa=='' or phongg=='' or tang=='':
            messages.error(request,'Hãy nhập đầy đủ thông tin')
            return redirect('/tao-phong')

        expected_pattern = re.compile(rf"{toa}{tang}\d*")
        if not expected_pattern.fullmatch(phongg):
            messages.error(request,f'Cấu trúc tên phòng bắt buộc là Tòa+Tầng+Phòng.Ví dụ:{toa}{tang}01')
            return redirect('/tao-phong')

        existing_phong = Phong_base_model.objects.filter(toa=toa,tang=tang,phongg=phongg).exclude(id_phongbase=None).first()
        if existing_phong:
            messages.error(request, "Đã có phòng này rồi")
            return redirect('/tao-phong')
        
        try:
            phongmoi = Phong_base_model.objects.create(
                toa=toa,
                tang=tang,
                phongg=phongg
            )
            phongmoi.save()
            return redirect('/tao-phong')
        except Exception as e:
            messages.error(request, f"Có lỗi xảy ra: {e}")
            return redirect('/tao-phong')
    messages.error(request,"Thêm phòng không thành công")
    return redirect('/tao-phong')

#Xóa csvc    
def del_ph(request,id):
        vc_xoa=get_object_or_404(Loai_CSVC_model,id_tencsvc=id)
        vc_xoa.delete()
        return redirect('/tao-csvc')
#
def create_csvc(request):
    if request.method=='POST':
        ten_loaicsvc=request.POST['ten_loaicsvc']
        
        if ten_loaicsvc=='':
            messages.error(request,'Hãy nhập đầy đủ thông tin')
            return redirect('/tao-csvc')

        existing_csvc = Loai_CSVC_model.objects.filter(ten_loaicsvc=ten_loaicsvc).exclude(id_tencsvc=None).first()
        if existing_csvc:
            messages.error(request, f"Đã có {ten_loaicsvc} rồi")
            return redirect('/tao-csvc')
        
        try:
            csvcmoi = Loai_CSVC_model.objects.create(
                ten_loaicsvc=ten_loaicsvc,

            )
            csvcmoi.save()
            return redirect('/tao-csvc')
        except Exception as e:
            messages.error(request, f"Có lỗi xảy ra: {e}")
            return redirect('/tao-csvc')
    messages.error(request,"Thêm không thành công")
    return redirect('/tao-csvc')

#Xóa csvc    
def del_vc(request,id):
        p_xoa=get_object_or_404(Phong_base_model,id_phongbase=id)
        p_xoa.delete()
        return redirect('/tao-csvc')

#Chức năng sửa taocsvc     
def edit_taocsvc(request):
    if request.method == 'POST':
        id_tencsvc = request.POST['id_tencsvc']
        ten_loaicsvc=request.POST['ten_loaicsvc']

        if ten_loaicsvc=='':
            messages.error(request,'Hãy nhập đầy đủ thông tin')
            return redirect(f'/sua-ten-csvc/{id_tencsvc}')
        
        existing_csvc = Loai_CSVC_model.objects.filter(ten_loaicsvc=ten_loaicsvc).exclude(id_tencsvc=id_tencsvc).first()
        if existing_csvc:
            messages.error(request, f"Đã có {ten_loaicsvc} trong danh sách")
            return redirect(f'/sua-ten-csvc/{id_tencsvc}')
        
        # Tìm đối tượng csvc_model cần chỉnh sửa
        csvc_to_edit = get_object_or_404(Loai_CSVC_model, id_tencsvc=id_tencsvc)        
        csvc_to_edit.ten_loaicsvc = ten_loaicsvc

        # Lưu lại sự thay đổi
        csvc_to_edit.save()

        return redirect('/tao-csvc')
    
#Chức năng sửa taophong     
def edit_taophong(request):
    if request.method == 'POST':
        id_phongbase = request.POST['id_phongbase']
        toa= request.POST['toa']
        tang= request.POST['tang']
        phongg= request.POST['phongg']

        if toa=='' or phongg=='' or tang=='':
            messages.error(request,'Hãy nhập đầy đủ thông tin')
            return redirect(f'/sua-ten-Phong/{id_phongbase}')

        expected_pattern = re.compile(rf"{toa}{tang}\d*")
        if not expected_pattern.fullmatch(phongg):
            messages.error(request,f'Cấu trúc tên phòng bắt buộc là Tòa+Tầng+Phòng.Ví dụ:{toa}{tang}01')
            return redirect(f'/sua-ten-Phong/{id_phongbase}')

        existing_phong = Phong_base_model.objects.filter(toa=toa,tang=tang,phongg=phongg).exclude(id_phongbase=None).first()
        if existing_phong:
            messages.error(request, "Đã có phòng này rồi")
            return redirect(f'/sua-ten-Phong/{id_phongbase}')
        
        # Tìm đối tượng csvc_model cần chỉnh sửa
        phong_to_edit = get_object_or_404(Phong_base_model, id_phongbase=id_phongbase)        
        phong_to_edit.toa = toa
        phong_to_edit.tang = tang
        phong_to_edit.phongg = phongg

        # Lưu lại sự thay đổi
        phong_to_edit.save()

        return redirect('/tao-phong')