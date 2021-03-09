# toolgui

Simple event-driven GUI framework for building modular tools with Python and [ImGui](https://github.com/swistakm/pyimgui). 

![](https://github.com/rempelj/toolgui/raw/master/docs/images/toolgui.gif)

## Installation

```
pip install toolgui
```

## Usage

```python
import imgui
import toolgui

@toolgui.settings("example")
class Settings:
    window_open = False


@toolgui.menu_item("Example/Hello World")
def show_window():
    Settings.window_open = True


@toolgui.on_update()
def update_window():
    if Settings.window_open:
        expanded, Settings.window_open = imgui.begin("Hello World", True)
        imgui.text("Hello world")
        imgui.end()


toolgui.start_toolgui_app()
```

