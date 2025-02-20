//
//  fivethindividualsecondlaboratory.cpp
//  Algorithms&DataStructures
//
//  Created by Максим Гоглов on 20.02.2025.
//

#include "Header.h"

class CList6 {
private:
    NodeWithMark* head;
public:
    CList6() {
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

    pair<int, string> josephus(int n) {  // Изменено на возврат пары
        int cnt = count_nodes();
        int cnt_kills = 0;
        NodeWithMark* current = head;
        int i = 0;
        while (cnt_kills < cnt - 1) {
            if (!current->mark) {
                i++;
                if (i % n == 0) {
                    cnt_kills++;
                    current->mark = true;
                }
            }
            current = current->next;
        }

        // Находим последнего оставшегося игрока
        current = head;
        int index = 1;
        while (current->mark) {
            current = current->next;
            index++;
        }

        return make_pair(index, current->data);  // Возвращаем индекс и значение
    }
};

void FivethIndividualSecondLab()
{
    CList6 list1;
    ifstream file("data.txt");
    if (!file) {
        cerr << "Ошибка: не удалось открыть data.txt" << endl;
        return;
    }
    string line;
    while (getline(file, line)) {
        list1.append(line);
    }
    file.close();

    list1.print_list();

    pair<int, string> result = list1.josephus(4);
    cout << "Начальная позиция k-го игрока: " << result.first << endl;
    cout << "Значение на этой позиции: " << result.second << endl;

    return;
}

