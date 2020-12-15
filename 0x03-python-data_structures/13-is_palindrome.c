#include "lists.h"
/**
 * is_palindrome - checks if a list is palindrome.
 * @head: singly linked list.
 * Return: 1 if palindrome or 0 if not.
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	listint_t *temp2 = *head;
	int len, i, j;
	int *array;

	if (*head == NULL || head == NULL)
		return (0);
	if ((*head)->next == NULL)
		return (1);
	for (len = 0; temp->next != NULL; len++)
	{
		temp = temp->next;
	}
	array =  malloc(len * sizeof(int));
	for (i = 0; i <= len; i++)
	{
		array[i] = temp2->n;
		temp2 = temp2->next;
	}
	for (j = 0, len; j < len; j++, len--)
	{
		if (array[len] != array[j])
		{
			return (0);
		}
	}
	return (1);
}
