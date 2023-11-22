import matplotlib.pyplot as plt
import pandas as pd

# Create a DataFrame from the image data
data = {
    "Activity i": [1, 2, 3, 4, 5],
    "Starting Time": [2, 3, 4, 1, 8],
    "Finishing Time": [3, 4, 6, 7, 9]
}

df = pd.DataFrame(data)


# File path to save the image
file_path = './activity_graph_p2.png'

# Plotting the graph again and saving to the local disk
plt.figure(figsize=(4, 3))

# Plotting the activities with their start and finish times
for _, row in df.iterrows():
    plt.plot([row['Starting Time'], row['Finishing Time']], [row['Activity i'], row['Activity i']], 'bo-', label=f"Activity {row['Activity i']}")

# Formatting the plot
plt.xlabel('Time')
plt.ylabel('Activities')
plt.title('Activities Start and Finish Times')
plt.grid(True)
# plt.legend()
plt.yticks(df['Activity i'])

# Save the figure
plt.savefig(file_path)

# Close the plot to avoid displaying it in the output
plt.close()

file_path
