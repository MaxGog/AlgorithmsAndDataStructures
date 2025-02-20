//
//  individualsecondlaboratory.cpp
//  Algorithms&DataStructures
//
//  Created by Максим Гоглов on 20.02.2025.
//

#include "Header.h"

class CList {
public:
    NodeWithMark* head;

    CList() : head(nullptr) {}

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

    void each_n(CList& list2, int n) {
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

class CList2 {
public:
    Node2* head;

    CList2() : head(nullptr) {}

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
            cout << current->data["first"] << " : " << current->data["second"] << "      ";
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

    void each_n(CList2& list2, int n) {
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

void prizes(CList2& prizes, CList& people) {
    int cnt = prizes.count_nodes();

    Node2* current = prizes.head;
    NodeWithMark* current2 = people.head;

    for (int i = 0; i < cnt; i++) {
        current->data["second"] = current2->data;
        current = current->next;
        current2 = current2->next;
    }
}

void FirstIndividualSecondLab() {

    int students_count, tickets_count;

    cout << "Введите количество студентов: ";
    cin >> students_count;

    cout << "Введите количество билетов (больше количества студентов): ";
    cin >> tickets_count;

    if (tickets_count <= students_count) {
        cout << "Ошибка: Количество билетов должно быть больше количества студентов\n";
        return;
    }

    CList2 students;
    CList2 students_sorted;
    CList bilets;
    CList bilets_sorted;

    // Добавляем студентов
    for (int i = 1; i <= students_count; i++) {
        students.append("студент_" + to_string(i), "0");
    }

    // Добавляем билеты
    for (int i = 1; i <= tickets_count; i++) {
        bilets.append("билет_" + to_string(i));
    }

    CList list2;
    students.each_n(students_sorted, 3);
    bilets.each_n(bilets_sorted, 2);
    prizes(students_sorted, bilets_sorted);
    students_sorted.print_list();

    return;
}






//
//
//#include <iostream>
//#include <string>
//#include <map>
//using namespace std;
//
//class Node {
//public:
//    string data;
//    Node* next;
//    bool mark;
//
//    Node(const string& data) : data(data), next(nullptr), mark(false) {}
//};
//
//class CList {
//public:
//    Node* head;
//
//    CList() : head(nullptr) {}
//
//    void append(const string& data) {
//        Node* new_node = new Node(data);
//        if (!head) {
//            new_node->next = new_node;
//            head = new_node;
//        }
//        else {
//            Node* current = head;
//            while (current->next != head) {
//                current = current->next;
//            }
//            current->next = new_node;
//            new_node->next = head;
//        }
//    }
//
//    void print_list() const {
//        if (!head) {
//            cout << "Circular Linked List is empty\n";
//            return;
//        }
//        Node* current = head;
//        do {
//            cout << current->data << " ";
//            current = current->next;
//        } while (current != head);
//        cout << "\n";
//    }
//
//    int count_nodes() const {
//        if (!head) return 0;
//        int cnt = 1;
//        Node* current = head;
//        while (current->next != head) {
//            cnt++;
//            current = current->next;
//        }
//        return cnt;
//    }
//};
//
//class Node2 {
//public:
//    map<string, string> data;
//    Node2* next;
//    bool mark;
//
//    Node2(const string& first, const string& second) : next(nullptr), mark(false) {
//        data["first"] = first;
//        data["second"] = second;
//    }
//};
//
//class CList2 {
//public:
//    Node2* head;
//
//    CList2() : head(nullptr) {}
//
//    void append(const string& first, const string& second) {
//        Node2* new_node = new Node2(first, second);
//        if (!head) {
//            new_node->next = new_node;
//            head = new_node;
//        }
//        else {
//            Node2* current = head;
//            while (current->next != head) {
//                current = current->next;
//            }
//            current->next = new_node;
//            new_node->next = head;
//        }
//    }
//
//    void print_list() const {
//        if (!head) {
//            cout << "Circular Linked List is empty\n";
//            return;
//        }
//        Node2* current = head;
//        do {
//            cout << current->data["first"] << " : " << current->data["second"] << " -> ";
//            current = current->next;
//        } while (current != head);
//        cout << "\n";
//    }
//
//    int count_nodes() const {
//        if (!head) return 0;
//        int cnt = 1;
//        Node2* current = head;
//        while (current->next != head) {
//            cnt++;
//            current = current->next;
//        }
//        return cnt;
//    }
//};
//
//void winners(CList& list1, CList& list2, int k, int n) {
//    int cnt = list1.count_nodes();
//    if (k > cnt) {
//        cout << "Количество победителей не может быть больше количества участников\n";
//        return;
//    }
//    int cnt_winners = 0;
//    Node* current = list1.head;
//    int i = 0;
//    while (cnt_winners < k) {
//        if (!current->mark) {
//            i++;
//            if (i % n == 0) {
//                list2.append(current->data);
//                cnt_winners++;
//                current->mark = true;
//            }
//        }
//        current = current->next;
//    }
//}
//
//void prizes(CList2& prizes, CList& people) {
//    int cnt = prizes.count_nodes();
//
//    Node2* current = prizes.head;
//    Node* current2 = people.head;
//    for (int i = 0; i < cnt; i++) {
//        current->data["second"] = current2->data;
//        current = current->next;
//        current2 = current2->next;
//    }
//}
//
//int main() {
//    setlocale(LC_ALL, "ru");
//    CList list1;
//    CList2 listprs;
//    for (int i = 1; i <= 20; i++) {
//        list1.append("фамилия" + to_string(i));
//    }
//    for (int i = 1; i <= 5; i++) {
//        listprs.append("приз" + to_string(i), "0");
//    }
//    CList list2;
//    winners(list1, list2, 5, 5);
//    prizes(listprs, list2);
//    listprs.print_list();
//    return 0;
//}



//#include <iostream>
//#include <string>
//#include <map>
//using namespace std;
//
//class Node {
//public:
//    string data;
//    Node* next;
//    bool mark;
//
//    Node(const string& data) : data(data), next(nullptr), mark(false) {}
//};
//
//class CList {
//public:
//    Node* head;
//
//    CList() : head(nullptr) {}
//
//    void append(const string& data) {
//        Node* new_node = new Node(data);
//        if (!head) {
//            new_node->next = new_node;
//            head = new_node;
//        }
//        else {
//            Node* current = head;
//            while (current->next != head) {
//                current = current->next;
//            }
//            current->next = new_node;
//            new_node->next = head;
//        }
//    }
//
//    void print_list() const {
//        if (!head) {
//            cout << "Circular Linked List is empty\n";
//            return;
//        }
//        Node* current = head;
//        do {
//            cout << current->data << " ";
//            current = current->next;
//        } while (current != head);
//        cout << "\n";
//    }
//
//    int count_nodes() const {
//        if (!head) return 0;
//        int cnt = 1;
//        Node* current = head;
//        while (current->next != head) {
//            cnt++;
//            current = current->next;
//        }
//        return cnt;
//    }
//
//    void each_n(CList& list2, int n) {
//        int cnt = count_nodes();
//        int cnt_appends = 0;
//        Node* current = head;
//        int i = 0;
//        while (cnt_appends < cnt) {
//            if (!current->mark) {
//                i++;
//                if (i % n == 0) {
//                    list2.append(current->data);
//                    cnt_appends++;
//                    current->mark = true;
//                }
//            }
//            current = current->next;
//        }
//    }
//};
//
//class Node2 {
//public:
//    map<string, string> data;
//    Node2* next;
//    bool mark;
//
//    Node2(const string& first, const string& second) : next(nullptr), mark(false) {
//        data["first"] = first;
//        data["second"] = second;
//    }
//};
//
//class CList2 {
//public:
//    Node2* head;
//
//    CList2() : head(nullptr) {}
//
//    void append(const string& first, const string& second) {
//        Node2* new_node = new Node2(first, second);
//        if (!head) {
//            new_node->next = new_node;
//            head = new_node;
//        }
//        else {
//            Node2* current = head;
//            while (current->next != head) {
//                current = current->next;
//            }
//            current->next = new_node;
//            new_node->next = head;
//        }
//    }
//
//    void print_list() const {
//        if (!head) {
//            cout << "Circular Linked List is empty\n";
//            return;
//        }
//        Node2* current = head;
//        do {
//            cout << current->data["first"] << " : " << current->data["second"] << " -> ";
//            current = current->next;
//        } while (current != head);
//        cout << "\n";
//    }
//
//    int count_nodes() const {
//        if (!head) return 0;
//        int cnt = 1;
//        Node2* current = head;
//        while (current->next != head) {
//            cnt++;
//            current = current->next;
//        }
//        return cnt;
//    }
//
//    void each_n(CList2& list2, int n) {
//        int cnt = count_nodes();
//        int cnt_appends = 0;
//        Node2* current = head;
//        int i = 0;
//        while (cnt_appends < cnt) {
//            if (!current->mark) {
//                i++;
//                if (i % n == 0) {
//                    list2.append(current->data["first"], current->data["second"]);
//                    cnt_appends++;
//                    current->mark = true;
//                }
//            }
//            current = current->next;
//        }
//    }
//
//};
//
//void winners(CList& list1, CList& list2, int k, int n) {
//    int cnt = list1.count_nodes();
//    if (k > cnt) {
//        cout << "Количество победителей не может быть больше количества участников\n";
//        return;
//    }
//    int cnt_winners = 0;
//    Node* current = list1.head;
//    int i = 0;
//    while (cnt_winners < k) {
//        if (!current->mark) {
//            i++;
//            if (i % n == 0) {
//                list2.append(current->data);
//                cnt_winners++;
//                current->mark = true;
//            }
//        }
//        current = current->next;
//    }
//}
//
//void prizes(CList2& prizes, CList& people) {
//    int cnt = prizes.count_nodes();
//
//    Node2* current = prizes.head;
//    Node* current2 = people.head;
//    for (int i = 0; i < cnt; i++) {
//        current->data["second"] = current2->data;
//        current = current->next;
//        current2 = current2->next;
//    }
//}
//
//int main() {
//    setlocale(LC_ALL, "ru");
//    CList2 students;
//    CList2 students_sorted;
//    CList bilets;
//    CList bilets_sorted;
//    for (int i = 1; i <= 20; i++) {
//        students.append("фамилия" + to_string(i), "0");
//    }
//    for (int i = 1; i <= 10; i++) {
//        bilets.append("билет" + to_string(i));
//    }
//    CList list2;
//    students.each_n(students_sorted, 3);
//    bilets.each_n(bilets_sorted, 2);
//    prizes(students_sorted, bilets_sorted);
//    students_sorted.print_list();
//    return 0;
//}
