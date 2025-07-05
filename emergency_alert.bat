@echo off
adb shell am start -a android.intent.action.VIEW -d "sms:919790559885?body=EMERGENCY%20ALERT!%20Name:%20giugydtd,%20Contact:%2009y87rdhgjhbk,%20Location:%20Unknown,%20Lat:%2012.194895,%20Long:%2079.941625,%20Time:%2007/05/2025,%2004:29:37%20PM,%20Flood%20Height:%2045."
timeout /t 2 >nul
adb shell input tap 633 1421
