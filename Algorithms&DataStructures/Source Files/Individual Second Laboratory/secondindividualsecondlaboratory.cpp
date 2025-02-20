//
//  secondindividualsecondlaboratory.cpp
//  Algorithms&DataStructures
//
//  Created by Максим Гоглов on 20.02.2025.
//

#include "Header.h"

class NodeNonMark {
public:
    string data;
    NodeNonMark* next;

    NodeNonMark(string val) {
        data = val;
        next = nullptr;
    }
};

class CList {
private:
    NodeNonMark* head;
public:
    CList() {
        head = nullptr;
    }

    void append(string data) {
        NodeNonMark* newNode = new NodeNonMark(data);
        if (!head) {
            newNode->next = newNode;
            head = newNode;
        }
        else {
            NodeNonMark* current = head;
            while (current->next != head) {
                current = current->next;
            }
            current->next = newNode;
            newNode->next = head;
        }
    }

    void print_list() {
        if (!head) {
            cout << "Circular Linked List is empty" << endl;
            return;
        }
        NodeNonMark* current = head;
        do {
            cout << current->data << " ";
            current = current->next;
        } while (current != head);
        cout << endl;
    }

    int count_nodes() {
        if (!head) return 0;
        int count = 1;
        NodeNonMark* current = head;
        while (current->next != head) {
            count++;
            current = current->next;
        }
        return count;
    }

    void delete_n(int pos) {
        if (!head || pos < 1) return;
        NodeNonMark* current = head;
        NodeNonMark* prev = nullptr;
        if (pos == 1) {
            NodeNonMark* temp = head;
            while (temp->next != head) {
                temp = temp->next;
            }
            if (head->next == head) {
                delete head;
                head = nullptr;
                return;
            }
            head = head->next;
            temp->next = head;
            delete current;
            return;
        }
        for (int i = 1; i < pos; i++) {
            prev = current;
            current = current->next;
            if (current == head) return;
        }
        prev->next = current->next;
        delete current;
    }

    void devide_in_two(CList& list2)
    {
        if (count_nodes() <= 1) {
            cout << "Первый список должен содержать более одного узла\n" << endl;
            return;
        }
        if (list2.count_nodes() > 0) {
            cout << "Второй список должен быть пустым" << endl;
            return;
        }
        NodeNonMark* current = head;
        int i = 1;
        do {
            NodeNonMark* nextNode = current->next;
            if (i % 2 == 0) {
                list2.append(current->data);
            }
            current = nextNode;
            i++;
        } while (current != head);

        int halfSize = count_nodes() / 2;
        for (int i = halfSize; i > 0; i--) {
            delete_n(i * 2);
        }
    }
};

void SecondIndividualSecondLab()
{
    CList list1;
    for (int i = 1; i <= 20; i++) {
        list1.append("фамилия" + to_string(i));
    }
    cout << "Вывод изначального списка:" << endl;
    list1.print_list();

    CList list2;
    list1.devide_in_two(list2);

    cout << "\n\nРазделенные списки:" << endl;
    list1.print_list();
    list2.print_list();

    return;
}
