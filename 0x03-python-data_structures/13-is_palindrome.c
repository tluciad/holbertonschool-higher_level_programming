#include "lists.h"
#include <stdlib.h>
/**
 *is_palindrome - function that checks if palindrome
 *@head: head of the node
 *Return: 0 false, 1 true
 */
int is_palindrome(listint_t **head)
{
    unsigned int len = 1;
    listint_t *temp;

    if (head == NULL || *head == NULL)
        return (1);
    temp = *head;
    while (temp)
    {
        temp = temp->next;
        len++;
    }
    return (0);
}
