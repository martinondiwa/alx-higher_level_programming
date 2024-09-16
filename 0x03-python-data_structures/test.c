#include <stdint.h>

#define PY_SSIZE_T_CLEAN
#include <Python.h>

static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT, "test", NULL, -1
};

PyMODINIT_FUNC
PyInit_test(void)
{
    return PyModule_Create(&module);
}
