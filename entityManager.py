import entity
import screen
from random import randint

START_COUNT_HEALTHY = 740
START_COUNT_INFECTED = 10

entities = []
for i in range(START_COUNT_HEALTHY):
    entities.append(entity.Entity(randint(20, screen.WIDTH - 20), randint(20, screen.HEIGHT - 20)))
for i in range(START_COUNT_INFECTED):
    entities.append(entity.Entity(randint(20, screen.WIDTH - 20), randint(20, screen.HEIGHT - 20), True))

states = [START_COUNT_HEALTHY, START_COUNT_INFECTED]
def tick():
    for e in entities:
        e.tick()
        for j in range(entities.index(e), len(entities)):
            if e.collision(entities[j]) and e.infected != entities[j].infected:
                if e.infected:
                    entities[j].infected = True
                elif entities[j].infected:
                    e.infected = True

                states[0] -= 1
                states[1] += 1

def render(window):
    for e in entities:
        e.render(window)

def simOver():
    return states[0] == 0
