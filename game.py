import types
import arcade
import Comp151Window
import time
#cannot get the cars and log to move
#can only get the player to collide once, but game doesnt end
#tried to create a backgrount but it won't


def main():
    window = Comp151Window.Comp151Window(800, 800, "first move demo")
    background = (800,800,'Untitled_Artwork.png')
    window.car_left = arcade.Sprite("car_left.gif")
    window.car_left.center_x = 220
    window.car_left.center_y = 220
    window.car_left_dx = 0
    window.car_left_dy = 0
    window.car_list = []
    window.car_left_list = []
    window.car_right = arcade.Sprite("car_right.gif")
    window.car_right.center_x = 220
    window.car_right.center_y = 300
   # window.car_right_dx = 0
   # window.car_right_dy = 0

    window.car_left2 = arcade.Sprite("car_left.gif")
    window.car_left2.center_x = 220
    window.car_left2.center_y = 380
   # window.car_left2_dx = 0
   # window.car_left2_dy = 0

    window.car_right2 = arcade.Sprite("car_right.gif")
    window.car_right2.center_x = 220
    window.car_right2.center_y = 460
   # window.car_right2_dx = 0
   # window.car_right2_dy = 0

    window.log = arcade.Sprite("log_full.gif")
    window.log.center_x = 600
    window.log.center_y = 600
   # window.log_dx = 0
   # window.log_dy = 0

    window.log2 = arcade.Sprite("log_full.gif")
    window.log2.center_x = 600
    window.log2.center_y = 690
   # window.log2_dx = 0
   # window.log2_dy = 0

    window.slime = arcade.Sprite("Slime_1.png")
    window.slime.center_x = 100
    window.slime.center_y = 100
    window.slime_dx = 0
    window.slime_dy = 0
    window.display_text = "SAFE ZONE!"
    add_cars(window)
    window.on_draw = types.MethodType(comp151_draw, window)
    window.on_key_press = types.MethodType(handle_key_press, window)
    #window.car1 = types.MethodType(motion, window)
    window.on_key_release = types.MethodType(handle_key_release, window)
    # key presses left and right
    arcade.run()
    #opens up window, coordinates for each picture


def comp151_draw(window):
    arcade.start_render()
    window.slime.draw()
    window.car_left.draw()
    window.car_left2.draw()
    window.car_right.draw()
    window.car_right2.draw()
    window.log.draw()
    window.log2.draw()
    if does_collide(window.slime, window.car_left):
        window.display_text = "LOSE!!"
    for car in window.car_list:
        car.draw()

    arcade.draw_text(window.display_text, 250, 50, arcade.color.ANTI_FLASH_WHITE, font_size=30)
    update_slime_location(window)
    update_car_left(window)
    arcade.finish_render()


def does_collide(sprite1, sprite2):
    return sprite1.collides_with_sprite(sprite2)

def does_collide_with_any_in_list(player, sprite_list):
    easy_list = arcade.SpriteList()
    easy_list.extend(sprite_list)
    return player.collides_with_list(easy_list)


def update_slime_location(window):
    if window.slime_dx != 0:
        window.slime.center_x += window.slime_dx
    if window.slime_dy !=0:
        window.slime.center_y += window.slime_dy
    if window.slime.center_x <-24:
        window.slime.center_x = 824
    if window.slime.center_x > 824:
        window.slime.center_x = -24
    if window.slime.center_y < -24:
        window.slime.center_y = 824
    if window.slime.center_y > 824:
        window.slime.center_y = -24
    #center y = up and down
    #center x = left and right

def update_car_left(window):
    if window.car_left_dx != 0:
        window.car_left.center_x += window.car_left_dx
    if window.car_left_dy != 0:
        window.car_left.center_y += window.car_left_dy
    if window.car_left.center_x < -24:
        window.slime.center_x = 824
    if window.car_left.center_x > 824:
        window.car_left.center_x = -24
    if window.car_left.center_y < -24:
        window.car_left.center_y = 824
    if window.car_left.center_y > 824:
        window.car_left.center_y = -24


def does_collide_with_any_in_list(player, sprite_list):
    easy_list = arcade.SpriteList()
    easy_list.extend(sprite_list)
    return player.collides_with_list(easy_list)

def handle_key_press(window, key, mod):
    if key == arcade.key.LEFT:
        window.slime_dx = -3
    elif key == arcade.key.RIGHT:
        window.slime_dx = 3
    elif key == arcade.key.UP:
        window.slime_dy = 3
    elif key == arcade.key.DOWN:
        window.slime_dy = -3


def handle_key_release(window, key, mod):
    if key == arcade.key.LEFT or key == arcade.key.RIGHT:
        window.slime_dx = 0
    elif key == arcade.key.UP or key == arcade.key.DOWN:
        window.slime_dy = 0


def add_cars(window):
    for car_number in range(5):
        current_sprite = arcade.Sprite("car_left.gif")
        current_sprite.center_x = 600
        current_sprite.center_y = 200
        window.car_list.append(current_sprite)
#adds 5 cars


main()