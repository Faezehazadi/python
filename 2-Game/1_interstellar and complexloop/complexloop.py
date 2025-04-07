import arcade

COLUMN_SPACING = 20
ROW_SPACING = 20
LEFT_MARGIN = 110
BOTTOM_MARGIN = 110

arcade.open_window(400, 400, "🔸 Complex Loops - Box 🔸")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()

for row in range(10):
    for column in range(10):
        x = column * COLUMN_SPACING + LEFT_MARGIN
        y = row * ROW_SPACING + BOTTOM_MARGIN
        if (column + row) %2 == 0 :
            color_draw = arcade.color.RED
        else:
            color_draw = arcade.color.BLUE_YONDER

        arcade.draw_rectangle_filled(x, y, 10, 10, color_draw, 45)

arcade.finish_render()
arcade.run()