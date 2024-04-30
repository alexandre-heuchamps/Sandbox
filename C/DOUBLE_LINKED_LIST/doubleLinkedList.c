#include <stdio.h>
#include <stdlib.h>










// Define the Node data structure
typedef struct Node
{
    int data;
    struct Node* next;
    struct Node* prev;
} Node;










// Function to insert a node at the start of the linked list
void
insert_start(Node** headRef, int data)
{
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->data = data;
    newNode->next = *headRef;
    newNode->prev = NULL;

    if (*headRef != NULL)
    {
        (*headRef)->prev = newNode;
    }

    *headRef = newNode;
}










// Function to insert a node at the end of the linked list
void
insert_end(Node** headRef, int data)
{
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->data = data;
    newNode->next = NULL;

    if (*headRef == NULL)
    {
        newNode->prev = NULL;
        *headRef = newNode;
    }
    else
    {
        Node* last = *headRef;
        while (last->next != NULL) {
            last = last->next;
        }
        last->next = newNode;
        newNode->prev = last;
    }
}










// Function to delete the first node of the linked list
void
delete_start(Node** headRef)
{
    if (*headRef == NULL)
    {
        return;
    }

    Node* nextNode = (*headRef)->next;
    free(*headRef);

    if (nextNode != NULL)
    {
        nextNode->prev = NULL;
    }

    *headRef = nextNode;
}










// Function to delete the last node of the linked list
void
delete_end(Node** headRef)
{
    if (*headRef == NULL)
    {
        return;
    }

    Node* last = *headRef;
    while (last->next != NULL)
    {
        last = last->next;
    }

    if (last->prev != NULL)
    {
        last->prev->next = NULL;
    }
    else
    {
        *headRef = NULL;
    }

    free(last);
}










// Function to delete a node at a specific position in the linked list
void
delete_position(Node** headRef, unsigned int position)
{
    if (*headRef == NULL)
    {
        return;
    }

    Node* temp = *headRef;
    unsigned int count = 0;

    while (temp != NULL && count < position)
    {
        temp = temp->next;
        count++;
    }

    if (temp != NULL)
    {
        if (temp->prev != NULL)
        {
            temp->prev->next = temp->next;
        }
        else
        {
            *headRef = temp->next;
        }

        if (temp->next != NULL)
        {
            temp->next->prev = temp->prev;
        }

        free(temp);
    }
}










// Function to print the linked list
void
printList(Node* node)
{
    while (node != NULL)
    {
        printf("%d ", node->data);
        node = node->next;
    }
}










// Function to free the linked list
void
freeLinkedList(Node** headRef)
{
    Node* current = *headRef;
    Node* next;

    while (current != NULL)
    {
        next = current->next;
        free(current);
        current = next;
    }

    *headRef = NULL;
}










int
main()
{
    Node* head = NULL;

    insert_start(&head, 1);  // Insert 1 at the start
    insert_end(&head, 2);    // Insert 2 at the end
    insert_end(&head, 3);    // Insert 3 at the end
    insert_end(&head, 4);    // Insert 4 at the end
    insert_end(&head, 5);    // Insert 5 at the end

    printList(head);
    printf("\n");

    delete_position(&head, 2);  // Delete node at position 2

    printList(head);
    printf("\n");

    freeLinkedList(&head);

    return 0;
}