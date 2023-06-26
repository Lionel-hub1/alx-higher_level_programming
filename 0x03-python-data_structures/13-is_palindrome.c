#include "lists.h"

listint_t *reverse_list(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverses_list - Is a function that reverses our listint_t list
 * @head: Is the node that starts our list
 *
 * Return: A pointer of the reversed list
 */
listint_t *reverses_list(listint_t **head)
{
	listint_t *current = *head, *next_node, *previous = NULL;

	while (current)
	{
		next_node = current->next;
		current->next = previous;
		previous = current;
		current = next_node;
	}

	/* Update the head to point to the new head */
	*head = previous;
	return (*head);
}

/**
 * is_palindrome - Is a function that check the list which is palindrome
 * @head: Is a pointer of the starting point of the list
 *
 * Return: 1 if the linked list is a palindrome or 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp, *reversed, *mid;
	size_t size = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	temp = *head;
	while (temp)
	{
		size++;
		temp = temp->next;
	}

	temp = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		temp = temp->next;

	if ((size % 2) == 0 && temp->n != temp->next->n)
		return (0);

	temp = temp->next->next;

	/* Reverse the second half of the list */
	reversed = reverses_list(&temp);
	mid = reversed; /* Save the reversed list to restore it later */

	temp = *head;
	while (reversed)
	{
		if (temp->n != reversed->n)
			return (0);
		temp = temp->next;
		reversed = reversed->next;
	}
	/* Restore the reversed part to its original order */
	reverses_list(&mid);

	return (1);
}
