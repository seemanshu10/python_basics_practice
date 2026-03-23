# My Project Title
sajfgvuyds

## Introduction

### h3

#### h4

##### ejrgbirfbg

this is **python file**

Welcome to my project! *This document will guide you* through the basics.

### Features
```
- jegruyergbre
- jiwerbfg
- Easy to use
- Flexible formatting
- Compatible with many platforms

```
### Installation
1. enriugjbuth
2. Open the project in your favorite text editor.
3. Start customizing!

[Open AI](https://chatgpt.com/)

![Open AI](panda.png)

![Open AI](https://cdn.pixabay.com/photo/2015/06/19/20/13/sunset-815270_640.jpg)


![Open AI](../assets/panda.png)


```python
import sys
from PySide2.QtWidgets import QApplication, QWidget, QLabel
from PySide2.QtCore import Qt

class KeyCheckExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Key Check Example")
        self.resize(300, 200)

        self.label = QLabel("Press A, B, or Space", self)
        self.label.move(50, 80)

    def keyPressEvent(self, event):
        print(Qt.Key_A)
        print(event.key())
        print("----")

        
        if event.key() == Qt.Key_A:
            self.label.setText("A Pressed")

        elif event.key() == Qt.Key_B:
            self.label.setText("B Pressed")

        elif event.key() == Qt.Key_Space:
            self.label.setText("Space Pressed")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = KeyCheckExample()
    window.show()
    sys.exit(app.exec_())


```

```json
{
    "name":"raj"

}
```

ksb  ~~jisdhgfuibdsuyfvb~~

- [ ] food
- [x] done task


* task1
* task 2
* task 3

[ ] have food
[x] done task
