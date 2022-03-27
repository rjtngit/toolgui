import imgui
import toolgui


@toolgui.settings("Number Picker")
class Settings:
    my_number = 0


class State:
    frame_count = 0


@toolgui.window("Example/Windows/Number Picker")
def number_picker():
    imgui.text(f"Frame count: {State.frame_count}")
    Settings.my_number = imgui.input_int("My Number", Settings.my_number, 1)[1]


@toolgui.menu_item("Example/Reset")
def reset():
    State.frame_count = 0
    Settings.my_number = 0


@toolgui.on_app_start()
def on_app_start():
    print("Application started")


@toolgui.on_app_quit()
def on_app_quit():
    print("Application quit")


@toolgui.on_update()
def on_update():
    State.frame_count += 1


toolgui.set_app_name("More Examples")
toolgui.start_toolgui_app()
