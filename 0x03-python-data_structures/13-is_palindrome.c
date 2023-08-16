#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 *
 * @head: Pointer to head of list.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	int i = 0, j;
	int num_array[1024];

	if (*head == NULL)
		return (1);

	while (*head != NULL)
	{
		num_array[i++] = (*head)->n;
		*head = (*head)->next;
	}

	for (j = 0, i -= 1; j < i; j++, i--)
		if (num_array[i] != num_array[j])
			return (0);

	return (1);
}
