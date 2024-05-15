#include <stdio.h>
#include <stdlib.h>
#include "point.h"
#include "vector.h"
#include "geometry.h"

#define PI 3.14159265358979323846

int main()
{
    point *pt = alloc_point();
    float x = 0.0;
    float y = 2.3;
    init_point(pt, x, y);

    vector *v = alloc_vector();

    free_vector(v);
    free_point(pt);
    return 0;
}