## 医生小助手
### 功能

1. 处理Excel列提取
2. 计算肝病参数



### 命令

+ mac 打包命令

  ``` shell
  pyinstaller --onefile --windowed --icon res/img/apple.ico --add-data res/img/file70.svg:res/img --add-data res/img/apple.svg:res/img -D --name ICEHelper_mac Main.py
  ```

+ win 打包命令
  ```shell
  pyinstaller --add-data 'res/img/file70.svg:res/img/' --add-data 'res/img/apple.svg:res/img/' --icon './res/img/apple.ico' -wF --name ICEHelper_x64  main.py
  pyinstaller --add-data '.\res\QtSheetStyle.qrc:.\res' --icon './res/img/apple.ico' -wF --name ICEHelper_x64  main.py
  ```

  
### 版本信息

```shell
altgraph==0.17.4
certifi==2024.12.14
charset-normalizer==3.4.0
docopt==0.6.2
et_xmlfile==2.0.0
idna==3.10
macholib==1.16.3
numpy==2.2.0
openpyxl==3.1.5
packaging==24.2
pandas==2.2.3
pillow==11.0.0
pipreqs==0.4.13
pyinstaller==6.11.1
pyinstaller-hooks-contrib==2024.10
PyQt5==5.15.11
PyQt5-Qt5==5.15.15
PyQt5-stubs==5.15.6.0
PyQt5_sip==12.16.1
python-dateutil==2.9.0.post0
pytz==2024.2
requests==2.32.3
setuptools==75.6.0
six==1.17.0
tzdata==2024.2
urllib3==2.2.3
yarg==0.1.10
```