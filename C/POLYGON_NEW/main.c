#include <stdio.h>
#include <stdlib.h>
#include "point.h"

int main()
{
    point *pt = alloc_point();
    float x = 0.0;
    set_x_point(pt, x);
    free_point(pt);
    return 0;
}