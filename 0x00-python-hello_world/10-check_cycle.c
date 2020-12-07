#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

int check_cycle(listint_t *list)
{
    listint_t *tmp;

    if (list == NULL)
    {
        return (0);
    }
    while(list)
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
