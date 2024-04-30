#ifndef POINT_H
#define POINT_H

typedef struct Point point;

point *alloc_point(void);
void *free_point(point *);
void *set_x_point(point *, float);
void *set_y_point(point *, float);
float get_x_point(const point *);
float get_y_point(const point *);
void *init_point(point *, float, float);
void *print_point(const point *);

#endif