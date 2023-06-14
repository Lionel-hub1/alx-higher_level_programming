#include <Python.h>

/**
 * print_python_list_info - Prints information about a Python list object
 * @p: Pointer to the Python list object
 */
void print_python_list_info(PyObject *p)
{
	int list_size, list_allocated, i;
	PyObject *item;

	/* Get the size and allocated memory of the list */
	list_size = Py_SIZE(p);
	list_allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", list_size);
	printf("[*] Allocated = %d\n", list_allocated);

	/* Iterate over the list elements */
	for (i = 0; i < list_size; i++)
	{
		printf("Element %d: ", i);

		/* Get the i-th item from the list */
		item = PyList_GetItem(p, i);

		/* Print the type name of the item */
		printf("%s\n", Py_TYPE(item)->tp_name);
	}
}
