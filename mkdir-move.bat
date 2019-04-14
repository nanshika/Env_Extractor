@title mkdir-move.bat

call :mkdir-move "Alice or Alice Siscon Niisan to Futago no Imouto"

exit 

:mkdir-move
mkdir %1
move *%1* %1
exit /b
