#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: Pointer to head of list.
 * @number: Number to insert into.
 *
 * Return: The address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *i = *head;
	listint_t *new = malloc(sizeof(*head));

	if (new == NULL)
		return (NULL);

	new->n = number;
	if (*head == NULL)
	{
		new->next = NULL;
		*head = new;
		return (new);
	}
	if (i->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	for (; i->next != NULL; i = i->next)
	{
		if (i->next->n > number)
		{
			new->next = i->next;
			i->next = new;
			return (new);
		}
	}

	new->next = NULL;
	i->next = new;

	return (new);
}
