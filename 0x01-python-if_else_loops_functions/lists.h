#ifndef LISTS_H
#define LISTS_H

#include <stddef.h>  /* For size_t and NULL */
#include <stdlib.h>  /* For malloc and free */

/**
 * struct listint_s - singly linked list node structure
 * @n: integer data
 * @next: pointer to the next node in the list
 *
 * Description: This structure represents a node in a singly linked list.
 */
typedef struct listint_s
{
    int n;                  /* Integer data */
    struct listint_s *next; /* Pointer to the next node */
} listint_t;

/**
 * print_listint - Prints all the elements of a linked list.
 * @h: A pointer to the head of the linked list.
 *
 * Return: The number of nodes in the list.
 */
size_t print_listint(const listint_t *h);

/**
 * add_nodeint_end - Adds a new node at the end of a linked list.
 * @head: A pointer to a pointer to the head of the linked list.
 * @n: The integer data for the new node.
 *
 * Return: A pointer to the new node, or NULL if it fails.
 */
listint_t *add_nodeint_end(listint_t **head, const int n);

/**
 * free_listint - Frees a linked list.
 * @head: A pointer to the head of the linked list.
 */
void free_listint(listint_t *head);

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer to a pointer to the head of the linked list.
 * @number: The number to insert into the list.
 *
 * Return: A pointer to the new node, or NULL if it fails.
 */
listint_t *insert_node(listint_t **head, int number);

#endif /* LISTS_H */
