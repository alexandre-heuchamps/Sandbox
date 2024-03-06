#ifndef POINT_H
#define POINT_H

typedef struct Point point;

point *point_alloc(void);
void *point_free(point *);
void *point_init(point *, float, float);
void *point_print(const point *);
float point_get_x(const point *);
float point_get_y(const point *);
void *point_set_x(point *, float);
void *point_set_y(point *, float);

#endif