#include "lists.h"

/**
 * check_cycle - This function checks if singly linked list has cycle
 * @list: Is the linked list to check
 * Return: 1 if it has a cycle and 0 if none found
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next; /* Move slow ptr 1 step */
		fast = fast->next->next; /* Move fast ptr 2 steps*/
		/* If slow and fast pointers meet, cycle detected */
		if (slow == fast)
			return (1);
	}
	/* No cycle found */
	return (0);
}
