import arcade
import heapq

# colors
RED = (255, 122, 122)
BLUE = (167, 210, 221)
BROWN = (255, 194, 74)
GREEN = (103, 150, 114)
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


class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.f = 0


def m_sort(open_list):
    for i in range(len(open_list)):
        min_idx = i
        for j in range(i + 1, len(open_list)):
            x = open_list[min_idx].g
            y = open_list[j].g
            if x > y:
                min_idx = j
        open_list[i], open_list[min_idx] = open_list[min_idx], open_list[i]


def ubs(maze, start, goal):
    # Create start and goal node
    start_node = Node(None, start)
    start_node.g = start_node.f = 0
    goal_node = Node(None, goal)
    goal_node.g = goal_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the goal
    while len(open_list) > 0:
        m_sort(open_list)

        # for i in range(len(open_list)):
        #     print(f"no {i}")
        #     print(open_list[i].g)

        print("------ New Node ---------")

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node.position == goal_node.position:
            path = []
            current = current_node
            current_node.g = current_node.g + maze[start[0]][start[1]]
            print(f'Custo total: {current_node.g}')
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]  # Return reversed path

        # Generate children
        children = []

        # Adjacent squares
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if (len(maze) - 1) >= node_position[0] >= 0 and (
                    (len(maze) - 1) >= node_position[1] >= 0):

                # Create new node
                new_node = Node(current_node, node_position)

                # Append
                children.append(new_node)

        # Loop through children
        for child in range(len(children)):

            # Child is on the closed list
            for closed_child in range(len(closed_list)):
                if children[child].position == closed_list[closed_child].position:
                    continue
            # Create the f and g values

            parent = children[child].parent
            children[child].g = parent.g + maze[children[child].position[0]][children[child].position[1]]
            children[child].f = children[child].g
            print(f'child {children[child].position}= g ={children[child].g} f= {children[child].f} ')

            # Child is already in the open list
            for open_node in range(len(open_list)):
                if children[child].position == open_list[open_node].position and children[child].g > open_list[open_node].g:
                    continue

            # Add the child to the open list
            open_list.append(children[child])


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title, matrix):
        """
        Set up the application.
        :param matrix:
        """
        super().__init__(width, height, title)
        # Create a 2 dimensional array. A two dimensional
        # array is simply a list of lists.
        self.grid = []
        self.grid = matrix
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
                    color = GREEN
                elif self.grid[row][column] == 2:
                    color = BROWN
                elif self.grid[row][column] == 3:
                    color = BLUE
                else:
                    color = RED
                # Do the math to figure out where the box is
                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2
                # Draw the box
                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)

    def on_update(self, delta_time: float):
        """
        Move everything. Perform collision checks. Do all the game logic here.
        :param float delta_time: Time interval since the last time the function was called.
        """
        pass


def costMatrix(a):
    for j in range(42):
        for i in range(42):
            if a[j][i] == 1:
                a[j][i] = 1
            if a[j][i] == 2:
                a[j][i] = 5
            if a[j][i] == 3:
                a[j][i] = 10
            if a[j][i] == 4:
                a[j][i] = 15


def main():
    f = open('ArvEstrada.txt', 'r')
    start = f.readlines()[0]
    f.close()
    f = open('ArvEstrada.txt', 'r')
    goal = f.readlines()[1]
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
    start = (start.split(','))
    start = (int(start[0]), int(start[1]))
    goal = (goal.split(','))
    goal = (int(goal[0]), int(goal[1]))
    # MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, a)
    # arcade.run()
    b = a
    print("Matriz sem custo")
    print(b)
    costMatrix(a)
    print("Matriz com custo")
    print(a)

    path = ubs(b, start, goal)
    print(path)


if __name__ == "__main__":
    main()
