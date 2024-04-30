#include <stdio.h>
#include <stdlib.h>










// Define the Node data structure
typedef struct Node {
    int data;
    struct Node* next;
} Node;










// Function to insert a node at the start of the linked list
void insert_start(Node** headRef, int data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->data = data;
    newNode->next = *headRef;
    *headRef = newNode;
}










// Function to insert a node at the end of the linked list
void insert_end(Node** headRef, int data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->data = data;
    newNode->next = NULL;

    if (*headRef == NULL) {
        *headRef = newNode;
    } else {
        Node* last = *headRef;
        while (last->next != NULL) {
            last = last->next;
        }
        last->next = newNode;
    }
}










// Function to delete the first node of the linked list
void delete_start(Node** headRef) {
    if (*headRef == NULL) {
        return;
    }

    Node* nextNode = (*headRef)->next;
    free(*headRef);
    *headRef = nextNode;
}










// Function to delete the last node of the linked list
void delete_end(Node** headRef) {
    if (*headRef == NULL) {
        return;
    }

    if ((*headRef)->next == NULL) {
        free(*headRef);
        *headRef = NULL;
    } else {
        Node* secondLast = *headRef;
        while (secondLast->next->next != NULL) {
            secondLast = secondLast->next;
        }

        free(secondLast->next);
        secondLast->next = NULL;
    }
}










// Function to delete a node at a specific position in the linked list
void delete_position(Node** headRef, unsigned int position) {
    if (*headRef == NULL) {
        return;
    }

    if (position == 0) {
        delete_start(headRef);
    } else {
        Node* temp = *headRef;
        unsigned int count = 0;

        while (temp != NULL && count < position - 1) {
            temp = temp->next;
            count++;
        }

        if (temp == NULL || temp->next == NULL) {
            delete_end(headRef);
        } else {
            Node* nextNode = temp->next->next;
            free(temp->next);
            temp->next = nextNode;
        }
    }
}










// Function to print the linked list
void printList(Node* node) {
    while (node != NULL) {
        printf("%d ", node->data);
        node = node->next;
    }
}










// Function to free the linked list
void freeLinkedList(Node** headRef) {
    Node* current = *headRef;
    Node* next;

    while (current != NULL) {
        next = current->next;
        free(current);
        current = next;
    }

    *headRef = NULL;
}










int main() {
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