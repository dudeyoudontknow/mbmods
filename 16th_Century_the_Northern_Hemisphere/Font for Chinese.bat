@echo off


echo 字体选择工具
echo ####################################################################
echo 1 原版字体 
echo 2 16世纪字体


:0
echo ####################################################################
set /p num= 输入1或2选择你想使用的字体，并按回车确认：


if %num% == 1 goto 1
if %num% == 2 goto 2
if %num% neq 1 (if "%num%" neq 2 goto other)



:1
echo.
echo.
echo.
echo ####################################################################
echo 已选择原版字体
del Data\font_data.xml 2>nul
del Textures\font.dds 2>nul
goto end


:2
echo.
echo.
echo.
echo ####################################################################
echo 已选择16世纪字体
copy Tools\Data\font_data.xml Data\font_data.xml >nul
copy Tools\Textures\font.dds Textures\font.dds >nul
goto end

:other
echo.
echo.
echo.
echo ####################################################################
set /p con= 你输入的是无效序号，是否重新选择（输入y并按回车）：

if %con% == y goto 0
if %num% neq y goto end


:end
echo ####################################################################
echo 按任意键退出...
pause>nul


