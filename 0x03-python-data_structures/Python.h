#include <Python.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for project
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

/**
 * print_listint - Prints all the elements of a listint_t linked list.
 * @h: Pointer to the head of the listint_t list.
 * 
 * Return: The number of nodes in the list.
 */
size_t print_listint(const listint_t *h);

/**
 * add_nodeint_end - Adds a new node at the end of a listint_t list.
 * @head: Pointer to the pointer to the head of the listint_t list.
 * @n: Integer to add to the listint_t list.
 * 
 * Return: Pointer to the newly added node, or NULL if it failed.
 */
listint_t *add_nodeint_end(listint_t **head, const int n);

/**
 * free_listint - Frees a listint_t linked list.
 * @head: Pointer to the head of the listint_t list.
 */
void free_listint(listint_t *head);

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to the pointer to the head of the listint_t list.
 * 
 * Return: 1 if the list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head);
