import tcod as libtcod
from input_handlers import handle_keys


def main():
    # screen size in pixels
    screen_width = 80
    screen_height = 50

    # player position
    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    # selecting a custom font through libtcod
    # using a picture of all the characters for the font
    libtcod.console_set_custom_font(
        "arial10x10.png", libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)

    # renders the actual window
    # boolean attribute is True if fullscreen
    libtcod.console_init_root(
        screen_width, screen_height, "roguelike tutorial", False)

    con = libtcod.console_new(screen_width, screen_height)

    key = libtcod.Key()
    mouse = libtcod.Mouse()

    # game loop
    while not libtcod.console_is_window_closed():
        # event listener for mouse and keypad input
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)

        # sets the colour for the @ symbol
        libtcod.console_set_default_foreground(con, libtcod.white)

        # puts the "@" on the screen, set's the background to "none"
        libtcod.console_put_char(
            con, player_x, player_y, "@", libtcod.BKGND_NONE)

        libtcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)

        # this puts everything on the screen
        libtcod.console_flush()

        libtcod.console_put_char(
            con, player_x, player_y, " ", libtcod.BKGND_NONE)

        action = handle_keys(key)

        move = action.get("move")
        exit = action.get("exit")
        fullscreen = action.get("fullscreen")

        if move:

            dx, dy = move
            player_x += dx
            player_y += dy

        # if the key is ESC...
        if exit:
            # exit window
            return True

        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())


if __name__ == '__main__':
    main()
