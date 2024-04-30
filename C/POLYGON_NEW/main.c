#include <stdio.h>
#include <stdlib.h>
#include "point.h"

int main()
{
    point *pt = alloc_point();
    free_point(pt);
    return 0;
}