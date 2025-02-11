//
//  main.cpp
//  Algorithms&DataStructures
//
//  Created by Максим Гоглов on 04.02.2025.
//
#include "header.h"
#include "firstlaboratory.hpp"
#include "secondlaboratory.hpp"


int main(int argc, const char * argv[])
{
    setlocale(LC_ALL, "Russian");
    char menu = 'n';
    while (menu != 'e' || menu != 'E')
    {
        system("clear");
        cout << "Дисциплина: Алгоритмы и структуры данных" << endl;
        cout << "Разработчик: студент Гоглов М. А.\n" << endl;
        cout << "1) Лабораторная работа №1" << endl;
        cout << "E) Выход из программы" << endl;
        cin >> menu;
        system("clear");
        cout << endl << endl;
        switch (menu)
        {
            case '1': FirstLaboratoryMenu(); break;
            case '2': SecondLaboratoryMenu(); break;
        }
    }
    
    return 0;
}
