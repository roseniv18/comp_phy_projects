	#include <math.h>
	#include <stdbool.h>
	#include <time.h>
	#include <omp.h>
	#include <string.h>

	#ifndef M_PI
		#define M_PI 3.1415926
	#endif

	#define LAMBDA 650e-9L
	#define A 0.0L
	#define B 550e-6L
	#define STEPS 300
	#define PI 3.141592653589793238462643383279L
	
	// Wavenumber
	#define WAVENUM ((2 * PI) / LAMBDA)
	// Slice width
	#define SLICEW ((B - A) / (STEPS - 1.0L))
	
	long double const pi = M_PI;

	// Simulation parameters
	typedef struct {
		/* 
		 Number of steps in the integration
		 There is no point of the steps being over 10 000
		 because the algorithm will reach the limits of machine precision.
		 Computational Physics (Mark Newman) page 163 
		*/
		int steps;
		// Integration bounds
		long double a;
		long double b;
		// Wavelength
		long double lambda;
		int points;
		// Separation factor in intensity points.
		double separation;
	} SIM_PARAMS;

	const SIM_PARAMS sp = { 1000, 650e-9L, 0.0L, 550e-6L, 300, 4e-9 };

	// Intensity parameters
	typedef struct {
		// r - distance in the focal plane from the center of the diffraction pattern
		// Lower bound of r
		const long double r_a;
		// Upper bound of r (1 micro meter)
		const long double r_b;
		// Initial Intensity
		const int I0;
	} I_PARAMS;

	const I_PARAMS ip = { 0.0, 1e-6L, 1 };

	inline long double Jm(double m, long double x, long double theta);			
	long double Simpson(double m, long double x, long double (*fn)(double, long double, long double));
	long double I(long double r);
	void Intensity_vals(int points, int I0, double separation);
