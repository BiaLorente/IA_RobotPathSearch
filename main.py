import arcade

# Set how many rows and columns we will have
ROW_COUNT = 42
COLUMN_COUNT = 42

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 15
HEIGHT = 15

# This sets the margin between each cell
# and on the edges of the screen.
MARGIN = 1

# Do the math to figure out our screen dimensions
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN
SCREEN_TITLE = "Robo Ambiente Busca Cega"


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title):
        """
        Set up the application.
        """

        super().__init__(width, height, title)

        # Create a 2 dimensional array. A two dimensional
        # array is simply a list of lists.
        self.grid = []

        f = open('ArvEstrada.txt', 'r')

        start = f.readlines()[0]

        print(start)

        f.close()

        f = open('ArvEstrada.txt', 'r')

        goal = f.readlines()[1]

        print(goal)

        f.close()

        a_file = open("ArvEstrada.txt", "r")

        lines = a_file.readlines()
        a_file.close()

        del lines[1]

        new_file = open("field.txt", "w+")

        for line in lines:
            new_file.write(line)

        new_file.close()

        a_file = open("field.txt", "r")

        lines = a_file.readlines()
        a_file.close()

        del lines[0]

        new_file = open("field.txt", "w+")

        for line in lines:
            new_file.write(line)

        new_file.close()

        f = open("field.txt", "r")

        f = open('field.txt', 'r')
        a = []
        for line in f.readlines():
            a.append([int(x) for x in line.split(',')])

        print(a)

        self.grid = a

        print(self.grid)

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """
        Render the screen.
        """
        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw the grid
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                # Figure out what color to draw the box
                if self.grid[row][column] == 1:
                    color = arcade.color.GREEN
                elif self.grid[row][column] == 2:
                    color = arcade.color.DARK_BROWN
                elif self.grid[row][column] == 3:
                    color = arcade.color.DARK_BLUE
                else:
                    color = arcade.color.ORANGE_RED

                # Do the math to figure out where the box is
                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

                # Draw the box
                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)


def main():
    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()
