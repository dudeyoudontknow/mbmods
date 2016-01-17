@echo off


echo 战场地图大小选择工具
echo ####################################################################
echo 1 标准战场地图 
echo 2 大型战场地图


:0
echo ####################################################################
set /p num= 输入1或2选择你想使用的战场地图大小，并按回车确认：


if %num% == 1 goto 1
if %num% == 2 goto 2
if %num% neq 1 (if "%num%" neq 2 goto other)



:1
echo.
echo.
echo.
echo ####################################################################
echo 已选择标准战场地图


copy scenes.txt Tools\scenes.txt >nul
(for /f "tokens=1,2 delims=:" %%a in ('findstr /n .* Tools\scenes.txt') do (

	if %%a equ 15 (echo scn_random_scene_steppe random_scene_steppe 1792 none none 0.000000 0.000000 830.000000 830.000000 -0.500000 0x00000000200005000006599600001c3f000031d0000051fa ) ^
	else if %%a equ 19 (echo scn_random_scene_plain random_scene_plain 1792 none none 0.000000 0.000000 830.000000 830.000000 -0.500000 0x00000000300005000006599600001c3f000031d0000051fa ) ^
	else if %%a equ 23 (echo scn_random_scene_snow random_scene_snow 1792 none none 0.000000 0.000000 830.000000 830.000000 -0.500000 0x00000000400005000006599600001c3f000031d0000051fa ) ^
	else if %%a equ 27 (echo scn_random_scene_desert random_scene_desert 1792 none none 0.000000 0.000000 830.000000 830.000000 -0.500000 0x00000000500005000006599600001c3f000031d0000051fa ) ^
	else if %%a equ 31 (echo scn_random_scene_steppe_forest random_scene_steppe_forest 1792 none none 0.000000 0.000000 830.000000 830.000000 -0.500000 0x00000000a00005000006599600001c3f000031d0000051fa ) ^
	else if %%a equ 35 (echo scn_random_scene_plain_forest random_scene_plain_forest 1792 none none 0.000000 0.000000 830.000000 830.000000 -0.500000 0x00000000b00005000006599600001c3f000031d0000051fa ) ^
	else if %%a equ 39 (echo scn_random_scene_snow_forest random_scene_snow_forest 1792 none none 0.000000 0.000000 830.000000 830.000000 -0.500000 0x00000000c00005000006599600001c3f000031d0000051fa ) ^
	else if %%a equ 43 (echo scn_random_scene_desert_forest random_scene_desert_forest 1792 none none 0.000000 0.000000 830.000000 830.000000 -0.500000 0x00000000d00005000006599600001c3f000031d0000051fa ) ^
	else (echo %%b)
))>scenes.txt

del Tools\scenes.txt 2>nul


goto end


:2
echo.
echo.
echo.
echo ####################################################################
echo 已选择大型战场地图


copy scenes.txt Tools\scenes.txt >nul
(for /f "tokens=1,2 delims=:" %%a in ('findstr /n .* Tools\scenes.txt') do (

	if %%a equ 15 (echo scn_random_scene_steppe random_scene_steppe 1792 none none 0.000000 0.000000 830.000000 830.000000 -0.500000 0x0000000321600808000d2348000043fe0000018e00004652 ) ^
	else if %%a equ 19 (echo scn_random_scene_plain random_scene_plain 1792 none none 0.000000 0.000000 830.000000 830.000000 -0.500000 0x0000000334400500000d234800006b9900002f78000017b6 ) ^
	else if %%a equ 23 (echo scn_random_scene_snow random_scene_snow 1792 none none 0.000000 0.000000 830.000000 830.000000 -0.500000 0x0000000340814b8c000d2348000043fe0000018e00004652 ) ^
	else if %%a equ 27 (echo scn_random_scene_desert random_scene_desert 1792 none none 0.000000 0.000000 830.000000 830.000000 -0.500000 0x00000003d0c10806000d2348000043fe0000018e00004652 ) ^
	else if %%a equ 31 (echo scn_random_scene_steppe_forest random_scene_steppe_forest 1792 none none 0.000000 0.000000 830.000000 830.000000 -0.500000 0x00000003ac66d39f000d2348000043fe0000018e00004652 ) ^
	else if %%a equ 35 (echo scn_random_scene_plain_forest random_scene_plain_forest 1792 none none 0.000000 0.000000 830.000000 830.000000 -0.500000 0x00000003bc689723000d2348000043fe0000018e00004652 ) ^
	else if %%a equ 39 (echo scn_random_scene_snow_forest random_scene_snow_forest 1792 none none 0.000000 0.000000 830.000000 830.000000 -0.500000 0x00000003cc6b9733000d2348000043fe0000018e00004652 ) ^
	else if %%a equ 43 (echo scn_random_scene_desert_forest random_scene_desert_forest 1792 none none 0.000000 0.000000 830.000000 830.000000 -0.500000 0x00000003dc650c17000d2348000043fe0000018e00004652 ) ^
	else (echo %%b)
))>scenes.txt

del Tools\scenes.txt 2>nul


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


