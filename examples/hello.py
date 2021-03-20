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
