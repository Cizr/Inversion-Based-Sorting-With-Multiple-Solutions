def draw_path_not_found(win, draw, grid, rows, grid_width, grid_height):
    # win.fill(WHITE)
    
    for row in grid:
        for cell in row:
            if cell.is_visited() or cell.is_in_queue():
                cell.set_no_path()
    
    draw()
    time.sleep(0.6)
    
    for i in range(6):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               pygame.quit()
        
        for row in grid:
            for cell in row:
                if cell.is_no_path():
                    cell.set_unvisited()
                elif cell.is_unvisited():
                    cell.set_no_path()
        draw()
        time.sleep(0.6)
    
    draw_grid_lines(win, rows, grid_width, grid_height)
    pygame.display.update()

# Buttons #####################################################################
# Values for Window Size = 1300X680 and Grid Size = 1280X580
spacing = 5
button_width = 180
button_height = 45
button_radius = 30
button_font = pygame.font.SysFont("Georgia", 15, bold=False, italic=False)

# Algorithm Buttons
dijkstra_surf = button_font.render("Dijkstra's Algorithm", True, BLACK)
dijkstra_button = Button(spacing, 5, button_width, button_height, text_surface=dijkstra_surf, border_radius=button_radius, color=LAPIS_LAZULI)
dijkstra_button.set_secondary_button_color(LIGHT_LAPIS_LAZULI)

a_star_surf = button_font.render("A* Search", True, BLACK)
a_star_button = Button((2*spacing) + button_width, 5, button_width, button_height, text_surface=a_star_surf, border_radius=button_radius, color=VERDIGRIS)
a_star_button.set_secondary_button_color(LIGHT_VERDIGRIS)

bidirectional_surf = button_font.render("Bidirectional Search", True, BLACK)
bidirectional_button = Button((3*spacing) + (2*button_width), 5, button_width, button_height, text_surface=bidirectional_surf, border_radius=button_radius, color=EMERALD)
bidirectional_button.set_secondary_button_color(LIGHT_EMERALD)

bfs_surf = button_font.render("Breadth-First Search", True, BLACK)
bfs_button = Button((4*spacing) + (3*button_width), 5, button_width, button_height, text_surface=bfs_surf, border_radius=button_radius, color=LIGHT_GREEN_1)
bfs_button.set_secondary_button_color(LIGHT_GREEN_2)

dfs_surf = button_font.render("Depth-First Search", True, BLACK)
dfs_button = Button((5*spacing) + (4*button_width), 5, button_width, button_height, text_surface=dfs_surf, border_radius=button_radius, color=TEA_GREEN)
dfs_button.set_secondary_button_color(DARK__TEA_GREEN)

# Clear Button
clear_surf = button_font.render("CLEAR", True, BLACK)
clear_button = Button((6*spacing) + (5*button_width), 5, button_width, button_height, text_surface=clear_surf, border_radius=button_radius, color=RED)
clear_button.set_secondary_button_color(LIGHT_RED)

# Random Maze Button
maze_surf = button_font.render("Generate Random Maze", True, BLACK)
maze_button = Button((7*spacing) + (6*button_width), 5, button_width, button_height, text_surface=maze_surf, border_radius=button_radius, color=ORANGE)
maze_button.set_secondary_button_color(LIGHT_ORANGE)

# Helper Functions ############################################################
def update_cell_neighbors(grid):
    for row in grid:
        for cell in row:
            cell.update_neighbors(grid)
    return

def draw_stationary_objects(win):
    pygame.draw.rect(win, DARK_SLATE_GRAY, (0, 0, WIN_WIDTH, 55))
    
    # Algorithm buttons
    dijkstra_button.draw(win)
    a_star_button.draw(win)
    bidirectional_button.draw(win)
    bfs_button.draw(win)
    dfs_button.draw(win)
    
    # Clear button
    clear_button.draw(win)
    
    # Generate Random Maze button
    maze_button.draw(win)
    
    # Legend
    # Values for Window Size = 1300X680 and Grid Size = 1280X580
    cube_size = 25
    spacing = 5
    legend_font = pygame.font.SysFont("Georgia", 20, bold=False, italic=False)
    
    # Legend - Start
    pygame.draw.rect(win, GREEN, (GRID_LEFT_BUFFER + 20, GRID_TOP_BUFFER - (cube_size + 5), cube_size, cube_size))
    text_visited_surf = legend_font.render("Start Cell", True, DARK_SLATE_GRAY)
    win.blit(text_visited_surf, (GRID_LEFT_BUFFER + cube_size + spacing + 20, GRID_TOP_BUFFER - (cube_size + 5)))
    
    # Legend - End
    pygame.draw.rect(win, RED, (GRID_LEFT_BUFFER + 216, GRID_TOP_BUFFER - (cube_size + 5), cube_size, cube_size))
    text_visited_surf = legend_font.render("End Cell", True, DARK_SLATE_GRAY)
    win.blit(text_visited_surf, (GRID_LEFT_BUFFER + cube_size + spacing + 216, GRID_TOP_BUFFER - (cube_size + 5)))
    
    # Legend - Wall
    pygame.draw.rect(win, DARK_SLATE_GRAY, (GRID_LEFT_BUFFER + 416, GRID_TOP_BUFFER - (cube_size + 5), cube_size, cube_size))
    text_visited_surf = legend_font.render("Wall/Obstacle Cell", True, DARK_SLATE_GRAY)
    win.blit(text_visited_surf, (GRID_LEFT_BUFFER + cube_size + spacing + 416, GRID_TOP_BUFFER - (cube_size + 5)))
    
    # Legend - Unvisited
    pygame.draw.rect(win, DARK_SLATE_GRAY, (GRID_LEFT_BUFFER + 696, GRID_TOP_BUFFER - (cube_size + 5), cube_size, cube_size), width=1)
    text_visited_surf = legend_font.render("Unvisited Cells", True, DARK_SLATE_GRAY)
    win.blit(text_visited_surf, (GRID_LEFT_BUFFER + cube_size + spacing + 696, GRID_TOP_BUFFER - (cube_size + 5)))
    
    # Legend - Visited Cells
    pygame.draw.rect(win, DODGER_BLUE, (GRID_LEFT_BUFFER + 956, GRID_TOP_BUFFER - (cube_size + 5), cube_size, cube_size))
    pygame.draw.rect(win, LIGHT_GRAY, (GRID_LEFT_BUFFER + 986, GRID_TOP_BUFFER - (cube_size + 5), cube_size, cube_size))
    text_visited_surf = legend_font.render("Visited Cells", True, DARK_SLATE_GRAY)
    win.blit(text_visited_surf, (GRID_LEFT_BUFFER + cube_size + spacing + 986, GRID_TOP_BUFFER - (cube_size + 5)))
    
    # Legend - Path
    pygame.draw.rect(win, GOLD, (GRID_LEFT_BUFFER + 1190, GRID_TOP_BUFFER - (cube_size + 5), cube_size, cube_size))
    text_visited_surf = legend_font.render("Path", True, DARK_SLATE_GRAY)
    win.blit(text_visited_surf, (GRID_LEFT_BUFFER + cube_size + spacing + 1190, GRID_TOP_BUFFER - (cube_size + 5)))
    return

# Main Function ###############################################################
def main(win, rows, grid_width, grid_height):
    grid = generate_grid(rows, grid_width, grid_height)
    cols = len(grid[0])
    
    START = grid[random.randrange(0, rows, 2)][random.randrange(0, cols, 2)]
    START.set_start()
    END = grid[random.randrange(0, rows, 3)][random.randrange(0, cols, 3)]
    END.set_end()
    
    running = True
    algorithm_started = False
    algorithm_completed = False
    path_found = False
    
    while running:
        WIN.fill(WHITE) # Refresh the screen to clear the previous content
        
        draw_stationary_objects(win)
        draw_grid(win, grid, rows, grid_width, grid_height)
        
        for event in pygame.event.get():
            # User can press X (close button) to quit anytime
            if event.type == pygame.QUIT:
               running = False
               break
            
            # User should not be able to change anything while an algorithm is running
            # User can still quit anytime
            if algorithm_started:
                continue
            
            # User can click CLEAR button to clear the grid
            if clear_button.draw(win):
                algorithm_completed = False
                path_found = False
                reset_grid(grid)
                if START:
                    START.set_start()
                if END:
                    END.set_end()
            
            # User should not be able to change grid after an algorithm is completed
            # User can still clear the grid
            if algorithm_completed:
                continue
            
            # Left click
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                if click_in_grid(pos):
                    row, col = get_clicked_cell(pos, rows, grid_width, grid_height)
                    cell = grid[row][col]
                    if not START and cell != END:
                        START = cell
                        START.set_start()
                    elif not END and cell != START:
                        END = cell
                        END.set_end()
                    elif cell != START and cell != END:
                        cell.set_wall()
            
            # Right click
            if pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()    
                if click_in_grid(pos):
                    row, col = get_clicked_cell(pos, rows, grid_width, grid_height)
                    cell = grid[row][col]
                    cell.reset()
                    if cell == START:
                        START = None
                    elif cell == END:
                        END = None
            
            # Generate Random Maze
            if maze_button.draw(win) and not algorithm_started:
                algorithm_started = True
                reset_grid(grid)
                if START:
                    START.set_start()
                if END:
                    END.set_end()
                generate_random_maze(0, 0, cols, rows, grid, lambda: draw_grid(win, grid, rows, grid_width, grid_height))
                algorithm_started = False
            
            if not algorithm_started and START and END:
                # Start Dijkstra's algorithm
                if dijkstra_button.draw(win):
                    algorithm_started = True
                    update_cell_neighbors(grid)
                    path_found = dijkstra_algorithm(lambda: draw_grid(win, grid, rows, grid_width, grid_height), grid, START, END)
                    if not path_found:
                        draw_path_not_found(win, lambda: draw_grid(win, grid, rows, grid_width, grid_height), grid, rows, grid_width, grid_height)
                    algorithm_started = False
                    algorithm_completed = True
                # Start A* Search algorithm
                elif a_star_button.draw(win):
                    algorithm_started = True
                    update_cell_neighbors(grid)
                    path_found = a_star_search_algorithm(lambda: draw_grid(win, grid, rows, grid_width, grid_height), grid, START, END)
                    if not path_found:
                        draw_path_not_found(win, lambda: draw_grid(win, grid, rows, grid_width, grid_height), grid, rows, grid_width, grid_height)
                    algorithm_started = False
                    algorithm_completed = True
                # Start Bidirectional Search algorithm
                elif bidirectional_button.draw(win):
                    algorithm_started = True
                    update_cell_neighbors(grid)
                    path_found = bidirectional_search_algorithm(lambda: draw_grid(win, grid, rows, grid_width, grid_height), grid, START, END)
                    if not path_found:
                        draw_path_not_found(win, lambda: draw_grid(win, grid, rows, grid_width, grid_height), grid, rows, grid_width, grid_height)
                    algorithm_started = False
                    algorithm_completed = True
                # Start BFS algorithm
                elif bfs_button.draw(win):
                    algorithm_started = True
                    update_cell_neighbors(grid)
                    path_found = BFS_algorithm(lambda: draw_grid(win, grid, rows, grid_width, grid_height), grid, START, END)
                    if not path_found:
                        draw_path_not_found(win, lambda: draw_grid(win, grid, rows, grid_width, grid_height), grid, rows, grid_width, grid_height)
                    algorithm_started = False
                    algorithm_completed = True
                # Start DFS algorithm
                elif dfs_button.draw(win):
                    algorithm_started = True
                    update_cell_neighbors(grid)
                    path_found = DFS_algorithm(lambda: draw_grid(win, grid, rows, grid_width, grid_height), grid, START, END)
                    if not path_found:
                        draw_path_not_found(win, lambda: draw_grid(win, grid, rows, grid_width, grid_height), grid, rows, grid_width, grid_height)
                    algorithm_started = False
                    algorithm_completed = True
        
        # Update the screen to show the content
        pygame.display.update()
        # Limit FPS to 60
        CLOCK.tick(60)
        
    pygame.quit()
    return
main(WIN, GRID_ROWS, GRID_WIDTH, GRID_HEIGHT)