import imgui
import toolgui

@toolgui.window("Example/Hello World")
def hello_example():
    imgui.text("Hello!")

toolgui.set_app_name("Hello World Example")
toolgui.start_toolgui_app()
