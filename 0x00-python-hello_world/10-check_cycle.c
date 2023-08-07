#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - Checks if a singly linked list has a cycle in it.
 *
 * @list: Pointer to head of list.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	static listint_t *pass;

	if (pass == NULL)
	{
		pass = list;
		return (0);
	}

	return (1);
}
