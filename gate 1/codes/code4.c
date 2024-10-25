#include <stdio.h>

void print_mat(int[][3]);

void main() {
    int i, j, sum = 0;
    int m[3][3] = {{1, 3, 5}, {7, 9, 11}, {13, 15, 17}};
    
    for (i = 0; i < 3; i++) {
        for (j = 2; j > 1; j--) {
            sum += m[i][j] * m[i][j - 1];
        }
    }
    
    printf("%d", sum);
    print_mat(m);  // FUNCTION CALL
}

void print_mat(int mat[][3]) {
    int (*p)[3] = &mat[1];
    printf("%d and %d", (*p)[1], (*p)[2]);
}

