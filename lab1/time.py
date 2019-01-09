import time;

localtime = time.localtime(time.time())
print ("Thoi gian hien tai la :", localtime)


    # tm_year	Trả về năm hiện tại (ví dụ: 2019)
    # tm_mon	Trả về tháng hiện tại (1-12)
    # tm_mday	Trả về ngày hiện tại (1-31)
    # tm_hour	Trả về giờ hiện tại (0-23)
    # tm_min	Trả về phút hiện tại (0-59)
    # tm_sec	Trả về giây hiện tại (0-61 với 60 và 61 là các dây nhuận)
    # tm_wday	Trả về ngày trong tuần (0-6 với 0 là Monday)
    # tm_yday	Trả về ngày trong năm (1-366 kể cả năm nhuận)
    # tm_isdst	Trả về -1, 0 hoặc 1 tức là có xác định DST không
