@echo off


echo ����ѡ�񹤾�
echo ####################################################################
echo 1 ԭ������ 
echo 2 16��������


:0
echo ####################################################################
set /p num= ����1��2ѡ������ʹ�õ����壬�����س�ȷ�ϣ�


if %num% == 1 goto 1
if %num% == 2 goto 2
if %num% neq 1 (if "%num%" neq 2 goto other)



:1
echo.
echo.
echo.
echo ####################################################################
echo ��ѡ��ԭ������
del Data\font_data.xml 2>nul
del Textures\font.dds 2>nul
goto end


:2
echo.
echo.
echo.
echo ####################################################################
echo ��ѡ��16��������
copy Tools\Data\font_data.xml Data\font_data.xml >nul
copy Tools\Textures\font.dds Textures\font.dds >nul
goto end

:other
echo.
echo.
echo.
echo ####################################################################
set /p con= �����������Ч��ţ��Ƿ�����ѡ������y�����س�����

if %con% == y goto 0
if %num% neq y goto end


:end
echo ####################################################################
echo ��������˳�...
pause>nul


