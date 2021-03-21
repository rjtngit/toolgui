import glfw
import OpenGL.GL as gl

import imgui
from imgui.integrations.glfw import GlfwRenderer


class State:
    app_name = "toolgui"
    update_callbacks = []
    quit_callbacks = []
    start_callbacks = []


def on_update():
    """
    @on_update()

    Decorator to add a static function to the event loop to be called every frame.
    """
    def dec(callback):
        State.update_callbacks.append(callback)
    return dec

def on_app_quit():
    """
    @on_app_quit()

    Decorator to call a static function when the application quits.
    """
    def dec(callback):
        State.quit_callbacks.append(callback)
    return dec

def on_app_start():
    """
    @on_app_start()

    Decorator to call a static function when the application starts.
    """
    def dec(callback):
        State.start_callbacks.append(callback)
    return dec

def start_toolgui_app():
    """
    Start the application.
    """
    imgui.create_context()
    window = _impl_glfw_init()
    impl = GlfwRenderer(window)

    for on_start in State.start_callbacks:
        on_start()

    while not glfw.window_should_close(window):
        glfw.poll_events()
        impl.process_inputs()

        imgui.new_frame()

        for on_update in State.update_callbacks:
            on_update()

        gl.glClearColor(0, 0, 0, 0)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        imgui.render()
        impl.render(imgui.get_draw_data())
        glfw.swap_buffers(window)

    for on_quit in State.quit_callbacks:
        on_quit()

    impl.shutdown()
    glfw.terminate()


def _impl_glfw_init():
    width, height = 800, 600
    window_name = State.app_name

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
    State.app_name = name
