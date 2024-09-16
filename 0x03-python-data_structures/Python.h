#ifndef PYTHON_H
#define PYTHON_H

#include <stdio.h>
#include <stddef.h>

#define Py_ssize_t size_t
#define PyListObject listobject
#define PyObject void*

typedef struct {
    PyObject **ob_item;
    Py_ssize_t allocated;
} PyListObject;

#define PyList_Check(op) 1
#define PyList_Size(op) 5

static inline PyObject* PyList_GetItem(PyObject* p, Py_ssize_t i) {
    return ((PyListObject*)p)->ob_item[i];
}

#endif /* PYTHON_H */
