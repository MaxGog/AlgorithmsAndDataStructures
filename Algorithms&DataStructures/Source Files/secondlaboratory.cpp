//
//  secondlaboratory.cpp
//  Algorithms&DataStructures
//
//  Created by Максим Гоглов on 06.02.2025.
//

#include "secondlaboratory.hpp"

void ViewArray(int array[], int count)
{
    cout << "ID" << "\t\t" << "Элемент" << endl;
    for (int i = 0; i < count; i++)
    {
        cout << i << "\t\t" << array[i] << endl;
    }
}

void GetArray(int* array, int count)
{
    if (count == 0)
    {
        cout << "Массив не может быть пустым" << endl;
        return;
    }
    for (int i = 0; i < count; i++)
    {
        cout << "Введите " << i << " элемент: ";
        cin >> array[i];
    }
}

void SecondLaboratoryMenu()
{
    char menu = 'n';
    while (menu != 'e' || menu != 'E')
    {
        system("clear");
        cout << "Лабораторная работа №2\nОдносвязные списки" << endl;
        cout << "1) Передвижения элемента на n позиций." << endl;
        cout << "2) Создать копию списка." << endl;
        cout << "3) Добавить элемент в начало списка." << endl;
        cout << "4) Склеить два списка." << endl;
        cout << "5) Удалить n-ый элемент из списка." << endl;
        cout << "6) Вставить элемент после n-го элемента списка." << endl;
        cout << "7) Создать список содержащий элементы общие для двух списков." << endl;
        cout << "8) Упорядочить элементы в списке по возрастанию." << endl;
        cout << "9) Удалить каждый второй элемент списка." << endl;
        cout << "A) Удалить каждый третий элемент списка." << endl;
        cout << "B) Упорядочить элементы списка по убыванию." << endl;
        cout << "C) Очистить список." << endl;
        cin >> menu;
        system("clear");
        cout << endl << endl;
        switch (menu)
        {
            case '1': FirstTaskSecondLab(); break;
            case '2': SecondLaboratoryMenu(); break;
            case '3': ThirdTaskSecondLab(); break;
            case '4': FourthTaskSecondLab(); break;
            case '5': FivethTaskSecondLab(); break;
            case '6': SixthTaskSecondLab(); break;
            case '7': SeventhTaskSecondLab(); break;
            case '8': EigthTaskSecondLab(); break;
            case '9': NinethTaskSecondLab(); break;
            case 'a': TenthTaskSecondLab(); break;
            case 'b': EleventhTaskSecondLab(); break;
            case 'c': TwelvethTaskSecondLab(); break;
        }
    }
}

void FirstTaskSecondLab()
{
    int count = 0;
    cout << "Введите кол-во элементов массива: ";
    cin >> count;
    int* array = new int[count];
    GetArray(array, count);
    ViewArray(array, count);
    
    int offset = 0;
    int idElement = 0;
    cout << "\n\nВведите номер передвигаемого элемента: ";
    cin >> idElement;
    cout << "Введите, насколько позиций передвинуть элемент: ";
    cin >> offset;
    
    if (idElement > count) { cout << "Такого элемента не существует." << endl; return; }
    int temp = array[idElement];
    if (idElement + offset > count) { array[idElement + offset - count] = temp; }
    else { array[idElement + offset] = temp; }
    array[idElement] = 0;
    
    cout << "Задание №1: передвижение элемента на n позиций" << endl;
    ViewArray(array, count);
    delete[] array;
    return;
}

void SecondTaskSecondLab()
{
    int count = 0;
    cout << "Введите кол-во элементов массива: ";
    cin >> count;
    int* array = new int[count];
    GetArray(array, count);
    ViewArray(array, count);
    
    int* newArray = new int[count];
    for (int i = 0; i < count; i++)
    {
        newArray[i] = array[i];
    }
    
    cout << "Задание №2: создать копию списка" << endl;
    ViewArray(newArray, count);
    delete[] array;
    delete[] newArray;
    return;
}

void ThirdTaskSecondLab()
{
    int count = 0;
    cout << "Введите кол-во элементов массива: ";
    cin >> count;
    int* array = new int[count];
    GetArray(array, count);
    ViewArray(array, count);
    
    int newElement = 0;
    cout << "Введите значение нового элемента в начало списка: ";
    cin >> newElement;
    
    int* newArray = new int[count + 1];
    newArray[0] = newElement;
    
    for (int i = 0; i < count + 1; i++) { newArray[i + 1] = array[i]; }
    
    cout << "Задание №3: вставить новый элемент в начало списка" << endl;
    ViewArray(newArray, count + 1);
    delete[] array;
    delete[] newArray;
    return;
}

void FourthTaskSecondLab()
{
    int count = 0;
    cout << "Введите кол-во элементов массива: ";
    cin >> count;
    int* array = new int[count];
    GetArray(array, count);
    ViewArray(array, count);
    
    int secondCount = 0;
    cout << "Введите кол-во элементов второго массива: ";
    cin >> secondCount;
    int* secondArray = new int[secondCount];
    GetArray(secondArray, secondCount);
    ViewArray(secondArray, secondCount);
    
    int newCount = count + secondCount;
    int* newArray = new int[newCount];
    for (int i = 0; i < count; i++) { newArray[i] = array[i]; }
    for (int i = 0; i < secondCount; i++) { newArray[count + i] = secondArray[i]; }
    
    cout << "Задание №4: склеить два списка" << endl;
    ViewArray(newArray, newCount);
    
    delete[] array;
    delete[] secondArray;
    delete[] newArray;
    return;
}

void FivethTaskSecondLab()
{
    int count = 0;
    cout << "Введите кол-во элементов массива: ";
    cin >> count;
    int* array = new int[count];
    GetArray(array, count);
    ViewArray(array, count);
    
    int newCount = count - 1;
    int* newArray = new int[newCount];
    
    int idRemove = 0;
    cout << "Введите индекс элемента, который требуется удалить: ";
    cin >> idRemove;
    
    for (int i = 0; i < idRemove; i++) { newArray[i] = array[i]; }
    for (int i = idRemove + 1; i < newCount + 1; i++) { newArray[i - 1] = array[i]; }
    
    cout << "Задание №5: удалить n-ый элемент из списка" << endl;
    ViewArray(newArray, newCount);
    
    delete[] array;
    delete[] newArray;
    return;
}

void SixthTaskSecondLab()
{
    int count = 0;
    cout << "Введите кол-во элементов массива: ";
    cin >> count;
    int* array = new int[count];
    GetArray(array, count);
    ViewArray(array, count);
    
    int newCount = count + 1;
    int* newArray = new int[newCount];
    
    int idAdd = 0;
    cout << "Введите индекс элемента, после которого надо вставить новый элемент: ";
    cin >> idAdd;
    
    int newElement = 0;
    cout << "Введите значение нового элемента: ";
    cin >> newElement;
    
    for (int i = 0; i <= idAdd; i++) { newArray[i] = array[i]; }
    array[idAdd + 1] = newElement;
    for (int i = idAdd + 2; i < newCount; i++) { newArray[i] = array[i - 1]; }
    
    cout << "Задание №6: вставить элемент после n-ого элемента" << endl;
    ViewArray(newArray, newCount);
    
    delete[] array;
    delete[] newArray;
    return;
}

void SeventhTaskSecondLab()
{
    int count = 0;
    cout << "Введите кол-во элементов массива: ";
    cin >> count;
    int* array = new int[count];
    GetArray(array, count);
    ViewArray(array, count);
    
    int secondCount = 0;
    cout << "Введите кол-во элементов второго массива: ";
    cin >> secondCount;
    int* secondArray = new int[secondCount];
    GetArray(secondArray, secondCount);
    ViewArray(secondArray, secondCount);
    
    int tempCount = 0;
    if (count > secondCount) { tempCount = secondCount; }
    else { tempCount = count; }
    
    int tempArray[tempCount];
    int tempI = 0;
    bool isNewElement = true;
    
    for (int i = 0; i < count; i++)
    {
        for (int j = 0; j < secondCount; j++)
        {
            if (array[i] == secondArray[j])
            {
                for (int g = 0; g < tempI; g++)
                {
                    for (int gg = 1; gg < tempI; gg++)
                    {
                        if (tempArray[g] == tempArray[gg])
                        {
                            isNewElement = false;
                        }
                    }
                }
                if (isNewElement)
                {
                    tempArray[tempI] = array[i];
                    tempI++;
                }
                isNewElement = true;
                break;
            }
        }
    }
    
    int newCount = tempI;
    int* newArray = new int[newCount];
    
    for (int i = 0; i < newCount; i++) { newArray[i] = tempArray[i]; }
    
    cout << "Задание №7: Создать список содержащий элементы общие для двух списков" << endl;
    ViewArray(newArray, newCount);
    
    delete[] array;
    delete[] secondArray;
    delete[] newArray;
    return;
}

void EigthTaskSecondLab()
{
    int count = 0;
    cout << "Введите кол-во элементов массива: ";
    cin >> count;
    int* array = new int[count];
    GetArray(array, count);
    ViewArray(array, count);
    
    for (int i = 0; i < count; i++)
    {
        for (int j = 1; j < count; j++)
        {
            if (array[i] >= array[j])
            {
                int temp = array[i];
                array[i] = array[j];
                array[j] = temp;
            }
        }
    }
    
    cout << "Задание №8: отсортировать список по возростанию" << endl;
    ViewArray(array, count);
    delete[] array;
    return;
}

void EleventhTaskSecondLab()
{
    int count = 0;
    cout << "Введите кол-во элементов массива: ";
    cin >> count;
    int* array = new int[count];
    GetArray(array, count);
    ViewArray(array, count);
    
    for (int i = 0; i < count; i++)
    {
        for (int j = 1; j < count; j++)
        {
            if (array[i] <= array[j])
            {
                int temp = array[i];
                array[i] = array[j];
                array[j] = temp;
            }
        }
    }
    
    cout << "Задание №8: отсортировать список по убыванию" << endl;
    ViewArray(array, count);
    delete[] array;
    return;
}

void NinethTaskSecondLab()
{
    int count = 0;
    cout << "Введите кол-во элементов массива: ";
    cin >> count;
    int* array = new int[count];
    GetArray(array, count);
    ViewArray(array, count);
    
    int newCount = count / 2;
    if (count % 2 != 0) { newCount++; }
    int* newArray = new int[newCount];
    for (int i = 0, j = 0; i < count; i += 2, j++)
    {
        newArray[j] = array[i];
    }
    
    cout << "\nЗадание №9: удалить каждый второй элемент" << endl;
    ViewArray(newArray, newCount);
    delete[] newArray;
    delete[] array;
}

void TenthTaskSecondLab()
{
    int count = 0;
    cout << "Введите кол-во элементов массива: ";
    cin >> count;
    int* array = new int[count];
    GetArray(array, count);
    ViewArray(array, count);
    
    int newCount = count / 3;
    if (count % 3 != 0) { newCount++; }
    int* newArray = new int[newCount];
    for (int i = 0, j = 0; i < count; i += 3, j++)
    {
        newArray[j] = array[i];
    }
    
    cout << "\nЗадание №10ы: удалить каждый третий элемент" << endl;
    ViewArray(newArray, newCount);
    delete[] newArray;
    delete[] array;
}

void TwelvethTaskSecondLab()
{
    int count = 0;
    cout << "Введите кол-во элементов массива: ";
    cin >> count;
    int* array = new int[count];
    GetArray(array, count);
    ViewArray(array, count);
    
    for (int i = 0; i < count; i++)
    {
        array[i] = 0;
    }
    
    cout << "Задание №12: отчистить список" << endl;
    ViewArray(array, count);
    delete[] array;
    return;
}
