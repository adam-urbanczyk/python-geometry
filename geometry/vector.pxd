
from .point cimport Point
from .quat cimport Quat
from libc.math cimport sqrt, acos


cdef class Vector(object):
    
    cdef public double x
    cdef public double y
    cdef public double z
    
    cpdef double min(Vector)
    cpdef double max(Vector)
    
    cpdef int argmin(Vector)
    cpdef int argmax(Vector)
    
    cpdef bint unit(Vector)
    cpdef double norm(Vector)
    cpdef Vector normalize(Vector)
    cpdef Vector normalized(Vector)
    
    cpdef double angle(Vector, Vector)
    
    cpdef double dot(Vector, Vector)
    cpdef Vector cross(Vector, Vector)
    
    cpdef double cosines_with(Vector, Vector)
    
    cpdef Vector rotate(Vector, Quat)
    cpdef Vector rotate_inplace(Vector, Quat)
    
    
cpdef double dot(Vector a, Vector b)
cpdef Vector cross(Vector a, Vector b)
cpdef double cosine_between_vectors(Vector a, Vector b)
