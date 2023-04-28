#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    unique_sides = {a, b, c}
    if not all_sides_real(unique_sides) or invalid_triangle(a, b, c):
        raise TriangleError()
    elif len(unique_sides) == 1:
        return 'equilateral'
    elif len(unique_sides) == 2:
        return 'isosceles'
    return 'scalene'

def all_sides_real(unique_sides):
    return all(v > 0 for v in unique_sides)

def invalid_triangle(a,b,c):
    return (a + b <= c or a + c <= b or b + c <= a)

# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
