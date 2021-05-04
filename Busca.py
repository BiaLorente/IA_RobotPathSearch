from tkinter import *
import arcade

# colors
RED = (255, 122, 122)
BLUE = (167, 210, 221)
BROWN = (255, 194, 74)
GREEN = (103, 150, 114)
BLACK = (255, 255, 255)
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


def heuristic(a, b) -> float:
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)


class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.f = 0


def weight_key(Node):
    return Node.f


def ubs(maze, start, goal):
    # Create start and goal node
    costMatrix(maze)
    cont = 0
    start_node = Node(None, start)
    start_node.g = start_node.g = 0
    goal_node = Node(None, goal)
    goal_node.f = goal_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the goal
    while len(open_list) > 0:
        open_list.sort(key=weight_key)

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        # for index, item in enumerate(open_list):
        #     if item.f < current_node.f:
        #         current_node = item
        #         current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)
        for i in range(len(open_list)):
            print(f"Nodes em aberto na fronteira: {open_list[i].position}")
        for i in range(len(closed_list)):
            print(f"Nodes Fechados: {closed_list[i].position}")

        # Found the goal
        if current_node.position == goal_node.position:
            path = []
            current = current_node

            for i in range(len(open_list)):
                print(f"Nodes em aberto na fronteira: {open_list[i].position}")
            print("----------------------------------------------------------------")
            for i in range(len(closed_list)):
                print(f"Nodes Fechados: {closed_list[i].position}")
            print("----------------------------------------------------------------")

            current_node.g = current_node.g + maze[start[0]][start[1]]
            print(f'Numero de nodes na closed_list: {len(closed_list)}')
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
            flag: int = 0
            already_in_open: int = 0
            # Child is on the closed list
            for closed_child in range(len(closed_list)):
                if children[child].position == closed_list[closed_child].position:
                    flag = 1
                    continue
            # Create the f and g values
            if flag != 1:
                parent = children[child].parent
                children[child].g = parent.g + maze[children[child].position[0]][children[child].position[1]]
                children[child].f = children[child].g
                cont = cont + 1

                for open_node in range(len(open_list)):
                    if children[child].position == open_list[open_node].position:
                        if children[child].g < open_list[open_node].g:
                            open_list[open_node] = children[child]
                            already_in_open = 1
                            continue
                        else:
                            already_in_open = 1
                            continue
                    # x = open_list[open_node]
                    # open_list.remove(x)

                    # Add the child to the open list and
                if already_in_open != 1:
                    open_list.append(children[child])


def astar(maze, start, goal):
    """Returns a list of tuples as a path from the given start to the given goal in the given maze"""
    costMatrix(maze)
    # Create start and goal node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    goal_node = Node(None, goal)
    goal_node.g = goal_node.h = goal_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    # heapq.heappush(open_list, start_node)
    open_list.append(start_node)

    # Loop until you find the goal
    while len(open_list) > 0:

        # Get the current node
        open_list.sort(key=weight_key)
        current_node = open_list[0]
        current_index = 0

        # Pop current off open list, add to closed list
        # heapq.heappop(open_list)
        open_list.pop(current_index)
        # heapq.heappush(closed_list, current_node)
        closed_list.append(current_node)
        # maze[current_node.position[0]][current_node.position[1]] = 1
        for i in range(len(open_list)):
            print(f' Nos da open {open_list[i].position}')
        for i in range(len(closed_list)):
            print(f' Nos da close {closed_list[i].position}')
        # Found the goal
        if current_node.position == goal_node.position:
            path = []
            current = current_node
            custo_total = current.f
            tam = (len(closed_list))
            while current is not None:
                path.append(current.position)
                current = current.parent
            print(f'Custo total: {custo_total}')
            print(f'Total de nos visitados: {tam}')

            return path[::-1]  # Return reversed path

        # Generate children
        children = []

        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:  # Adjacent squares

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
            flag: int = 0
            already_in_open: int = 0
            # Child is on the closed list
            for closed_child in range(len(closed_list)):
                # print(f'no da closed list{closed_list[closed_child].position}')
                if children[child].position == closed_list[closed_child].position:
                    # children.pop(child)
                    # print(f'localizei que o nó {children[child].position} esta closed_list')
                    flag = 1
                    continue
            if flag != 1:
                # Create the f, g, and h values
                parent = children[child].parent
                children[child].g = parent.g + maze[children[child].position[0]][children[child].position[1]]
                children[child].h = heuristic(children[child].position, goal_node.position)
                children[child].f = children[child].g + children[child].h

                # Child is already in the open list
                for open_node in range(len(open_list)):
                    if children[child].position == open_list[open_node].position:
                        if children[child].g < open_list[open_node].g:
                            open_list[open_node] = children[child]
                            already_in_open = 1
                            continue
                        else:
                            already_in_open = 1
                            continue
                # x = open_list[open_node]
                # open_list.remove(x)

                # Add the child to the open list and
                if already_in_open != 1:
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
        # print(self.grid)
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
                elif self.grid[row][column] == 0:
                    color = BLACK
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


def call_map(a):
    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, a)
    arcade.run()


def call_ubs(m, start, goal, ubs_list):
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("---------------------------")
    path = ubs(m, start, goal)
    print(f'Caminho Busca Cega: {path}')
    print("---------------------------")


    for j in range(42):
        for i in range(42):
            for k in range(len(path)):
                if str(path[k]) == str((i, j)):
                    ubs_list[i][j] = 0

    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, ubs_list)
    arcade.run()


def call_astar(m, start, goal, astar_list):
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("---------------------------")
    path_astar = astar(m, start, goal)
    print(f'Caminho Astar: {path_astar}')
    print("---------------------------")

    for j in range(42):
        for i in range(42):
            for k in range(len(path_astar)):
                if str(path_astar[k]) == str((i, j)):
                    astar_list[i][j] = 0

    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, astar_list)
    arcade.run()

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
    map_list = []
    ubs_list = []
    astar_list = []
    for line in f.readlines():
        a.append([int(x) for x in line.split(',')])
        map_list.append([int(x) for x in line.split(',')])
        ubs_list.append([int(x) for x in line.split(',')])
        astar_list.append([int(x) for x in line.split(',')])
    start = (start.split(','))
    start = (int(start[0]), int(start[1]))
    goal = (goal.split(','))
    goal = (int(goal[0]), int(goal[1]))

    print(f'Matriz Original: {map_list}')
    print(f'Destino: {goal}')
    print(f'Origem: {start}')

    screen = Tk()
    screen.title("Buscas - IA")
    screen.geometry("300x200")
    screen.configure(bg='black')

    welcome_text = Label(text="| Buscas |", fg="blue", bg="gray")
    welcome_text.pack()

    click_me = Button(text="Busca A*", fg="blue", bg="gray", command=lambda: call_astar(a, start, goal, astar_list), width=20)
    click_me.place(x=75, y=50)
    click_me = Button(text="Busca BCCU", fg="blue", bg="gray", command=lambda: call_ubs(a, start, goal, ubs_list), width=20)
    click_me.place(x=75, y=75)
    click_me = Button(text="Mapa", fg="blue", bg="gray", command=lambda: call_map(map_list), width=20)
    click_me.place(x=75, y=100)
    click_me = Button(text="Fechar", fg="red", bg="gray", command=lambda: screen.destroy(), width=20)
    click_me.place(x=75, y=150)
    screen.mainloop()



if __name__ == "__main__":
    main()
