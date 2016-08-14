@echo off

echo.

echo Enter Password :
set /p name=
if %name%==redhat (
	
	start Xming.exe
	
	set /p Dum=Hit Enter To Install Xming Fonts
	
	start Xmingfonts.exe
	
	set /p D=Hit Enter to continue
	
	start putty.exe -ssh -X root@192.168.0.8 -pw redhat

)
else (echo Password Not Valid!!!)
)
set /p Dummy=Hit Enter To Exit
