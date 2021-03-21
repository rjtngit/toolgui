# toolgui

Modular event-driven GUI system for quickly building tools with Python and [pyimgui](https://github.com/swistakm/pyimgui). 

![](https://github.com/rempelj/toolgui/raw/master/docs/images/toolgui.gif)

## Installation

```
pip install toolgui
```

## Usage

```python
import imgui
import toolgui


@toolgui.window("Example/Hello World")
def hello_example():
    imgui.text("Hello!")


toolgui.start_toolgui_app()
```

