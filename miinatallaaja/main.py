import inputs
import sweeperlib as ui
import functions as f
import menu
import tallaaja

graphics = {
    "window": None,
    "background": None,
    "bg_color": None,
    "batch": None,
    "sprites": [],
    "images": {},
}

handlers = {
    "timeouts": [],
}


ui.load_sprites("sprites")
ui.load_duck("images")
ui.create_window(f.XRES, f.YRES, (0, 0, 0, 255))

# ui.set_draw_handler(menu.draw_handler)
# ui.set_mouse_handler(menu.mouse_handle

# ui.set_draw_handler(input.draw_handler)
# ui.set_mouse_handler(input.mouse_handler)
# ui.set_keyboard_handler(input.keyboard_handler)
# ui.set_interval_handler(input.interval_handler, 1)

menu.load()

CURSOR_BLINK_DELAY = 0.5

ui.set_interval_handler(tallaaja.timer, 1)
ui.set_interval_handler(inputs.cursor_blink, CURSOR_BLINK_DELAY)

ui.start()
