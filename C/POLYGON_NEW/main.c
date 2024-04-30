#include <stdio.h>
#include <stdlib.h>
#include "point.h"

int main()
{
    point *pt = alloc_point();
    float x = 0.0;
    float y = 2.3;
    set_x_point(pt, x);
    printf("'x' point: %lf\n", get_x_point(pt));
    set_y_point(pt, y);
    free_point(pt);
    return 0;
}