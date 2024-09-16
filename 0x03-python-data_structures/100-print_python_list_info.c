#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - print info about a Python list object
 * @p: pointer to PyObject, which should be castable to a PyListObject
 */
void print_python_list_info(PyObject *p)
{
    if (!PyList_Check(p))
    {
        fprintf(stderr, "Provided PyObject is not a list\n");
        return;
    }

    PyListObject *list_obj = (PyListObject *)p;
    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t allocated = PyList_GET_SIZE(p);  // This gives us the allocated size, not always visible

    // Print the size of the list
    printf("[*] Size of the Python List = %zd\n", size);

    // Print allocated size
    printf("[*] Allocated = %zd\n", allocated);

    // Iterate through the list and print the type of each element
    for (Py_ssize_t i = 0; i < size; i++)
    {
        PyObject *item = PyList_GetItem(p, i);
        const char *type = Py_TYPE(item)->tp_name;
        printf("Element %zd: %s\n", i, type);
    }
}
