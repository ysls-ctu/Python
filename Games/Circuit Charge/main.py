import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Circuit Charge")

# Define colors
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Define component sizes
COMPONENT_SIZE = 50
GRID_SIZE = 50
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Define components
toolbox = {
    "Battery": pygame.transform.scale(pygame.image.load("Games/Circuit Charge/battery.png"), (COMPONENT_SIZE, COMPONENT_SIZE)),
    "Resistor": pygame.transform.scale(pygame.image.load("Games/Circuit Charge/resistor.png"), (COMPONENT_SIZE, COMPONENT_SIZE)),
    "LightBulb": pygame.transform.scale(pygame.image.load("Games/Circuit Charge/lightbulb.png"), (COMPONENT_SIZE, COMPONENT_SIZE)),
    "Wire": pygame.transform.scale(pygame.image.load("Games/Circuit Charge/wire.png"), (COMPONENT_SIZE, COMPONENT_SIZE))
}

# Store placed components on the grid
placed_components = []

# Function to draw the grid
def draw_grid():
    for x in range(0, SCREEN_WIDTH, GRID_SIZE):
        pygame.draw.line(screen, GRAY, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, GRAY, (0, y), (SCREEN_WIDTH, y))

# Function to draw the toolbox
def draw_toolbox():
    toolbox_rect = pygame.Rect(0, SCREEN_HEIGHT - COMPONENT_SIZE, SCREEN_WIDTH, COMPONENT_SIZE)
    pygame.draw.rect(screen, GRAY, toolbox_rect)
    for i, (component, image) in enumerate(toolbox.items()):
        screen.blit(image, (i * COMPONENT_SIZE, SCREEN_HEIGHT - COMPONENT_SIZE))

# Function to check if component is placed on the grid
def is_on_grid(pos):
    return pos[0] >= 0 and pos[1] >= 0 and pos[0] < SCREEN_WIDTH and pos[1] < SCREEN_HEIGHT

# Function to check if component is already placed on a specific grid position
def is_occupied(pos):
    return any(component[1] == pos for component in placed_components)

# Function to check if component is connected to another component
def is_connected(pos):
    return any((pos[0] + dx, pos[1] + dy) in [component[1] for component in placed_components] for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)])

# Function to draw wires between connected components
def draw_wires():
    for component in placed_components:
        if component[0] == "Wire":
            pos = component[1]
            neighbors = [(pos[0] + dx, pos[1] + dy) for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]]
            for neighbor in neighbors:
                if neighbor in [comp[1] for comp in placed_components]:
                    pygame.draw.line(screen, GREEN, (pos[0] + COMPONENT_SIZE // 2, pos[1] + COMPONENT_SIZE // 2), (neighbor[0] + COMPONENT_SIZE // 2, neighbor[1] + COMPONENT_SIZE // 2), 3)

# Function to check if circuit is complete
def is_circuit_complete():
    return all(component[0] == "LightBulb" for component in placed_components if component[1][1] == 0)

# Game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if toolbox component clicked
            mouse_pos = pygame.mouse.get_pos()
            for i, (component, image) in enumerate(toolbox.items()):
                component_rect = pygame.Rect(i * COMPONENT_SIZE, SCREEN_HEIGHT - COMPONENT_SIZE, COMPONENT_SIZE, COMPONENT_SIZE)
                if component_rect.collidepoint(mouse_pos):
                    selected_component = component
                    if selected_component == "Wire":
                        start_pos = (i * COMPONENT_SIZE + COMPONENT_SIZE // 2, SCREEN_HEIGHT - COMPONENT_SIZE // 2)
        elif event.type == pygame.MOUSEBUTTONUP:
            # Place component on the grid
            mouse_pos = pygame.mouse.get_pos()
            if selected_component:
                grid_x = mouse_pos[0] // GRID_SIZE * GRID_SIZE
                grid_y = mouse_pos[1] // GRID_SIZE * GRID_SIZE
                grid_pos = (grid_x, grid_y)
                if selected_component != "Wire":
                    if is_on_grid(grid_pos) and not is_occupied(grid_pos):
                        placed_components.append((selected_component, grid_pos))
                else:  # If Wire is selected
                    end_pos = (grid_x + COMPONENT_SIZE // 2, grid_y + COMPONENT_SIZE // 2)
                    if is_on_grid(grid_pos) and not is_occupied(grid_pos) and is_connected(grid_pos):
                        placed_components.append((selected_component, grid_pos))
                        placed_components.append(("Wire", end_pos))
                selected_component = None

    # Draw the grid, toolbox, wires, and placed components
    screen.fill(WHITE)
    draw_grid()
    draw_toolbox()
    draw_wires()
    for component, pos in placed_components:
        screen.blit(toolbox[component], pos)

    # Check if circuit is complete and display result
    if is_circuit_complete():
        pygame.draw.rect(screen, GREEN, (0, 0, SCREEN_WIDTH, COMPONENT_SIZE))
        font = pygame.font.SysFont(None, 36)
        text = font.render("Circuit Complete!", True, WHITE)
        screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, COMPONENT_SIZE // 2 - text.get_height() // 2))

    # Update the display
    pygame.display.flip()
