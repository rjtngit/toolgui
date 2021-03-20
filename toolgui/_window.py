import toolgui
import imgui

def window_update(menu_path):
    """
    @window_update(menu_path)

    Decorator for the update loop of a window that can be opened from the main menu bar.
    """
    def dec(update_func):
        @toolgui.settings(menu_path)
        class Settings:
            window_open = False

        @toolgui.menu_item(menu_path)
        def show_window():
            Settings.window_open = True

        @toolgui.on_update()
        def update_window():
            if Settings.window_open:
                window_name = menu_path.rsplit("/", 1)[1]
                expanded, Settings.window_open = imgui.begin(window_name, True)
                update_func()
                imgui.end()
    return dec