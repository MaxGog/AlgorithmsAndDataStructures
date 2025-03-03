//
//  main.cpp
//  Algorithms&DataStructures
//
//  Created by Максим Гоглов on 04.02.2025.
//

#include "firstlaboratory.h"
#include "secondlaboratory.h"
#include "thirdlaboratory.h"

void MainMenu()
{
    char menu = 'n';
    while (menu != '0')
    {
        cout << "\nДисциплина: Алгоритмы и структуры данных" << endl;
        cout << "Разработчик: студент Гоглов М. А.\n" << endl;
        cout << "1) Лабораторная работа №1" << endl;
        cout << "2) Лабораторная работа №2" << endl;
        cout << "3) Лабораторная работа №3" << endl;
        cout << "0) Выход из программы" << endl;
        cout << "Выберите пункт меню: ";
        cin >> menu;
        cout << endl << endl;
        switch (menu)
        {
            case '1': FirstLaboratoryMenu(); break;
            case '2': SecondLaboratoryMenu(); break;
            case '3': ThirdLaboratoryMenu(); break;
        }
    }
}


int main(int argc, const char * argv[])
{
    setlocale(LC_ALL, "Russian");
    MainMenu();
    return 0;
}

