import glfw
import OpenGL.GL as gl

import imgui
from imgui.integrations.glfw import GlfwRenderer

from toolgui import _menu

class AppData:
    app_name = "toolgui"
    update_callbacks = []


def on_update():
    """
    @on_update()

    Decorator to add a static function to the event loop to be called every frame.
    """
    def dec(callback):
        AppData.update_callbacks.append(callback)
    return dec


def start_toolgui_app():
    """
    Start the application.
    """
    imgui.create_context()
    window = _impl_glfw_init()
    impl = GlfwRenderer(window)

    while not glfw.window_should_close(window):
        glfw.poll_events()
        impl.process_inputs()

        imgui.new_frame()

        _menu.update_main_menu()
        for update_callback in AppData.update_callbacks:
            update_callback()

        gl.glClearColor(0, 0, 0, 0)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        imgui.render()
        impl.render(imgui.get_draw_data())
        glfw.swap_buffers(window)

    impl.shutdown()
    glfw.terminate()


def _impl_glfw_init():
    width, height = 800, 600
    window_name = AppData.app_name

    if not glfw.init():
        print("Could not initialize OpenGL context")
        exit(1)

    # OS X supports only forward-compatible core profiles from 3.2
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, gl.GL_TRUE)

    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(
        int(width), int(height), window_name, None, None
    )
    glfw.make_context_current(window)

    if not window:
        glfw.terminate()
        print("Could not initialize Window")
        exit(1)

    return window


def set_app_name(name):
    """
    Set the name of the application.
    """
    AppData.app_name = name
