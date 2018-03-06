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
- [input_dialog](#inputdialog)  
- [file_dialog](#filedialog)  
- [image](#image)  
- [image](#pixel)  
- [color_dialog](#colordialog)  
- [color](#color)  
- [drag_drop](#dragdrop)  
- [font_dialog](#fontdialog)  
- [matplotlib](#matplotlib)  
- [browser](#browser)  
- [treeview](#treeview)  
- [directory_view](#directoryview)  
- [form_layout](#formlayout)  
- [box_layout](#boxlayout)  
- [wizard](#wizard)  

## reference
[pythonspot](https://pythonspot.com/pyqt5/)    
[PyQt5中文教程](http://code.py40.com/pyqt5/), or [PyQt5 tutorial](http://zetcode.com/gui/pyqt5/)  
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



## file_dialog  
`python3 file_dialog.py`  

![file_dialog](/Assets/file_dialog.png)  



## image
`python3 image.py`  

![image](/Assets/image.png)  



## pixel
`python3 pixel.py`  

![pixel](/Assets/pixel.png)   




## color_dialog
`python3 color_dialog.py`  

![color_dialog](/Assets/color_dialog.png)   



## color
`python3 color.py`  

![color](/Assets/color.png)  



## drag_drop
`python3 drag_drop.py`  

![drag_drop](/Assets/drag_drop.png)  



## font_dialog
`python3 font_dialog.py`  

![font_dialog](/Assets/font_dialog.png)  



## matplotlib
Firstly, install matplotlib: `pip3 install matplotlib`  

`python3 plot.py`  

![matplotlib](/Assets/matplotlib.png)  


## browser  

>The **QtWebEngineWidgets** module contains classes for a Chromium based implementation of a web browser. This supercedes the **QtWebKit** module and provides better and up-to-date support for HTML, CSS and JavaScript features. However it also consumes more resources and doesn’t give direct access to the network stack and the HTML document via Python APIs.


`python3 browser.py`  

![browser](/Assets/browser.png)



## treeview
`python3 treeview.py`  

![treeview](/Assets/treeview.png)  



## directory_view  
`python3 directory_view.py`  

![directory_view](/Assets/directory_view.png)  




## form_layout
`python3 form_layout.py`  

![form_layout](/Assets/form_layout.png)  



## box_layout
`python3 box_layout.py`   

![box_layout](/Assets/box_layout.png)   



---



## wizard
`python3 wizard.py`  

![wizard](/Assets/wizard.png)  