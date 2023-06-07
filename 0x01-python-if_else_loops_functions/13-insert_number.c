#include "lists.h"
/**
 * insert_node - This function inserts a node in a sorted singly-linked list
 * @head: Is a pointer to the head of the linked list
 * @number: Is the number to be inserted
 *
 * Return: Address of the newly inserted node, or NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number; /* Set the value of the new node */

	/* If list is empty, new node is inserted at the beginning */
	if (node == NULL || node->n >= number)
	{
		/* Make new node point to the current head */
		new->next = node;
		*head = new; /* Make head point to the new node */
		return (new);
	}
	/* Find the correct position for insertion*/
	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
