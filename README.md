# toolgui

Modular event-driven GUI system for quickly building tools with Python and [pyimgui](https://github.com/swistakm/pyimgui). 

![](https://github.com/rempelj/toolgui/raw/master/docs/images/toolgui.gif)

## Installation

```
pip install toolgui
```

## Usage
### Window

Create a window that can be opened from the menu bar.

```python
import imgui
import toolgui

@toolgui.window("Example/Hello World")
def hello_example():
    imgui.text("Hello!")

toolgui.set_app_name("toolgui example")
toolgui.start_toolgui_app()
```

### Settings

Persist state across sessions. Data is saved to the `toolgui.ini` file.

```python
import imgui
import toolgui

@toolgui.settings("Number Picker")
class Settings:
    my_number = 0

@toolgui.window("Example/Number Picker")
def number_picker():
    Settings.my_number = imgui.input_int("My Number", Settings.my_number, 1)[1]

toolgui.set_app_name("toolgui example")
toolgui.start_toolgui_app()

```

### Menu Item

Call a static function from the menu bar. 

```python
@toolgui.menu_item("Example/Reset")
def reset():
    Settings.my_number = 0
```

### Events
Event functions are executed by toolgui with these decorators.

#### Application Start
Executed when the application starts.
```python
@toolgui.on_app_start()
def on_app_start():
    # do_something()
```

#### Application Quit
Executed when the application quits.
```python
@toolgui.on_app_quit()
def on_app_quit():
    # do_something()
```

#### Update
Executed every frame.
```python
@toolgui.on_update()
def on_update():
    # do_something()
```
