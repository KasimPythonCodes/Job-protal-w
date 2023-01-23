from pyproj import Geod

wgs84_geod = Geod(ellps='WGS84') #Distance will be measured on this ellipsoid - more accurate than a spherical method

#Get distance between pairs of lat-lon points

def Distance(lat1,lon1,lat2,lon2):
    az12,az21,dist = wgs84_geod.inv(lon1,lat1,lon2,lat2) #Yes, this order is correct
    print(dist)

Distance(1,2,3,4)






# import socket

# s = socket.socket()

# print("Created Socket ")

# s.bind(('localhost' , 9999))

# s.listen(3)
# print("waiting for connection")

# while True:
#     c, addr = s.accept()
#     name= c.recv(1024).decode()
#     print("Address " , addr , name)
    
#     c.send(bytes("welcome kasim saifi " , 'utf-8'))
    
#     c.close()


# import turtle

# turtle.bgcolor("black")
# squery = turtle.Turtle()
# squery.speed(20)
# squery.pencolor("red")
# for i in range(400):
#     squery.forward(i)
#     squery.left(91)
# # import datetime
# # def date_calculation(dob):
# #     today = datetime.datetime.now()
# #     print(today,"kkkkkkkkkkkkkkkkkkkk")
# #     birth_date = datetime.datetime.strptime(dob,'%Y-%m-%d')
# #     print(birth_date, "JJJJJJJJJJJJJJJJJJJJJJJJJJ")
# #     age = str((today - birth_date)/365)[:2] +" " + 'years'
# #     print(age,"AAAAAAAAAAAAAAAAAAAAAAAAAAA")
# #     return age
# # date_calculation("2000-2-25")

# # import os
# # cwd = os.getcwd() 
# # print(cwd)

# import sys
# import os
# import comtypes.client

# wdFormatPDF = 17

# in_file = os.path.abspath(sys.argv[0])
# out_file = os.path.abspath(sys.argv[1])

# word = comtypes.client.CreateObject('Word.Application')
# doc = word.Documents.Open(in_file)
# doc.SaveAs(out_file, FileFormat=wdFormatPDF)
# doc.Close()
# word.Quit()