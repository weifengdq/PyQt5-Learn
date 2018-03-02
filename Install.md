- Install  
    -[macOS](#macos)  
    -[Windows](#windows)   

# macOS  
PyQt相关安装步骤如下:  
* 安装Apple Command Line Tools: xcode-select --install
* 安装Qt, 官网下载, 在线安装
* 安装Python3 从官网下载
* 安装SIP: sudo pip3 install sip
* 安装PyQt5: sudo pip3 install PyQt5

安装Eric6这个IDE方便开发:  
sudo pip3 install qscintilla  
sudo python3 install.py  

如果双击.ui文件打不开, 可以 Eric6->Prefenrences: 

![Eric6P](/Assets/Eric6P.png)  

默认的Qt路径是这个: 
/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/PyQt5/Qt/translations
可能是哪里装的不对.   


# Windows  

注意打开powershell或者cmd的时候, 用 **管理员身份**.   

## 安装Python3

从 [Python官网](https://www.python.org/) 下载2.x和3.x的安装包安装.  

Windows装完python2和python3后, 发现cmd里面出现两种情况之一:   
1. 输入python是python 2 , 输入python3不识别.  
2. 输入python是python3, 输入python2不识别.   

打开环境变量, 确定图中的4个路径都已经添加上去:  

![Path](/Assets/path.png)  

找到Python36的路径, 把python.exe重命名为python3.exe.  

pip或者pip3可能无法识别, 用 **管理员身份** 运行powershell或者cmd, 重装pip:  

```
python3 -m pip install --upgrade pip --force-reinstall
python -m pip install --upgrade pip --force-reinstall
```

输入以下命令:   

```
python -V
python3 -V
pip -V
pip3 -V
```  

![Version](/Assets/version.png)  

## 安装PyQt5相关  
 用 **管理员身份** 运行powershell或者cmd:  
**安装PyQt5**:  `pip3 install PyQt5`  
**安装PyQt相关工具**: `pip3 install PyQt5-tools`  
**安装QScintilla**: `pip3 install QScintilla`  
**安装Eric6**: 下载 https://eric-ide.python-projects.org/eric-download.html, 解压, 切换到解压的目录, `python3 install.py`  

安装的PyQt5的路径: %\Python36-32\Lib\site-packages\PyQt5  
安装的PyQt5-tools的路径: %\Python36-32\Lib\site-packages\pyqt5-tools, 把这个路径添加到 环境变量 里面. 

**安装自动补全**: `pip3 install jedi`, 打开Eric6 -> Pulgins -> Plugins Repository, 找到Completions, Jedi. 下载安装.  还要在Setting -> Preferences -> Editor -> Autocompletion -> Jedi -> 勾选Enable autocompletion.