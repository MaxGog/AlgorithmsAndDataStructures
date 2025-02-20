//
//  sixthindividualsecondlaboratory.cpp
//  Algorithms&DataStructures
//
//  Created by Максим Гоглов on 20.02.2025.
//

#include "Header.h"

class CList7 {
public:
    NodeWithMark* head;

    CList7() : head(nullptr) {}

    void append(const string& data) {
        NodeWithMark* new_node = new NodeWithMark(data);
        if (!head) {
            new_node->next = new_node;
            head = new_node;
        }
        else {
            NodeWithMark* current = head;
            while (current->next != head) {
                current = current->next;
            }
            current->next = new_node;
            new_node->next = head;
        }
    }

    void print_list() const {
        if (!head) {
            cout << "Circular Linked List is empty\n";
            return;
        }
        NodeWithMark* current = head;
        do {
            cout << current->data << " ";
            current = current->next;
        } while (current != head);
        cout << "\n";
    }

    int count_nodes() const {
        if (!head) return 0;
        int cnt = 1;
        NodeWithMark* current = head;
        while (current->next != head) {
            cnt++;
            current = current->next;
        }
        return cnt;
    }
};

class Node3 {
public:
    map<string, string> data;
    Node3* next;
    bool mark;

    Node3(const string& first, const string& second) : next(nullptr), mark(false) {
        data["first"] = first;
        data["second"] = second;
    }
};

class CList8 {
public:
    Node3* head;

    CList8() : head(nullptr) {}

    void append(const string& first, const string& second) {
        Node3* new_node = new Node3(first, second);
        if (!head) {
            new_node->next = new_node;
            head = new_node;
        }
        else {
            Node3* current = head;
            while (current->next != head) {
                current = current->next;
            }
            current->next = new_node;
            new_node->next = head;
        }
    }

    void print_list() const {
        if (!head) {
            cout << "Circular Linked List is empty\n";
            return;
        }
        Node3* current = head;
        do {
            cout << current->data["first"] << " : " << current->data["second"] << " -> ";
            current = current->next;
        } while (current != head);
        cout << "\n";
    }

    int count_nodes() const {
        if (!head) return 0;
        int cnt = 1;
        Node3* current = head;
        while (current->next != head) {
            cnt++;
            current = current->next;
        }
        return cnt;
    }
};

void winners(CList7& list1, CList7& list2, int k, int n) {
    int cnt = list1.count_nodes();
    if (k > cnt) {
        cout << "Количество победителей не может быть больше количества участников\n";
        return;
    }
    int cnt_winners = 0;
    NodeWithMark* current = list1.head;
    int i = 0;
    while (cnt_winners < k) {
        if (!current->mark) {
            i++;
            if (i % n == 0) {
                list2.append(current->data);
                cnt_winners++;
                current->mark = true;
            }
        }
        current = current->next;
    }
}

void prizes(CList8& prizes, CList7& people) {
    int cnt = prizes.count_nodes();

    Node3* current = prizes.head;
    NodeWithMark* current2 = people.head;
    for (int i = 0; i < cnt; i++) {
        current->data["second"] = current2->data;
        current = current->next;
        current2 = current2->next;
    }
}

void SixthIndividualSecondLab()
{
    CList7 list1;
    CList8 listprs;
    for (int i = 1; i <= 20; i++) {
        list1.append("фамилия" + to_string(i));
    }
    for (int i = 1; i <= 5; i++) {
        listprs.append("приз" + to_string(i), "0");
    }
    CList7 list2;
    winners(list1, list2, 5, 5);
    prizes(listprs, list2);
    listprs.print_list();
    return;
}
