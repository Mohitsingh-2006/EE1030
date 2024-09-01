#include <stdio.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>

void matrix_multiply(float A[2][2], float B[2], float C[2]) {
    for(int i = 0; i < 2; i++) {
        C[i] = 0;
        for(int j = 0; j < 2; j++) {
            C[i] += A[i][j] * B[j];
        }
    }
}

void calculate_point_on_median(float x1, float y1, float x2, float y2, float m, float n, float* px, float* py) {
    float A[2][2] = {{m, n}, {m, n}};
    float B[2] = {x2, x1};
    float C[2];
    
    matrix_multiply(A, B, C);
    
    *px = C[0] / (m + n);
    *py = C[1] / (m + n);
}

int main() {
    float ax = 4, ay = 2;
    float bx = 6, by = 5;
    float cx = 1, cy = 4;
    float ex, ey, fx, fy;
    float qx, qy, rx, ry;
    float m = 2, n = 1;

    // Midpoints E and F
    ex = (ax + cx) / 2;
    ey = (ay + cy) / 2;
    fx = (ax + bx) / 2;
    fy = (ay + by) / 2;

    
    calculate_point_on_median(bx, by, ex, ey, m, n, &qx, &qy);
    calculate_point_on_median(cx, cy, fx, fy, m, n, &rx, &ry);

    FILE *output_file;
    output_file = fopen("output_coordinates.txt", "w");
    if (output_file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    fprintf(output_file, "The coordinates of point Q on median BE are: (%.2f, %.2f)\n", qx, qy);
    fprintf(output_file, "The coordinates of point R on median CF are: (%.2f, %.2f)\n", rx, ry);

    fclose(output_file);
    printf("Results have been written to output_coordinates.txt\n");

    return 0;
}

