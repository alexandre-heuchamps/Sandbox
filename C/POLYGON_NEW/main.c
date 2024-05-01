#include <stdio.h>
#include <stdlib.h>
#include "point.h"
#include "vector.h"

#define PI 3.14159265358979323846

int main()
{
    point *pt = alloc_point();
    float x = 0.0;
    float y = 2.3;
    init_point(pt, x, y);

    point *pt_rot = alloc_point();
    init_point(pt_rot, 0.0, 0.0);
    rotate_point(pt, pt_rot, 0.25 * PI);

    vector *v = alloc_vector();
    set_origin_vector(v, pt_rot);
    set_end_vector(v, pt);
    print_vector(v);
    printf("Norm: %lf\n", get_norm_vector(v));

    free_vector(v);
    free_point(pt_rot);
    free_point(pt);
    return 0;
}