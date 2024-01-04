import matplotlib.pyplot as plt
import entity
import entityManager

graphed = False
data = [[], []]

def dataUpdate():
    for i in range(len(entityManager.states)):
        data[i].append(entityManager.states[i])

def createGraph():
    global graphed
    if not graphed:
        plt.title("Entities Over Time")
        for j in range(len(data)):
            plt.plot([i for i in range(len(data[0]))], data[j])
        plt.legend(["Healthy", "Infected"])
        plt.xlabel("Ticks")
        plt.ylabel("Entities")
        plt.show()
        graphed = True

