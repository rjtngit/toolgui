import imgui
import toolgui

class State:
    menu_top_nodes = []


class MenuNode:
    def __init__(self, path, name, callback=None):
        self.path = path
        self.name = name
        self.callback = callback
        self.children = []


def menu_item(path):
    """
    @menu_item(Path)

    Decorator to call a static function from the main menu.
    Use forward slashes (/) to separate menu levels.
    """
    def dec(callback):
        add_menu_data(path, callback)
    return dec


def add_menu_data(path, callback):
    first_node_name = path.split("/", 1)[0]
    path_remainder = path.split("/", 1)[1]
    last_node_name = path.rsplit("/", 1)[1]
    leaf_node = MenuNode(path, last_node_name, callback)
    for node in State.menu_top_nodes:
        if first_node_name == node.name and not node.callback:
            build_tree(node, path_remainder, leaf_node)
            return
    first_node = MenuNode(first_node_name, first_node_name)
    build_tree(first_node, path_remainder, leaf_node)
    State.menu_top_nodes.append(first_node)


def build_tree(from_node, path, end_node):
    if path == end_node.name:
        from_node.children.append(end_node)
        return
    next_node_name = path.split("/", 1)[0]
    path_remainder = path.split("/", 1)[1]
    for child in from_node.children:
        if next_node_name == child.name and not child.callback:
            build_tree(child, path_remainder, end_node)
            return
    next_node = MenuNode(from_node.path + "/" + next_node_name, next_node_name)
    build_tree(next_node, path_remainder, end_node)
    from_node.children.append(next_node)


def update_menu_from_node(node):
    if node.callback:
        clicked, selected = imgui.menu_item(node.name)
        if clicked:
            node.callback()
    else:
        if imgui.begin_menu(node.name):
            for i, child in enumerate(node.children):
                update_menu_from_node(child)
            imgui.end_menu()


@toolgui.on_update()
def update_main_menu():
    if imgui.begin_main_menu_bar():
        for node in State.menu_top_nodes:
            update_menu_from_node(node)
        imgui.end_main_menu_bar()


def window(menu_path):
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