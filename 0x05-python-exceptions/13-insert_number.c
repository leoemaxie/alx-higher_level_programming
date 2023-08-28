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
	if ((*head)->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	for (; (*head)->next != NULL; *head = (*head)->next)
	{
		if ((*head)->next->n > number)
		{
			new->next = (*head)->next;
			(*head)->next = new;
			return (new);
		}
	}

	new->next = NULL;
	(*head)->next = new;

	return (new);
}
