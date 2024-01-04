import pygame
import screen
import graph
import entityManager
#import sidebar
import time

pygame.init()

window = screen.screenSetup()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    graph.dataUpdate()
    window.fill(screen.BLACK)

    entityManager.tick()
    entityManager.render(window)

    #sidebar.render(window)

    time.sleep(0.05)

    pygame.display.update()

    if entityManager.simOver():
        graph.createGraph()