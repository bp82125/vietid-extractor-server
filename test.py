data = ['Số I No: 092041000207', 'Họ và tên I Full name', 'NGUYỄN HỒNG THOAI', 'Ngày sinh/Date of birth: 01/10/1941', 'Giới tính/ Sex: Nam Quốc tịch/Nationality: Việt Nam 1996', 'Quê quán I Place of origin:', 'Thị trấn Núi Sập, Thoại Sơn, An Giang', 'Nơi thường trú I Place of residence', '151, KV Yên Hạ;', 'Thường Thạnh, Cái Răng, Cần Thơ', 'có cho chỉ mỗ thời hạnh']

from image_processing.post_processing import process_text

print(process_text(data))