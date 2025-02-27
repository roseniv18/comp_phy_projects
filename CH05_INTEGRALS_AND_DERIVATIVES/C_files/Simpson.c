#include <stdio.h>
#include <stdlib.h>
#include "Simpson.h"

int main() {
	// Begin clock
	float startTime = (float)clock();
	double startTime_parallel = omp_get_wtime();

	// Calculate intensity values.
	Intensity_vals(1000, ip.I0, sp.separation);

	// End clock
	float endTime = (float)clock();
	double endTime_parallel = omp_get_wtime();

	printf("\n");
	printf("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n");
	printf("[SERIAL]				Execution time: %.3f s\n", (endTime - startTime) / CLOCKS_PER_SEC);
	printf("[PARALLEL]				Execution time: %.3f s\n", (endTime_parallel - startTime_parallel));
	printf("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n");
	printf("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n");
	printf("PARAMETERS: \n");
	printf("[N] 					Number of steps: %d\n", sp.steps);
	printf("[lambda] 				Wavelength: %.1Le m\n", sp.lambda);
	printf("[p x p] 				Intensity points: %d x %d\n", sp.points, sp.points);
	printf("[r_a] 					r lower bound: %.1Le m\n", ip.r_a);
	printf("[r_b] 					r upper bound: %.1Le m\n", ip.r_b);
	printf("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n");
	printf("\n");


	return 0;
}

// Bessel Function of the first kind
inline long double Jm(double m, long double x, long double theta) {
	return cos(m*theta - x*sin(theta));
}

long double Simpson(double m, long double x, long double (*fn)(double, long double, long double)) {
	// Add check if number of subintervals (n-1) is even
	//...

	// Integral value
	long double I = fn(m, x, ip.r_a) + fn(m, x, ip.r_b);

	for(int k = 1; k < (sp.steps - 1); k++) {
		// Value at k-th step
		long double k_val = Jm(m, x, ip.r_a + (k * SLICEW));
		if(k % 2 != 0)
			I += 4 * k_val;
		else
			I += 2 * k_val;
	}
	I *= (SLICEW / 3);
	return I;
}

inline long double I(long double r) {
	long double SimpsonVal = Simpson(1.0, WAVENUM*r, Jm) / (WAVENUM*r);
	return r != 0.0 ? SimpsonVal * SimpsonVal : 0.0;
}

// Calculate intensity vals in the form of a points x points matrix.
// Afterwards, save the intensity vals to a file.
void Intensity_vals(int points, int I0, double separation) {
	FILE *fptr;
	fptr = fopen("intensity.txt", "w");

	if(fptr == NULL) {
		printf("Error opening file!\n");
		exit(1);
	}

	// char* buffer = malloc(points * points * 30 * sizeof(char));
	// char* buffer_ptr = buffer;

	long double* intensity_buf = malloc(points * points * sizeof(long double));

	// Buffer for file output
	int buffer_size = points * 30;  // Estimate size for each line
	char* write_buffer = malloc(buffer_size * sizeof(char));

	int half_points = points / 2;

	#pragma omp parallel for collapse(2)
	for (int i = 0; i < points; i++) {
		long double y = separation * (i - half_points);

		for (int j = 0; j < points; j++) {
			long double x = separation * (j - half_points);
			double r = sqrt((x * x) + (y * y));

			if (r < ip.r_b) {
				intensity_buf[i * points + j] = 0.5;
			} else {
				intensity_buf[i * points + j]	 = I0 * I(r);
			}
		}
	}

	// Write to the file in larger batches to reduce I/O overhead
	for (int i = 0; i < points; i++) {
		char* buffer_ptr = write_buffer;
		for (int j = 0; j < points; j++) {
			// Write each intensity value to the buffer (instead of directly to the file)
			buffer_ptr += sprintf(buffer_ptr, "%.9Le ", intensity_buf[i * points + j]);
		}
		sprintf(buffer_ptr, "\n");  // Newline at the end of each row

		// Write the entire buffer for this row to the file in one go
		fwrite(write_buffer, sizeof(char), strlen(write_buffer), fptr);
	}

	// Cleanup
	free(write_buffer);
	free(intensity_buf);
	fclose(fptr);
}
