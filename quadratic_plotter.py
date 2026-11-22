import numpy as np
import matplotlib.pyplot as plt


def plot_quadratic_from_input():
    """
    Interactive quadratic function plotter that takes user input
    """
    print("Quadratic Function Plotter")
    print("Enter coefficients for f(x) = ax² + bx + c")

    try:
        # Get user input
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))

        # Generate x values
        x = np.linspace(-10, 10, 400)
        y = a * x**2 + b * x + c

        # Calculate important points
        vertex_x = -b / (2 * a)
        vertex_y = a * vertex_x**2 + b * vertex_x + c

        # Create the plot
        plt.figure(figsize=(12, 8))
        plt.plot(x, y, 'b-', linewidth=3, label=f'f(x) = {a}x² + {b}x + {c}')

        # Plot vertex
        plt.plot(vertex_x, vertex_y, 'ro', markersize=10,
                 label=f'Vertex ({vertex_x:.2f}, {vertex_y:.2f})')

        # Plot y-intercept
        plt.plot(0, c, 'go', markersize=8, label=f'y-intercept (0, {c})')

        # Calculate and plot roots if they exist
        discriminant = b**2 - 4 * a * c
        if discriminant >= 0:
            root1 = (-b + np.sqrt(discriminant)) / (2 * a)
            root2 = (-b - np.sqrt(discriminant)) / (2 * a)
            plt.plot([root1, root2], [0, 0], 'ms', markersize=8,
                     label=f'Roots: ({root1:.2f}, 0), ({root2:.2f}, 0)')

        # Customize the plot
        plt.axhline(y=0, color='black', linewidth=0.5)
        plt.axvline(x=0, color='black', linewidth=0.5)
        plt.grid(True, alpha=0.3)
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title(f'Quadratic Function: f(x) = {a}x² + {b}x + {c}')
        plt.legend()

        # Set appropriate axis limits
        plt.xlim(-10, 10)
        y_margin = (max(y) - min(y)) * 0.1
        plt.ylim(min(y) - y_margin, max(y) + y_margin)

        plt.show()

        # Print function properties
        print("\nFunction Properties:")
        print(f"Equation: f(x) = {a}x² + {b}x + {c}")
        print(f"Vertex: ({vertex_x:.2f}, {vertex_y:.2f})")
        print(f"Axis of symmetry: x = {vertex_x:.2f}")
        print(f"Opens: {'Upward' if a > 0 else 'Downward'}")
        print(f"Y-intercept: (0, {c})")
        print(f"Discriminant: {discriminant}")

        if discriminant > 0:
            print(f"Two real roots: x = {root1:.2f} and x = {root2:.2f}")
        elif discriminant == 0:
            print(f"One real root (double root): x = {root1:.2f}")
        else:
            print("No real roots (complex roots)")

    except ValueError:
        print("Please enter valid numbers for coefficients!")
    except ZeroDivisionError:
        print("Coefficient 'a' cannot be zero for a quadratic function!")


# Run the interactive plotter
if __name__ == "__main__":
    plot_quadratic_from_input()
