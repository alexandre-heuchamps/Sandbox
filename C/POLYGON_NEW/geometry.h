#ifndef GEOMETRY_H
#define GEOMETRY_H

#include "point.h"
#include "vector.h"

void *translate_point(point *pt, const vector *vec);
void *rotate_point(point *pt, const point *origin_rot, float ang);

#endif