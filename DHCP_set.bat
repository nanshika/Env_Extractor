@title setIPAddressByDHCP.bat
netsh interface ipv4 set address "�C�[�T�l�b�g �A�_�v�^�[" dhcp
netsh interface ipv4 set dns "�C�[�T�l�b�g �A�_�v�^�[" dhcp
ipconfig /all
:: pause & exit
ping 8.8.8.8