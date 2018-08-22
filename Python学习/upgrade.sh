@echo off
color 2f
mode con cols=60 lines=30
adb reboot bootloader
title EDAXX FASTBOOT Update
set device_lock=0
set count=0
fastboot oem device-info 2>&1 | findstr "Device.unlocked:.false" >lock_status || goto start 
set /p device_lock= <lock_status
del lock_status
echo Unlock device! Please wait 20s
fastboot oem unlock-go
:unlock_device
timeout /T 3
echo "Wait for unlock device, wiping data. %count%s."
fastboot devices > temp
set a=1
set /p a= <temp
del temp
if "%a%"=="1" (
    set /a count=%count%+3
	goto unlock_device
)

:start
cls
echo ----------------------------------------
echo    请选择你要进行的操作，然后按回车
echo ----------------------------------------
echo.
echo        1，完整升级     2，升级AP
echo        3, 升级MP       4，boot
echo        5，system       6，userdata
echo        7，recovery     8，splash6
echo        9，cache        a，persist
echo        b，emmc         q，退出 
echo.
set/p n=      请选择：
if "%n%"=="1" (goto all_update) 
if "%n%"=="2" (goto ap_update)
if "%n%"=="3" (goto mp_update)
if "%n%"=="4" (goto boot_update)
if "%n%"=="5" (goto system_update)
if "%n%"=="6" (goto userdata_update)
if "%n%"=="7" (goto recovery_update)
if "%n%"=="8" (goto splash_update)
if "%n%"=="9" (goto cache_update)
if "%n%"=="a" (goto persist_update)
if "%n%"=="b" (goto emmc_update)
if "%n%"=="q" (goto updata_exit)


:all_update 

echo erase misc and devinfo partition....
fastboot erase misc 
fastboot erase devinfo 

echo fastboot MP....
fastboot flash modem %~dp0\MP\NON-HLOS.bin
fastboot flash rpm %~dp0\MP\rpm.mbn
fastboot flash sbl1 %~dp0\MP\sbl1.mbn
fastboot flash tz %~dp0\MP\tz.mbn
fastboot flash devcfg %~dp0\MP\devcfg.mbn
fastboot flash dsp %~dp0\MP\adspso.bin
fastboot flash lksecapp %~dp0\MP\lksecapp.mbn
fastboot flash cmnlib %~dp0\MP\cmnlib_30.mbn
fastboot flash cmnlib64 %~dp0\MP\cmnlib64_30.mbn
fastboot flash keymaster %~dp0\MP\keymaster64.mbn

echo fastboot AP....
fastboot flash boot %~dp0\AP\boot.img
fastboot flash system %~dp0\AP\system.img
fastboot flash persist %~dp0\AP\persist.img
fastboot flash splash %~dp0\AP\splash.img
fastboot flash aboot %~dp0\AP\emmc_appsboot.mbn
fastboot flash vendor %~dp0\AP\vendor.img
fastboot flash IPSM %~dp0\AP\ipsm.img
fastboot flash mdtp %~dp0\AP\mdtp.img
fastboot flash misc %~dp0\AP\misc.img
fastboot flash secure %~dp0\AP\secure.img
fastboot flash license %~dp0\AP\license.img

goto userdata_update

:ap_update
echo fastboot AP....
fastboot flash boot %~dp0\AP\boot.img
fastboot flash system %~dp0\AP\system.img
fastboot flash persist %~dp0\AP\persist.img
fastboot flash splash %~dp0\AP\splash.img
fastboot flash aboot %~dp0\AP\emmc_appsboot.mbn
fastboot flash vendor %~dp0\AP\vendor.img
fastboot flash IPSM %~dp0\AP\ipsm.img
fastboot flash mdtp %~dp0\AP\mdtp.img
fastboot flash misc %~dp0\AP\misc.img
fastboot flash secure %~dp0\AP\secure.img
fastboot flash license %~dp0\AP\license.img
goto userdata_update

:mp_update
echo fastboot MP....
fastboot flash modem %~dp0\MP\NON-HLOS.bin
fastboot flash rpm %~dp0\MP\rpm.mbn
fastboot flash sbl1 %~dp0\MP\sbl1.mbn
fastboot flash tz %~dp0\MP\tz.mbn
fastboot flash devcfg %~dp0\MP\devcfg.mbn
fastboot flash dsp %~dp0\MP\adspso.bin
fastboot flash lksecapp %~dp0\MP\lksecapp.mbn
fastboot flash cmnlib %~dp0\MP\cmnlib_30.mbn
fastboot flash cmnlib64 %~dp0\MP\cmnlib64_30.mbn
fastboot flash keymaster %~dp0\MP\keymaster64.mbn
echo --------------------------
echo     ++++++++OK++++++++
echo --------------------------
pause
goto start

:boot_update
fastboot flash boot %~dp0\boot.img
echo --------------------------
echo     ++++++++OK++++++++
echo --------------------------
pause
goto start

:system_update
fastboot flash system %~dp0\system.img
echo --------------------------
echo     ++++++++OK++++++++
echo --------------------------
pause
goto start

:userdata_update
fastboot getvar emmc-capacity 2>&1 | findstr 0x
if %ERRORLEVEL% EQU 0 (
fastboot getvar emmc-capacity 2>&1 | findstr 0x747c00000 && fastboot flash userdata %~dp0\AP\userdata_32G.img 
fastboot getvar emmc-capacity 2>&1 | findstr 0x3ab400000 && fastboot flash userdata %~dp0\AP\userdata_16G.img
) else (fastboot flash userdata %~dp0\AP\userdata.img)
echo --------------------------
echo     ++++++++OK++++++++
echo --------------------------

if "%device_lock%"=="0" (
echo "warning: device unlock! %device_lock% "
) else (
echo "---lock device!----"
fastboot oem lock
)
pause
goto start

:recovery_update
fastboot flash recovery %~dp0\recovery.img
echo --------------------------
echo     ++++++++OK++++++++
echo --------------------------
pause
goto start

:splash_update
fastboot flash splash %~dp0\splash.img
echo --------------------------
echo     ++++++++OK++++++++
echo --------------------------
pause
goto start

:cache_update
fastboot flash cache %~dp0\cache.img
echo --------------------------
echo     ++++++++OK++++++++
echo --------------------------
pause
goto start

:persist_update
fastboot flash persist %~dp0\persist.img
echo --------------------------
echo     ++++++++OK++++++++
echo --------------------------
pause
goto start

:emmc_update
fastboot flash aboot %~dp0\emmc_appsboot.mbn
echo --------------------------
echo     ++++++++OK++++++++
echo --------------------------

if "%device_lock%"=="0" (
echo "warning: device is unlocked status! %device_lock% "
) else (
echo "---lock device!----"
fastboot oem lock
) 
pause
goto start

:updata_exit
fastboot reboot
exit
