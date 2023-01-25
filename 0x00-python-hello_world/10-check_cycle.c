#include "lists.h"

/**
 * check_cycle - Checks for cycles
 * @list: The list to check
 * Return: 0 if no list, 1 if it exists
 */
int check_cycle(listint_t *list)
{
	listint_t *curr;

	if (list == NULL)
		return (0);

	curr = list;

	while (curr != NULL)
	{
		if (curr->next == list)
		{
			return (1);
		}
		curr = curr->next;
	}
	return (0);
}
