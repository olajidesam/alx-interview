def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the triangle with the first row [1]

    # Generate the remaining rows
    for i in range(1, n):
        prev_row = triangle[-1]  # Get the previous row
        new_row = [1]  # Start the new row with 1

        # Calculate the values in between using the sum of two consecutive elements from the previous row
        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])

        new_row.append(1)  # End the new row with 1
        triangle.append(new_row)  # Add the new row to the triangle

    return triangle

# Test the function
if __name__ == "__main__":
    def print_triangle(triangle):
        for row in triangle:
            print("[{}]".format(",".join([str(x) for x in row])))

    triangle_5 = pascal_triangle(5)
    print_triangle(triangle_5)
