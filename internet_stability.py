import matplotlib.pyplot as plt
import speedtest
import time

download_speed_list = []
upload_speed_list = []

for i in range(5):
    st = speedtest.Speedtest()
    download_speed = round(st.download(),1000000,2)
    download_speed_list.append(download_speed) 
    upload_speed = round(st.download(),1000000,2)
    upload_speed_list.append(upload_speed) 
    time.sleep(60)
    print(download_speed_list)
    print(upload_speed_list)

x = [1,2,3,4,5]

plt.plot(x, download_speed_list, label = "Download speed")
plt.plot(y, upload_speed_list, label = "upload speed")
plt.title("speed")
plt.show()



