#include <lists.h>

/**
 * print_python_list_info - print info about a Python list object
 * @p: pointer to PyObject, which should be castable to a PyListObject
 */
void print_python_list_info(PyObject *p)
{
    Py_ssize_t i;
    const char *type;
    Py_ssize_t l_size;
    PyListObject *newp;
    PyObject *element;

    if (PyList_Check(p))
    {
        newp = (PyListObject *)p;
        l_size = PyList_Size(p);
        // No need to check if l_size < 0 as PyList_Size should always return a non-negative value
        printf("[*] Size of the Python List = %zd\n", l_size);
        
        // l_allocated is not a standard field of PyListObject, so removing this line
        // Instead, print the size of the list only

        for (i = 0; i < l_size; i++)
        {
            element = PyList_GetItem(p, i);  // Use PyList_GetItem to access list elements
            type = Py_TYPE(element)->tp_name;
            printf("Element %zd: %s\n", i, type);
        }
    }
}
