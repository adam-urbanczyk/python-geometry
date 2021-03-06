import pytest
import tempfile
import pickle
from geometry import Plane, Point, Polygon, Vector


def test_from_normal_and_point():

    corners1 = [ Point(0.0, 0.0, 0.0), Point(1.0, 0.0, 0.0), Point(1.0, 1.0, 0.0), Point(0.0, 1.0, 0.0) ]
    center1 = Point(0.5, 0.5, 0.0)
    polygon1 = Polygon(corners1, center1)
    plane1 = Plane.from_normal_and_point(polygon1.plane().normal(), center1)
    assert polygon1.plane() == plane1    # tests the reduced normal form coefficients.


    corners2 = [ Point(0.0, 0.0, 0.0), Point(0.0, 1.0, 0.0), Point(0.0, 1.0, 1.0), Point(0.0, 0.0, 1.0) ]
    center2 = Point(0.0, 0.5, 0.5)
    polygon2 = Polygon(corners2, center2)
    plane2 = Plane.from_normal_and_point(polygon2.plane().normal(), center2)
    assert polygon2.plane() == plane2


    corners4 = [ Point(1.0, 0.0, 0.0), Point(1.0, 1.0, 0.0), Point(1.0, 1.0, 1.0), Point(1.0, 0.0, 1.0) ]
    center4 = Point(1.0, 0.5, 0.5)
    polygon4 = Polygon(corners4, center4)
    plane4 = Plane.from_normal_and_point(polygon4.plane().normal(), center4)
    assert polygon4.plane() == plane4


def test_intersection():

    plane = Plane(0.0, 0.0, 1.0, -0.9)
    a = Point(0.5, 0.5, -0.9)
    b = Point(0.0, 0.0, 0.0)
    assert plane.intersection(a, b) == Point(-0.5, -0.5, 0.9)

    points = [Point(0.5, 0.0, 0.0), Point(0.5, 1.0, 0.0), Point(0.5, 1.0, 1.0), Point(0.5, 0.1, 1.0)]
    polygon = Polygon(points, Point(0.5, 0.5, 0.5))

    source = Point(0.5, 0.5, 0.5)
    mirror = source.mirror_with(Plane.from_normal_and_point(Vector(1.0, 0.0, 0.0), Point(1.0, 0.5, 0.5)))
    intersection = polygon.plane().intersection(mirror, Point(1.0, 0.0, 0.0))

    assert intersection == Point(0.5, -0.5, -0.5)

def test_pickle():
    a = Plane(0.0, 0.0, 1.0, -0.9)

    with tempfile.TemporaryDirectory() as tmpdirname:
        with open('obj.pickle', mode='w+b') as f:
            pickle.dump(a, f)

        with open('obj.pickle', mode='r+b') as f:
            a2 = pickle.load(f)

        assert a2 == a
