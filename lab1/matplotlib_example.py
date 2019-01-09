from matplotlib import pyplot

#1. Prepare data
machine_counts = [18, 4, 2]

#2. Prepare labels
machine_name = ["PC", "Mac", "Linux"]

#3. Draw pie
pyplot.pie(machine_counts, labels = machine_name, autopct="%.1f%%", shadow=True, explode=[0, 0.2, 0])
pyplot.axis("equal")
pyplot.title("PC vs Mac vs Linux usage")

#4. Show
pyplot.show()