#include "lists.h"
int is_palindrome(listint_t **head)
{
    listint_t *temp = *head;
    listint_t *temp2 = *head;
    int len, i, j = 0;
    int *array;

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
    while (j <= len)
    {
        if (array[j] == array[len])
        {
            j++;
            len--;
        }
        else
        {
            free(temp);
            return (0);
        }
    }
    return (1);
}