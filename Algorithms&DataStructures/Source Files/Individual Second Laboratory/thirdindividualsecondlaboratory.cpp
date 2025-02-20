//
//  thirdindividualsecondlaboratory.cpp
//  Algorithms&DataStructures
//
//  Created by Максим Гоглов on 20.02.2025.
//

#include "Header.h"

class CList3 {
public:
    NodeWithMark* head;

    CList3() : head(nullptr) {}

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

    void each_n(CList3& list2, int n) {
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

class CList4 {
public:
    Node2* head;

    CList4() : head(nullptr) {}

    void append(const string& first, const string& second) {
        Node2* new_node = new Node2(first, second);
        if (!head) {
            new_node->next = new_node;
            head = new_node;
        }
        else {
            Node2* current = head;
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
        Node2* current = head;
        do {
            cout << current->data["first"] << " : " << current->data["second"] << " -> ";
            current = current->next;
        } while (current != head);
        cout << "\n";
    }

    int count_nodes() const {
        if (!head) return 0;
        int cnt = 1;
        Node2* current = head;
        while (current->next != head) {
            cnt++;
            current = current->next;
        }
        return cnt;
    }

    void each_n(CList4& list2, int n) {
        int cnt = count_nodes();
        int cnt_appends = 0;
        Node2* current = head;
        int i = 0;
        while (cnt_appends < cnt) {
            if (!current->mark) {
                i++;
                if (i % n == 0) {
                    list2.append(current->data["first"], current->data["second"]);
                    cnt_appends++;
                    current->mark = true;
                }
            }
            current = current->next;
        }
    }

};

void winners(CList3& list1, CList3& list2, int k, int n) {
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

void prizes(CList4& prizes, CList3& people) {
    int cnt = prizes.count_nodes();

    Node2* current = prizes.head;
    NodeWithMark* current2 = people.head;
    for (int i = 0; i < cnt; i++) {
        current->data["second"] = current2->data;
        current = current->next;
        current2 = current2->next;
    }
}

void sort_by_brand(CList4& listfrom, CList4& listto, string brand) {
    Node2* current = listfrom.head;
    while (current->next != listfrom.head) {
        if (current->data["first"] == brand) {
            listto.append(current->data["first"], current->data["second"]);
        }
        current = current->next;
    }
}

void ThirdIndividualSecondLab()
{
    CList4 products;
    CList4 products_sorted;
    for (int i = 1; i <= 20; i++) {
        if (i % 2 == 0) {
            products.append("Sony", "товар" + to_string(i));
        }
        else {
            products.append("Honor", "товар" + to_string(i));
        }
    }

    sort_by_brand(products, products_sorted, "Sony");

    products.print_list();
    cout << endl;
    products_sorted.print_list();
    return;
}
