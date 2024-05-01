#ifndef VECTOR_H
#define VECTOR_H

#include "point.h"

typedef struct Vector vector;

vector *alloc_vector(void);
void *free_vector(vector *vec);
void *set_origin_vector(vector *vec, const point *origin);
void *set_end_vector(vector *vec, const point *end);
void *set_xorigin_vector(vector *vec, float x);
void *set_yorigin_vector(vector *vec, float y);
void *set_xend_vector(vector *vec, float x);
// void *set_y_point(point *pt, float y);
// float get_x_point(const point *pt);
// float get_y_point(const point *pt);
// void *init_point(point *pt, float x, float y);
// void *print_point(const point *pt);
// void *rotate_point(point *pt, const point *origin, float ang);

#endif