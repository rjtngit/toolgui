import imgui
import toolgui


class Example:
    custom_window_enabled = False
    test_window_enabled = False


@toolgui.menu_item("Examples/Show Custom Window")
def show_custom_window():
    Example.custom_window_enabled = True


@toolgui.on_update()
def update_custom_window():
    if Example.custom_window_enabled:
        expanded, opened = imgui.begin("Custom window", True)
        Example.custom_window_enabled = opened
        imgui.text("Hello custom window")
        imgui.end()


@toolgui.menu_item("Examples/Show Test Window")
def show_test_window():
    Example.test_window_enabled = True


@toolgui.on_update()
def update_test_window():
    if Example.test_window_enabled:
        imgui.show_test_window()


toolgui.start_toolgui_app()
