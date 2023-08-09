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
    listint_t *i;
    listint_t *new = malloc(sizeof(*head));

    if (new == NULL)
        return (NULL);

    new->n = number;

    for (i = *head; i != NULL; i = i->next)
    {
        listint_t *tmp = i->next;

        if (tmp->n > number)
        {
            i->next = new;
            new->next = tmp;
            return (new);
        }
    }

    new->next = NULL;
    *head = new;

    return (new);
}
