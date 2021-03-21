import imgui
import toolgui

@toolgui.window("Example/Hello World")
def hello_example():
    imgui.text("Hello!")

toolgui.start_toolgui_app()
