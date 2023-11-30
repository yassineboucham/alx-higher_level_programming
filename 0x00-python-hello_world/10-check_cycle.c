#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: listint_t
 * Return: 0 if there is no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *faster = list->next;
	listint_t *slow = list;

	if (list == NULL || list->next == NULL)
		return (0);
	while (faster != NULL && faster->next != NULL)
	{
		if (faster == slow || faster->next == slow)
			return (1);
		faster = faster->next->next;
		slow = slow->next;
	}
return (0);
}
