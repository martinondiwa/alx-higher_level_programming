#include <stddef.h>
#ifndef LISTS_H
#define LISTS_H

/**
 * struct listint_s - singly linked list
 * @n: integer value of the node
 * @next: pointer to the next node in the list
 *
 * Description: Defines a node in a singly linked list for the project.
 */
typedef struct listint_s
{
    int n;                    /**< Integer value of the node */
    struct listint_s *next;   /**< Pointer to the next node in the list */
} listint_t;

/**
 * print_listint - Prints all the elements of a listint_t list.
 * @h: Pointer to the head of the list.
 *
 * Return: The number of nodes in the list.
 */
size_t print_listint(const listint_t *h);

/**
 * add_nodeint_end - Adds a new node at the end of a listint_t list.
 * @head: Double pointer to the head of the list.
 * @n: Integer value for the new node.
 *
 * Return: Pointer to the newly added node, or NULL if it failed.
 */
listint_t *add_nodeint_end(listint_t **head, const int n);

/**
 * free_listint - Frees a listint_t list.
 * @head: Pointer to the head of the list to be freed.
 */
void free_listint(listint_t *head);

/**
 * is_palindrome - Checks if a linked list is a palindrome.
 * @head: Double pointer to the head of the list.
 *
 * Return: 1 if the list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head);

#endif /* LISTS_H */
