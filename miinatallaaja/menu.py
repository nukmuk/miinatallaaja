import os

import functions as f
import sweeperlib as ui
import inputs
import stats


def get_btn_pos():
    start_btn_x = f.XRES / 2
    start_btn_y = f.YRES / 2
    return start_btn_x, start_btn_y


TEXT_OFFSET = 80


def load():
    ui.set_draw_handler(draw_handler)
    ui.set_mouse_handler(mouse_handler)
    f.XRES = f.XRES_START
    f.YRES = f.YRES_START
    ui.resize_window(f.XRES, f.YRES)


def draw_handler():
    btn_x, btn_y = get_btn_pos()
    ui.clear_window()
    ui.draw_background()

    ui.begin_sprite_draw()

    ui.prepare_sprite("1", 40, 10)
    ui.prepare_sprite("duck", 100, 10)

    ui.draw_sprites()

    f.draw_text_custom("miinatallaaja😻", f.XRES / 2, f.YRES - f.YRES / 4, size=48)

    f.draw_text_custom("start", btn_x, btn_y)
    f.draw_text_custom("print stats", btn_x, btn_y - TEXT_OFFSET)
    f.draw_text_custom("quit", btn_x, btn_y - TEXT_OFFSET * 2)


def mouse_handler(x, y, btn, mod):
    # print(x, y, btn, mod)
    btn_x, btn_y = get_btn_pos()

    start_game = f.button_in_range(x, y, btn_x, btn_y, 120, 40)
    stats_clicked = f.button_in_range(x, y, btn_x, btn_y - TEXT_OFFSET, 120, 40)
    quit_clicked = f.button_in_range(x, y, btn_x, btn_y - TEXT_OFFSET * 2, 120, 40)
    if start_game:
        inputs.load()
    elif stats_clicked:
        print(stats.get_scores_nice())
    elif quit_clicked:
        # quit()
        os._exit(1)
