#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list contains a cycle
 * @list: Pointer to the head of the linked list to check
 *
 * Return: 1 if a cycle is found, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	/* Move slow pointer one step, fast pointer two steps */
	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		/* If slow and fast meet, there is a cycle */
		if (slow == fast)
			return (1);
	}

	/* No cycle found */
	return (0);
}
