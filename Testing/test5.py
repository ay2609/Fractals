import random
import matplotlib.pyplot as plt
import math

class Voronoi:
    def __init__(self, points):
        self.points = points
        self.diagram = self._compute_diagram()

    def _compute_diagram(self):
        # Compute the Voronoi diagram from the points
        diagram = compute_voronoi_diagram(self.points)
        return diagram

    def plot(self):
        # Plot the diagram using colors to show the Voronoi cells
        for point in self.points:
            plt.scatter(point[0], point[1], c=point.color)
        plt.show()

def compute_voronoi_diagram(points):
    # Create an empty diagram
    diagram = []

    # For each point, compute the Voronoi cell
    for point in points:
        cell = []
        nearest_point = None
        for other_point in points:
            # Add all points that are closer to the current point to the cell
            if distance(point, other_point) < distance(other_point, nearest_point):
                cell.append(other_point)
            # Keep track of the nearest point to the current point
            if nearest_point is None or distance(point, other_point) < distance(point, nearest_point):
                nearest_point = other_point
        # Add the cell to the diagram
        diagram.append(cell)

    return diagram


def distance(point1, point2):
    # Compute the distance between two points using the Euclidean formula
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)



# Generate a list of 10 random points
points = [(random.uniform(-10, 10), random.uniform(-10, 10)) for _ in range(10)]

# Use the points to create a Voronoi diagram
voronoi_diagram = Voronoi(points)

# Plot the diagram using colors to show the Voronoi cells
for point in voronoi_diagram.points:
    plt.scatter(point[0], point[1], c=point.color)
plt.show()

