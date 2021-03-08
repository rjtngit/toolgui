# toolgui

Simple app to manage imgui windows for development tools written in python. 

## Installation

```
pip install toolgui
```

## Usage

```python
import imgui
import toolgui


class State:
    window_enabled = False


@toolgui.menu_item("Example/Hello World")
def show_window():
    State.window_enabled = True


@toolgui.on_update()
def update_window():
    if State.window_enabled:
        expanded, opened = imgui.begin("Hello World", True)
        State.window_enabled = opened
        imgui.text("Hello world")
        imgui.end()


toolgui.start_toolgui_app()
```

