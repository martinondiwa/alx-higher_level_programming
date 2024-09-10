#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer to the head of the linked list.
 * @number: The number to insert.
 *
 * Return: If the function fails - NULL.
 *         Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *node = *head, *new;

    /* Allocate memory for the new node */
    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    /* Assign the value to the new node */
    new->n = number;

    /* Insert the new node at the beginning if necessary */
    if (node == NULL || node->n >= number)
    {
        new->next = node;
        *head = new;
        return (new);
    }

    /* Traverse the list to find the correct insertion point */
    while (node && node->next && node->next->n < number)
        node = node->next;

    /* Insert the new node at the correct position */
    new->next = node->next;
    node->next = new;

    return (new);
}
