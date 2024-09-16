#include <stdlib.h>
#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - Prints basic information about Python lists.
 * @p: A Python list object.
 */
void print_python_list_info(PyObject *p)
{
    int elem;

    printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
    printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

    for (elem = 0; elem < Py_SIZE(p); elem++) {
        PyObject *item = PyList_GetItem(p, elem);
        printf("Element %d: %s\n", elem, Py_TYPE(item)->tp_name);
    }
}
