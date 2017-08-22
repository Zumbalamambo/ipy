netsh interface ip set address name="本地连接" static 172.18.66.230 255.255.0.0 172.18.66.254 1 
netsh interface ip set dns name="本地连接" static 61.147.37.1 
ipconfig/all 
pause 
close