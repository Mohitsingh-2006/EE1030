#include <stdio.h>
#include <math.h>

#define PI 3.141592653589793

int main(void) {
    int num_points = 100;  // Change number of points to 100
    double r = 13.0 / 6.0;  // Radius of the circle
    double center_y = 13.0 / 6.0;  // y-coordinate of the center of the circle
    double theta;  // Angle variable
    double x, y;  // Coordinates of the points

    // Open file to write points
    FILE *file = fopen("circle_points.dat", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Calculate 100 points on the circle
    for (int i = 0; i < num_points; i++) {
        // Calculate angle (theta) for current point
        theta = 2 * PI * i / num_points;

        // Parametric equations of a circle
        x = r * cos(theta);
        y = r * sin(theta) + center_y;

        // Print the points to the file
        fprintf(file, "%lf %lf\n", x, y);
    }

    // Close the file
    fclose(file);

    printf("100 points on the circle have been saved to circle_points.dat.\n");
    return 0;
}

