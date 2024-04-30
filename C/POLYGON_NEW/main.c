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
    printf("'y' point: %lf\n", get_y_point(pt));
    free_point(pt);

    point *pt2 = alloc_point();
    x = 3.6;
    y = 5.48;
    init_point(pt2, x, y);
    printf("'x' point: %lf\n", get_x_point(pt2));
    printf("'y' point: %lf\n", get_y_point(pt2));
    return 0;
}