import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


# Define the font properties
font = fm.FontProperties(fname='arial.ttf', size=50)

# Create a blank figure and axes
fig, ax = plt.subplots(1)

# Set the background color to white
ax.set_facecolor('white')

# Get user input
input_text = input("Enter text: ")

# if the input is "amour", display it
if input_text == "amour":
    ax.text(0.5, 0.5, input_text, fontproperties=font, horizontalalignment='center',
            verticalalignment='center', transform=ax.transAxes, color='black')
    plt.show()
# otherwise display it for 1 sec and clear the screen
else:
    ax.text(0.5, 0.5, input_text, fontproperties=font, horizontalalignment='center',
            verticalalignment='center', transform=ax.transAxes, color='black')
    plt.show(block=False)
    plt.pause(1)
    plt.clf()
