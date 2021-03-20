import imgui
import toolgui

@toolgui.window_update("Example/Hello World")
def hello_example():
    imgui.text("Hello!")

toolgui.start_toolgui_app()
