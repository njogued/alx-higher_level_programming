#include "lists.h"
/**
 * insert_node - Insert node function
 * @head: head of ll
 * @number: number to insert
 * Return: address of new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr;
	listint_t *newnode;

	if (head == NULL || !number)
		return (NULL);

	curr = *head;
	newnode = malloc(sizeof(listint_t));
	newnode->n = number;
	newnode->next = NULL;

	if (curr->next == NULL)
	{

	}

	while (curr != NULL)
	{
		if (curr->next->n >= number)
		{
			newnode->next = curr->next;
			curr->next = newnode;
			break;
		}
		curr = curr->next;
	}
	return (newnode);
}
