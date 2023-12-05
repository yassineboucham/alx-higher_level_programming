#include "lists.h"
#include <stdio.h>
#define SIZE 100
int is_palindrome(listint_t **head)
{
	int size = 0, *arr, i = 0, j;

	listint_t *walk = *head;

	while (walk->next != NULL)
	{
		walk = walk->next;
		size++;
	}
	walk = *head;
	arr = malloc(size * sizeof(int));
	while (walk != NULL)
	{
		arr[i++] = walk->n;
		walk = walk->next;
	}
	for (i = 0, j = size; i < j; i++, j--)
	{
		if (arr[i] != arr[j])
			return (0);
	}
	return (1);
}
