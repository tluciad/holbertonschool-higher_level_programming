#include "lists.h"
/**
*check_cycle - that checks if a singly linked list has a cycle in it
*@list: pointer to head
*
*/
int check_cycle(listint_t *list)
{
    listint_t *slow, *fast;
    slow = list;
    fast = list;
    while (slow && fast)
    {
        slow = slow->next;
        fast = fast->next;
        if (fast)
            fast = fast->next;
        if (slow && fast && slow == fast)
            return (1);
    }
    return (0);
}