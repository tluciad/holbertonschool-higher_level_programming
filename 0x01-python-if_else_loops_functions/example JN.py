#!/usr/bin/python3


def new_node(num, head=None):

    if type(num) is not int:
        return None

    new_node = dict(next=None, number=num)

    if head is not None:
        node = head
        while node['next'] is not None:
            node = node['next']
        node['next'] = new_node
        node['next'] = dict(next=None, number=num)

    if head is None:
        head = new_node

    return head


""" Juan """


def print_list(head=None):
    if head is None:
        print("None")
        return
    print(head.get('number', None), "» ", end="")
    print_list(head['next'])


""" Verde """


def delete(index, head=None):
    if head is None:
        return None

    if type(index) is not int:
        return None

    if head is not None:
        if index == 0:
            return head['next']

        node = head
        while node['next'] is not None:
            if index == 1:
                node['next'] = node['next']['next']
                break
            index -= 1
            node = node['next']

    return head


""" Amarillo """


def have_on_head(head, number):
    return head is not None and number == head['number']


def delete_number(number, head=None):
    change = have_on_head(head, number)

    node = head
    while node is not None:
        if number == node['next']['number']:
            node['next'] = node['next']['next']
        node = node['next']

    if change:
        head = head['next']

    return head


""" Rojo """


def _swap(current=None, prev=None, new_node=True, index=0, direction=1):
    for i in range(index - direction):
        current = current['next']
        prev = prev['next']
        next_node = next_node['next']
    return (current, prev, new_node)


def swap(index, head=None, up=True):
    next_node = head['next']['next']
    current = head['next']
    prev = head
    if index == 0 and up is True:
        prev['next'] = current['next']
        current['next'] = prev
        head = current
        return head
    if up is True:
        current, prev, new_node = _swap(current, prev, new_node, index)
    else:
        current, prev, new_node = _swap(current, prev, new_node, index, 2)
    prev['next'] = current['next']
    current['next'] = next_node['next']
    next_node['next'] = current
    return head


""" Azul """


def get_index(index, head):
    if head is None:
        return None

    if index == 0:
        return head

    return get_index(index - 1, head['next'])


def change_between_numbers(index_1, index_2, head=None):

    node_1 = get_index(index_1, head)
    node_2 = get_index(index_2, head)
    if node_1 is not None and node_2 is not None:
        node_1['number'], node_2['number'] = (
            node_2['number'], node_1['number'])


""" Purpura """


def delete_all(head=None):
    # check if head is None
    if head is None:
        return None
    # delete all the keys and next nodes
    return head.clear()


head = new_node(9)
new_node(10, head)
new_node(12, head)
new_node(13, head)
new_node(14, head)
new_node(20, head)
new_node(30, head)
print_list(head)
head = delete_all(head)
print_list(head)
