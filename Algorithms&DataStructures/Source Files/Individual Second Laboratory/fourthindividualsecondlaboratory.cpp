//
//  fourthindividualsecondlaboratory.cpp
//  Algorithms&DataStructures
//
//  Created by Максим Гоглов on 20.02.2025.
//

#include "Header.h"

class CList5 {
private:
    NodeWithMark* head;
public:
    CList5() {
        head = nullptr;
    }

    void append(string data) {
        NodeWithMark* newNode = new NodeWithMark(data);
        if (!head) {
            newNode->next = newNode;
            head = newNode;
        }
        else {
            NodeWithMark* current = head;
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
        NodeWithMark* current = head;
        do {
            cout << current->data << " ";
            current = current->next;
        } while (current != head);
        cout << endl;
    }

    int count_nodes() {
        if (!head) return 0;
        int count = 1;
        NodeWithMark* current = head;
        while (current->next != head) {
            count++;
            current = current->next;
        }
        return count;
    }

    void each_n(CList5& list2, int n) {
        int cnt = count_nodes();
        int cnt_appends = 0;
        NodeWithMark* current = head;
        int i = 0;
        while (cnt_appends < cnt) {
            if (!current->mark) {
                i++;
                if (i % n == 0) {
                    list2.append(current->data);
                    cnt_appends++;
                    current->mark = true;
                }
            }
            current = current->next;
        }
    }
};

void FourthIndividualSecondLab()
{
    CList5 list1;
    CList5 list2;
    for (int i = 1; i <= 7; i++) {
        list1.append("фамилия" + to_string(i));
    }
    for (int i = 8; i <= 14; i++) {
        list2.append("фамилия" + to_string(i));
    }
    cout << "Вывод изначальных списков:" << endl;
    list1.print_list();
    list2.print_list();

    CList5 list1_sorted;
    CList5 list2_sorted;
    list1.each_n(list1_sorted, 2);
    list2.each_n(list2_sorted, 13);

    cout << "Перемешанные списки:" << endl;
    list1_sorted.print_list();
    list2_sorted.print_list();

    return;
}
