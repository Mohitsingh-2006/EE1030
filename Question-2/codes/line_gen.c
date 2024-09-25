#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>

#include "./libs/matfun.h"

int main(void){
    double **A = createMat(2,1);
    double **B = createMat(2,1);
// A and are points on the line
    A[0][0] = 0; A[1][0] = 0;
    B[0][0] = 1; B[1][0] = 2;

    FILE *file;
    int len = 10;
    file = fopen("./lines.dat", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 0;
    }

    for (int i = 0; i <= 10; i++) {
       
        printMat(Matscale(A,2,1,i/10.0),2,1);

       
        fprintf(file, "%lf %lf\n",
            Matadd(A, Matscale(Matsub(B, A, 2, 1), 2, 1, i/10.0), 2, 1)[0][0],
            Matadd(A, Matscale(Matsub(B, A, 2, 1), 2, 1, i/10.0), 2, 1)[1][0]
            );
    }


   
    free(A);
    free(B);
    free(file);

    return 0;
}

