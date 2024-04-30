#ifndef POINT_H
#define POINT_H

typedef struct Point point;

point *alloc_point(void);
void *free_point(point *pt);
void *set_x_point(point *pt, float x);
void *set_y_point(point *pt, float y);
float get_x_point(const point *pt);
float get_y_point(const point *pt);
void *init_point(point *pt, float x, float y);
void *print_point(const point *pt);
void *rotate_point(point *pt, const point *origin, float ang);

#endif