import datetime

loop = True
while loop:
    now = datetime.datetime.now()
    if now.hour == 7:
        from gmail import GMail, Message
        gmail = GMail("haongo7979@gmail.com","haohao79")
        msg = Message("Don xin nghi lam", to="tranhuyen19122000@gmail.com", text="em xin nghi lam vi bi om")
        print("send")
        loop = False
    else:
        pass


# for i in list:
#     if i >= 7:
#         from gmail import GMail, Message
#         gmail = GMail("haongo7979@gmail.com","haohao79")
#         msg = Message("Don xin nghi lam", to="tranhuyen19122000@gmail.com", text="em xin nghi lam vi bi om")
#         print("send")
#     else:
#         pass
