#include <Python.h> 
#include <listobject.h> 
#include <object.h>

/** 
 * print_python_list_info - Print some basic info about Python lists 
 *
 * @p: Python object. 
 * 
 * Return: Nothing.
 */ 
void print_python_list_info(PyObject *p) 
{ 
	int i;
	long int size = PyList_Size(p);
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (i = 0; i < size; i++)
		printf("Element %i: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
}
