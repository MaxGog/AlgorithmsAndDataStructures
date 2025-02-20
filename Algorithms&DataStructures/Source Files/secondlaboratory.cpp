//
//  secondlaboratory.cpp
//  Algorithms&DataStructures
//
//  Created by Максим Гоглов on 06.02.2025.
//

#include "Header.h"

struct Node
{
    int data;
    Node* next;
    Node() : data(NULL), next(nullptr) {};
    Node(int value) : data(value), next(nullptr) {};
};

class Linkedlist
{
    Node* head;
    
public:
    Linkedlist() : head(NULL){};
    
    Linkedlist* copy(Linkedlist* list)
    {
        Node* curr = list->head; // Используем переданный список
        
        // Создаем новый список для копирования
        Linkedlist* newList = new Linkedlist();
        
        while (curr)
        {
            newList->insertAtEnd(curr->data);
            curr = curr->next;
        }
        
        return newList;
    }
    
    void addList(Linkedlist* list)
    {
        Node* curr = list->head; // Используем переданный список
        
        while (curr) {
            this->insertAtEnd(curr->data);
            curr = curr->next;
        }
    }
    
    void insertAtBeginning(int value)
    {
        Node* newNode = new Node(value);
        newNode->next = head;
        head = newNode;
    }
    
    void insertAtEnd(int value)
    {
        Node* newNode = new Node(value);
        newNode->next = NULL;
        if (!head) {
            head = newNode;
            return;
        }
        Node* temp = head;
        while (temp->next) {
            temp = temp->next;
        }
        temp->next = newNode;
    }
    
    void insertAtPosition(int value, int position)
    {
        if (position < 1)
        {
            cout << "Позиция должна быть >= 1." << endl;
            return;
        }
        
        if (position == 1)
        {
            insertAtBeginning(value);
            return;
        }
        
        Node* newNode = new Node(value);
        
        Node* temp = head;
        for (int i = 1; (i < position - 1) && temp; ++i)
        {
            temp = temp->next;
        }
        
        if (!temp)
        {
            cout << "Такой позиции нет." << endl;
            delete newNode;
            return;
        }
        
        newNode->next = temp->next;
        temp->next = newNode;
    }
    
    void deleteFromBeginning()
    {
        if (!head)
        {
            cout << "Список пуст." << endl;
            return;
        }
        
        Node* temp = head;
        head = head->next;
        delete temp;
    }
    
    void deleteFromEnd()
    {
        if (!head)
        {
            cout << "Список пуст." << endl;
            return;
        }
        
        if (!head->next)
        {
            delete head;
            head = NULL;
            return;
        }
        
        Node* temp = head;
        while (temp->next->next)
        {
            temp = temp->next;
        }
        
        delete temp->next;
        temp->next = NULL;
    }
    
    void deleteFromPosition(int position)
    {
        if (position < 1)
        {
            cout << "Позиция должна быть >= 1." << endl;
            return;
        }
        
        if (position == 1)
        {
            deleteFromBeginning();
            return;
        }
        
        Node* temp = head;
        for (int i = 1; i < position - 1 && temp; ++i)
        {
            temp = temp->next;
        }
        if (!temp && !temp->next)
        {
            cout << "Такой позиции нет.\n";
            return;
        }
        Node* nodeToDelete = temp->next;
        temp->next = temp->next->next;
        delete nodeToDelete;
    }
    
    void deleteEachSecond() {
        int length = this->getLength();
        int count = 0;
        for (int i = 2; i < length - count; ++i)
        {
            deleteFromPosition(i);
            count++;
        }
    }
    
    void deleteEachThird()
    {
        int length = this->getLength();
        int count = 0;
        for (int i = 3; i < length - count; i = i + 2)
        {
            deleteFromPosition(i);
            count++;
        }
    }
    
    int getLength()
    {
        Node* curr = head;
        int count = 0;
        while (curr) {
            curr = curr->next;
            count++;
        }
        return count;
    }
    
    int getElementByPos(int index)
    {
        Node* curr = head;
        int count = 0;
        while (curr)
        {
            if (count == index)
            {
                return curr->data;
            }
            curr = curr->next;
            count++;
        }
        return 0;
    }

    void moveElement(int elementPos, int addPos)
    {
        int element = getElementByPos(elementPos);
        deleteFromPosition(elementPos+1);
        elementPos = elementPos + addPos;
        insertAtPosition(element, elementPos);

    }

    void swap(Node* pos1, Node* pos2)
    {
        Node* first;
        Node* second;
        first = pos1;
        second = pos2;
    }

    void Sort() { };

    void display()
    {
        Node* temp = head;

        if (head == NULL)
        {
            cout << "Список пуст" << endl;
            return;
        }

        while (temp != NULL)
        {
            cout << temp->data << " ";
            temp = temp->next;
        }
    }

    void Clear()
    {
        Node* curr = head;

        while (head != NULL)
        {
            deleteFromBeginning();
        }
    }

    ~Linkedlist()
    {
        if (!head) return;
        Node* curr = head;
        Node* temp;
        do {
            temp = curr;
            curr = curr->next;
            delete temp;
        } while (curr != nullptr);
    }
};



struct CNode
{
    int data;
    CNode* next;
    CNode(int value) : data(value), next(nullptr) {}
};


class CircularLinkedList
{
private:
    CNode* head;
public:
    CircularLinkedList() : head(nullptr) {}

    void insertAtBeginning(int value)
    {
        CNode* newNode = new CNode(value);
        if (!head)
        { //если список пуст
            head = newNode;
            newNode->next = head;
        }
        else
        {
            CNode* temp = head; //находим последний элемент
            while (temp->next != head)
            {
                temp = temp->next;
            }
            temp->next = newNode;
            newNode->next = head;
            head = newNode; //не забываю в моём случае указать вновь позицию первого элемента (новоиспечённого)
        }
    }

    void insertAtEnd(int value)
    {
        CNode* newNode = new CNode(value);
        if (!head)
        { //если список пуст
            head = newNode;
            newNode->next = head;
        }
        else
        {
            CNode* temp = head; //находим последний элемент
            while (temp->next != head)
            {
                temp = temp->next;
            }
            //последний элемент теперь указывает на новый элемент, а новый на первый
            temp->next = newNode;
            newNode->next = head;
        }
    }

    void insertAtPosition(int value, int position)
    {
        if (position < 1)
        {
            cout << "Позиция должна быть >= 1." << endl;
            return;
        }

        if (position == 1)
        {
            insertAtBeginning(value);
            return;
        }

        CNode* newNode = new CNode(value);
        CNode* temp = head;

        for (int i = 1; (i < position - 1) && temp; ++i)
        {
            temp = temp->next;
        }
        if (!temp)
        {
            cout << "Такой позиции нет." << endl;
            delete newNode;
            return;
        }
        newNode->next = temp->next;
        temp->next = newNode;
    }

    void deleteFromBeginning()
    {
        if (!head)
        {
            cout << "Список пуст." << endl;
            return;
        }

        CNode* temp = head;
        CNode* tail = head;

        while (tail->next != head) { tail = tail->next; }
        head = head->next;
        tail->next = head;

        delete temp;
    }

    void deleteFromEnd()
    {
        if (!head)
        {
            cout << "Список пуст." << endl;
            return;
        }

        if (!head->next)
        {
            delete head;
            head = NULL;
            return;
        }

        CNode* temp = head;
        while (temp->next->next != head)
        {
            temp = temp->next;
        }

        delete temp->next;
        temp->next = head;
    }

    void deleteFromPosition(int position)
    {
        if (position < 1)
        {
            cout << "Позиция должна быть >= 1." << endl;
            return;
        }

        if (position == 1)
        {
            //deleteFromBeginning();
            return;
        }

        CNode* temp = head;
        for (int i = 1; i < position - 1 && temp; ++i)
        {
            temp = temp->next;
        }

        if (!temp || !temp->next)
        {
            cout << "Такой позиции нет." << endl;
            return;
        }
        CNode* nodeToDelete = temp->next;
        temp->next = temp->next->next;
        delete nodeToDelete;
    }

    void display()
    {
        if (!head) return;
        CNode* curr = head;
        do {
            std::cout << curr->data << " ";
            curr = curr->next;
        } while (curr != head);
        std::cout << std::endl;
    }

    ~CircularLinkedList()
    {
        if (!head) return;
        CNode* curr = head;
        CNode* temp;
        do {
            temp = curr;
            curr = curr->next;
            delete temp;
        } while (curr != head);
    }
};

void SecondLaboratoryMenu()
{
    char menu = 'n';
    while (menu != 'e')
    {
        
        Linkedlist list, list2;
        int value = 0;
        list.insertAtBeginning(54);
        list.insertAtBeginning(38);
        list.insertAtBeginning(92);
        
        
        //list.insertAtPosition(11, 2);
        //list.insertAtPosition(12, 2);
        //list.insertAtPosition(13, 2);
        //list.insertAtPosition(14, 2);
        
        
        system("clear");
        cout << "Лабораторная работа №2\nОдносвязные списки" << endl;
        cout << "1) Передвижения элемента на n позиций." << endl;
        cout << "2) Создать копию списка." << endl;
        cout << "3) Добавить элемент в начало списка." << endl;
        cout << "4) Склеить два списка." << endl;
        cout << "5) Удалить n-ый элемент из списка." << endl;
        cout << "6) Добавить элемент на n-ую позицию из списка." << endl;
        cout << "7) Удалить каждый второй элемент списка." << endl;
        cout << "8) Удалить каждый третий элемент списка." << endl;
        cout << "9) Очистить список." << endl << endl;
        cout << "A) 1-е инд. задание." << endl;
        cout << "B) 2-е инд. задание." << endl;
        cout << "C) 3-е инд. задание." << endl;
        cout << "D) 4-е инд. задание." << endl;
        cout << "F) 5-е инд. задание." << endl;
        cout << "J) 6-е инд. задание." << endl;
        cin >> menu;
        system("clear");
        cout << endl << endl;
        
        if (menu == '1')
        {
            cout << "1) Передвижения элемента на n позиций." << endl;
            
            Linkedlist list;
            list.insertAtBeginning(54);
            list.insertAtBeginning(38);
            list.insertAtBeginning(92);
            list.insertAtBeginning(33);
            list.insertAtBeginning(45);
            cout << "Оригинальный список: ";
            list.display();
            cout << endl;
            
            int value, count;
            cout << "Введите, какой элемент нужно передвинуть: ";
            cin >> value;
            cout << "Введите, на сколько позиций нужно передвинуть: ";
            cin >> count;
            
            list.moveElement(value, count);
            
            cout << "Изменённый список: ";
            list.display();
        }
        else if (menu == '2')
        {
            cout << "2) Создать копию списка." << endl;
            
            Linkedlist list;
            list.insertAtBeginning(54);
            list.insertAtBeginning(38);
            list.insertAtBeginning(92);
            list.insertAtBeginning(33);
            list.insertAtBeginning(45);
            cout << "Оригинальный список: ";
            list.display();
            cout << endl;
            
            Linkedlist* copiedList = list.copy(&list);
            
            cout << "Копия списка: ";
            copiedList->display();
            delete copiedList;
        }
        else if (menu == '3')
        {
            cout << "3) Добавить элемент в начало списка." << endl;
            
            Linkedlist list;
            list.insertAtBeginning(54);
            list.insertAtBeginning(38);
            list.insertAtBeginning(92);
            list.insertAtBeginning(33);
            list.insertAtBeginning(45);
            cout << "Оригинальный список: ";
            list.display();
            cout << endl;
            
            cout << "Введите значение элемента: ";
            cin >> value;
            list.insertAtBeginning(value);
            
            cout << "Изменённый список: ";
            list.display();
        }
        else if (menu == '4')
        {
            cout << "4) Склеить два списка." << endl;
            
            Linkedlist list, list2;
            list.insertAtBeginning(54);
            list.insertAtBeginning(38);
            list.insertAtBeginning(92);
            list.insertAtBeginning(33);
            list.insertAtBeginning(45);
            cout << "Оригинальный список: ";
            list.display();
            cout << endl;
            
            list2.insertAtBeginning(40);
            list2.insertAtBeginning(50);
            list2.insertAtBeginning(60);
            
            cout << "Второй список: ";
            list2.display();
            cout << endl;
            
            list.addList(&list2);
            
            cout << "\nОбъединённый список: ";
            list.display();
        }
        else if (menu == '5')
        {
            cout << "5) Удалить n-ый элемент из списка." << endl;
            
            Linkedlist list;
            list.insertAtBeginning(54);
            list.insertAtBeginning(38);
            list.insertAtBeginning(92);
            list.insertAtBeginning(33);
            list.insertAtBeginning(45);
            cout << "Оригинальный список: ";
            list.display();
            
            int count = 0;
            cout << "Введите позицию удаления элемента: ";
            cin >> count;
            cout << endl;
            
            list.deleteFromPosition(count);
            cout << "\nУдалён элемент на n позиции: ";
            list.display();
        }
        else if (menu == '6')
        {
            cout << "6) Добавить элемент на n-ую позицию из списка." << endl;
            
            Linkedlist list;
            list.insertAtBeginning(54);
            list.insertAtBeginning(38);
            list.insertAtBeginning(92);
            list.insertAtBeginning(33);
            list.insertAtBeginning(45);
            cout << "Оригинальный список: ";
            list.display();
            cout << endl;
            
            int count = 0, value = 0;
            cout << "Введите значение элемента: ";
            cin >> value;
            cout << "Введите позицию элемента: ";
            cin >> count;
            
            list.insertAtPosition(value, count);
            cout << "\nДобавлен элемент на n позицию: ";
            list.display();
        }
        else if (menu == '7')
        {
            cout << "9) Удалить каждый второй элемент списка." << endl;
            
            Linkedlist list;
            list.insertAtBeginning(54);
            list.insertAtBeginning(38);
            list.insertAtBeginning(92);
            list.insertAtBeginning(33);
            list.insertAtBeginning(45);
            cout << "Оригинальный список: ";
            list.display();
            cout << endl;
            
            list.deleteEachSecond();
            cout << "\nУдалён каждый 2: ";
            list.display();
        }
        else if (menu == '8')
        {
            cout << "10) Удалить каждый третий элемент списка." << endl;
            
            Linkedlist list;
            list.insertAtBeginning(54);
            list.insertAtBeginning(38);
            list.insertAtBeginning(92);
            list.insertAtBeginning(33);
            list.insertAtBeginning(45);
            list.insertAtBeginning(52);
            list.insertAtBeginning(13);
            list.insertAtBeginning(74);
            cout << "Оригинальный список: ";
            list.display();
            cout << endl;
            
            list.deleteEachThird();
            cout << "\nУдалён каждый 3: ";
            list.display();
        }
        else if (menu == '9')
        {
            cout << "c) Очистить список." << endl;
            
            Linkedlist list;
            list.insertAtBeginning(54);
            list.insertAtBeginning(38);
            list.insertAtBeginning(92);
            list.insertAtBeginning(33);
            list.insertAtBeginning(45);
            cout << "Оригинальный список: ";
            list.display();
            cout << endl;
            
            list.Clear();
            cout << "\nОчищен: ";
            list.display();
        }
        else if (menu == 'a') { FirstIndividualSecondLab(); }
        else if (menu == 'b') { SecondIndividualSecondLab(); }
        else if (menu == 'c') { ThirdIndividualSecondLab(); }
        else if (menu == 'd') { FourthIndividualSecondLab(); }
        else if (menu == 'f') { FivethIndividualSecondLab(); }
        else if (menu == 'j') { SixthIndividualSecondLab(); }
            
            
        cout << endl << endl;
    }
}
