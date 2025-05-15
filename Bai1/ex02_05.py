so_gio = float(input("Nhập số giờ làm mỗi tuần: "))
luong_gio = float(input("Nhập thù lao trên mỗi giờ: "))
gio_tieu_chuan = 44
gio_vuot_tieu_chuan = max(0,so_gio - gio_tieu_chuan)
thuc_linh = gio_tieu_chuan * luong_gio + gio_tieu_chuan + luong_gio * 1.5
print("Số tiền thực lĩnh",thuc_linh)