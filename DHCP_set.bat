@title setIPAddressByDHCP.bat
netsh interface ipv4 set address "イーサネット アダプター" dhcp
netsh interface ipv4 set dns "イーサネット アダプター" dhcp
ipconfig /all
:: pause & exit
ping 8.8.8.8