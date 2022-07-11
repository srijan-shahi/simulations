#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"

int  main(void) //main function begins
{

//Sample size
int sz = 1000000;
 
//Uniform random numbers
uniform("../data/uni.dat", sz);

//Gaussian random numbers
gaussian("../data/gau.dat", sz);

//Mean of uniform
//printf("%lf",mean("uni.dat"));
return 0;
}


