#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>

#include "libs/matfun.h"
#include "libs/geofun.h"

int main() {
	double **A,**B,**C,**E,**F,**Q,**R;
	A = createMat(2,1);
	B = createMat(2,1);
	C = createMat(2,1);
	F = createMat(2,1);
	E = createMat(2,1);
	A[0][0] = 4;
	A[1][0] = 2;
	B[0][0] = 6;
	B[1][0] = 5;
	C[0][0] = 1;
	C[1][0] = 4;
        F=Matsec(A,B,2,1);
        E=Matsec(A,C,2,1);
        Q=Matsec(B,E,2,2);
        R=Matsec(C,F,2,2);
	
	FILE *file;
	file = fopen("values.dat", "w");

	if (file == NULL) {
		printf("Error opening file!\n");
		return 1;
	}
	fprintf(file, "x y\n");
	fprintf(file, "%lf %lf \n", A[0][0],A[1][0]);
	fprintf(file, "%lf %lf \n", B[0][0],B[1][0]);
	fprintf(file, "%lf %lf \n", C[0][0],C[1][0]);
	fprintf(file, "%lf %lf \n", E[0][0],E[1][0]);
	fprintf(file, "%lf %lf \n", F[0][0],F[1][0]);
	fprintf(file, "%lf %lf \n", R[0][0],R[1][0]);
	fprintf(file, "%lf %lf \n", Q[0][0],Q[1][0]);
	
	
fclose(file);
	printf("Results have been written to values.dat\n");

	freeMat(A,2);
	freeMat(B,2);
	freeMat(C,2);
	freeMat(E,2);
	freeMat(F,2);
	freeMat(Q,2);
	freeMat(R,2);
	return 0;
	}
	
