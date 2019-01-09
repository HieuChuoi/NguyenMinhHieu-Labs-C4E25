
import time;

localtime = time.localtime(time.time())
print ("Thoi gian hien tai la :", localtime)

localtime = time.asctime( time.localtime(time.time()) )
print ("Thoi gian da duoc dinh dang la :", localtime)