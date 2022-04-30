import os

import glfw
import OpenGL.GL as gl

import imgui
from imgui.integrations.glfw import GlfwRenderer

import toolgui


class State:
    app_name = "toolgui"
    style = {}
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


def init_style(window, impl):
    # font
    win_w, win_h = glfw.get_window_size(window)
    fb_w, fb_h = glfw.get_framebuffer_size(window)
    font_scaling_factor = max(float(fb_w) / win_w, float(fb_h) / win_h)
    font_size_in_pixels = 14
    io = imgui.get_io()
    font_path = os.path.join(os.path.dirname(toolgui.__file__), "Roboto-Regular.ttf")
    State.style["font"] = io.fonts.add_font_from_file_ttf(
        font_path, font_size_in_pixels * font_scaling_factor,
        io.fonts.get_glyph_ranges_default()
    )
    io.font_global_scale /= font_scaling_factor
    impl.refresh_font_texture()

    # colors
    style = imgui.get_style()
    imgui.style_colors_light(style)
    style.colors[imgui.COLOR_BORDER] = (1, 1, 1, 1)


def push_style():
    imgui.push_font(State.style["font"])


def pop_style():
    imgui.pop_font()


def start_toolgui_app():
    """
    Start the application.
    """
    imgui.create_context()
    window = _impl_glfw_init()
    impl = GlfwRenderer(window)

    init_style(window, impl)

    for on_start in State.start_callbacks:
        on_start()

    while not glfw.window_should_close(window):
        glfw.poll_events()
        impl.process_inputs()

        imgui.new_frame()

        push_style()
        for on_update in State.update_callbacks:
            on_update()
        pop_style()

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

