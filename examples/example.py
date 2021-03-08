import toolgui


@toolgui.menu_item("Example/Print Hello")
def print_hello():
    print("Hello")


toolgui.start_toolgui_app()
