#include "lists.h"

/**
 * check_cycle - Checks for cycles
 * @list: The list to check
 * Return: 0 if no list, 1 if it exists
 */
int check_cycle(listint_t *list)
{
	listint_t *curr;
	listint_t *nxt;

	if (list == NULL)
		return (0);

	curr = list;
	nxt = curr->next;

	while (curr != NULL)
	{
		while (nxt != NULL)
		{
			if (nxt->next == curr)
			{
				return (1);
			}
			nxt = nxt->next;
		}
		curr = curr->next;
	}
	return (0);
}
