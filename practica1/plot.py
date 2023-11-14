import matplotlib.pyplot as plt

def plot(x, y, labels,  title):
    fig, ax = plt.subplots()
    
    ax.bar(x=x,height = y, tick_label=labels )
    ax.set_title(title)
    
    plt.show()