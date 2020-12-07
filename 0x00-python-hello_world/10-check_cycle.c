#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checks if there are cycles
 * @list: linked list
 * Return: 1 if cycle else 0.
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp;

	if (list == NULL)
	{
		return (0);
	}
	while (list)
	{
		tmp = list;
		list = list->next;
		if (tmp <= list)
		{
			return (1);
		}
	}
	return (0);
}
