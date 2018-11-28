ControlFocus("文件上传","","Edit1")  ;ControlFocus("title","text",controlID) Edit1=Edit instance 1  用于识别window窗口

WinWait("[CLASS:#32770]","",10) ;wait 10 seconds for the Upload window To appear

ControlSetText("文件上传","","Edit1","C:\\Users\\lixc\\Desktop\\productdata.txt") ;set the file name text on the Edit field
Sleep(2000)

ControlClick("文件上传","","Botton1") ;click on the open button