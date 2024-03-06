#include <stdio.h>
#include <stdlib.h>
#include "point.h"
#include "polygon.h"



int main() {
    unsigned nside = 7;
    float radius = 1.0;

    point* centre = point_alloc();
    point_init(centre, 7.0, 0.0);

    polygon* poly = polygon_alloc(nside);
    polygon_init(poly, nside, radius, centre); // this one is a problem
    polygon_print(poly);

    polygon_free(poly);
    point_free(centre);
    exit(EXIT_SUCCESS);
}