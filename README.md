# PyQt5-Learn
Learn PyQt5  

- [reference](#reference)  
- [window](#window)  
- [statusbar](#statusbar)  
- [button](#button)  
- [signal_slot](#signalslot)  
- [messagebox](#messagebox)  
- [textbox](#textbox)  
- [absolute_position](#absolutepostion)  
- [menu](#menu)  
- [table](#table)  
- [tab](#tab)  
- [horizontal_layout](#horizontallayout)  
- [grid_layout](#gridlayout)  


## reference
https://pythonspot.com/pyqt5/  
[Qt中QMainWindow, QWidget以及QDialog的区别和选择](http://blog.csdn.net/Mengwei_Ren/article/details/71305885)  


## window  
`python3 window.py`   

![window](/Assets/window.png)   



## statusbar  
A statusbar can be added to the main window (QMainWindow).   

`python3 statusbar.py`  

![statusbar](/Assets/statusbar.png)  

we change 3 lines from window.py:  

```Python
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow  #add QMainWindow
class App(QMainWindow): #QWidget -> QMainWindow
self.statusBar().showMessage('Message in statusbar.')   #add
```


## button
`python3 button.py`  

![button](/Assets/button.png)  



## signal_slot
`python3 signal_slot.py`  

Used QVBoxLayout:  

![signal_slot](/Assets/signal_slot.png)  



## messagebox
`python3 messagebox.py`  

![messagebox](/Assets/messagebox.png)  



## textbox  
`python3 textbox.py`  

![textbox](/Assets/textbox.png)  



## absolute_postion
`python3 absolute_position.py`  

Widgets can be added on an absolute position using the move(x,y) method.  

![absolute_postion](/Assets/absolute_position.png)  



## menu  
`python3 menu.py`  

The top menu can be created with the method menuBar().  
Sub menus are added with addMenu(name).  

![menu](/Assets/menu.png)  



## table  
`python3 table.py`  

![table](/Assets/table.png)  



## tab   
`python3 tab.py`  

![tab](/Assets/tab.png)    



## horizontal_layout
`python3 horizontal_layout.py`  

![horizontal_layout](/Assets/horizontal_layout.png)  



## grid_layout  
`python3 grid_layout.py`  

![grid_layout](/Assets/grid_layout.png)  



## input_dialog 
`python3 input_dialog.py`  

![input_dialog](/Assets/input_dialog.png)  