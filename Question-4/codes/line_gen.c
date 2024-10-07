#include <stdio.h>
#include <math.h>

double function_parabola(double x) {
    return x * x;  // y = x^2
}

double function_line(double x, double m, double c) {
    return m * x + c;  // y = mx + c
}

void generate_points(double m, double c, double lower_limit, double upper_limit, double step_size, FILE *fptr) {
    for (double x = lower_limit; x <= upper_limit; x += step_size) {
        // Compute y values for both the parabola and the line
        double y_parabola = function_parabola(x);
        double y_line = function_line(x, m, c);

        // Write the points (x, y_parabola) and (x, y_line) to the file
        fprintf(fptr, "%lf, %lf, %lf\n", x, y_parabola, y_line);
    }
}

int main() {
    double m = 2.86, c = 2;  // Line equation y = mx + c
    double lower_limit = -5, upper_limit = 5;  // Range of x values
    double step_size = 0.1;  // Step size for generating points
    
    // Open the output file
    FILE *fptr;
    fptr = fopen("points.dat", "w");
    if (fptr == NULL) {
        printf("Error opening file!\n");
        return 1;
    }
    
    // Write header
    fprintf(fptr, "x, y_parabola, y_line\n");

    // Generate points and write them to the file
    generate_points(m, c, lower_limit, upper_limit, step_size, fptr);
    
    // Close the file
    fclose(fptr);

    printf("Points have been written to points.dat\n");
    
    return 0;
}

