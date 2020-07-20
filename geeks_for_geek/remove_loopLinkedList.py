def remove_node(head):
    if head is None or head.next is None:
        return head

    first = head.next
    second = head.next.next
    while first is not None and second is not None:
        if first == second:
            break

        if first.next and second.next and second.next.next:
            first = first.next
            second = second.next.next
        else:
            return False

    if first == second:
        first = head
        while first is not None and second is not None and first != second:

            if first.next and second.next:
                first = first.next
                second = second.next
        first.next = None
        return head
    else:
        return False
