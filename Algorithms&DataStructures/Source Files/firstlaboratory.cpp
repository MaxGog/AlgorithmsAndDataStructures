//
//  firstlaboratory.cpp
//  Algorithms&DataStructures
//
//  Created by Максим Гоглов on 04.02.2025.
//

#include "firstlaboratory.hpp"

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

void FirstTaskFirstLab()
{
    int count = 0;
    cout << "Введите кол-во элементов массива: ";
    cin >> count;
    int* array = new int[count];
    GetArray(array, count);
    ViewArray(array, count);
    
    int temp = array[0];
    array[0] = array[count - 1];
    array[count - 1] = temp;
    
    cout << "\nЗадание 1: поменять местами первый и последний элемент" << endl;
    ViewArray(array, count);
    delete[] array;
}

void SecondTaskFirstLab()
{
    int count = 0;
    cout << "Введите кол-во элементов массива: ";
    cin >> count;
    int* array = new int[count];
    GetArray(array, count);
    ViewArray(array, count);
    
    int newCount = 0;
    if (count % 2 == 0) { newCount = count / 2; }
    else { newCount = (count - 1) / 2; }
    
    for (int i = 0; i < newCount; i++)
    {
        int temp = array[i];
        array[i] = array[count - i - 1];
        array[count - i - 1] = temp;
    }
    
    cout << "\nЗадание 2: перевернуть массив" << endl;
    cout << "Индекс" << "\t\t" << "Элемент массива" << endl;
    ViewArray(array, count);
    delete[] array;
}

void ThirdTaskFirstLab()
{
    int count = 0;
    cout << "Введите кол-во элементов массива: ";
    cin >> count;
    int* array = new int[count];
    GetArray(array, count);
    ViewArray(array, count);
    
    int temp_i;
    if (count % 2 != 0)
    {
        temp_i = ((count - 1) / 2) + 1;
        for (int i = temp_i; i < (count); i++)
        {
            array[i - 1] = array[i];
        }
        array[count - 1] = 0;
    }
    else
    {
        temp_i = count / 2;
        for (int i = temp_i; i < count - 1; i++)
        {
            array[i - 1] = array[i + 1];
            array[i] = array[i + 2];
        }
        array[count - 1] = 0;
        array[count - 2] = 0;
    }
    
    cout << "\nЗадание 3: удалить элемент в середине" << endl;
    ViewArray(array, count);
    delete[] array;
}

void FourTaskFirstLab()
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
    
    cout << "\nЗадание 4: удалить каждый второй элемент" << endl;
    ViewArray(newArray, newCount);
    delete[] newArray;
    delete[] array;
}

void FiveTaskFirstLab()
{
    int count = 0;
    cout << "Введите кол-во элементов массива: ";
    cin >> count;
    if (count == 0)
    {
        cout << "Массив не может быть пустым." << endl;
        return;
    }
    
    char* array = new char[count];
    for (int i = 0; i < count; i++)
    {
        cout << "Введите " << i << " элемент: ";
        cin >> array[i];
    }
    
    cout << "Индекс" << "\t\t" << "Элемент массива" << endl;
    for (int i = 0; i < count; i++)
    {
        cout << i << "\t\t" << array[i] << endl;
    }
    
    int newCountI;
    int newArrayCount = count + 1;
    char* newArray = new char[newArrayCount];
    
    if (count % 2 != 0)
    {
        newCountI = ((count - 1) / 2) + 1;
        for (int i = 0; i < newCountI + 1; i++)
        {
            newArray[i] = array[i];
        }
        newArray[newCountI] = '*';
        newCountI++;
        for (int i = newCountI; i < newArrayCount; i++)
        {
            newArray[i] = array[i - 1];
        }
    }
    else
    {
        newCountI = (count / 2);
        for (int i = 0; i < newCountI + 1; i++)
        {
            newArray[i] = array[i];
        }
        newArray[newCountI] = '*';
        newCountI++;
        for (int i = newCountI; i < newArrayCount; i++)
        {
            newArray[i] = array[i - 1];
        }
    }
    
    cout << "\nЗадание 5: вставить в середину звёздочку" << endl;
    cout << "ID" << "\t\t" << "Элемент" << endl;
    for (int i = 0; i < newArrayCount; i++)
    {
        cout << i << "\t\t" << newArray[i] << endl;
    }
    
    delete[] newArray;
    delete[] array;
}

void SixTaskFirstLab()
{
    int count = 0;
    cout << "Введите кол-во элементов массива: ";
    cin >> count;
    int* array = new int[count];
    GetArray(array, count);
    ViewArray(array, count);
    
    int min = array[0];
    int minCount = 0;
    for (int i = 1; i < count; i++)
    {
        if (min > array[i])
        {
            min = array[i];
            minCount = i + 1;
        }
    }
    
    int* newArray = new int[count + 1];
    for (int i = 0; i < minCount; i++)
    {
        newArray[i] = array[i];
    }
    newArray[minCount] = 0;
    minCount++;
    for (int i = minCount; i < count + 1; i++)
    {
        newArray[i] = array[i-1];
    }
    
    cout << "\nЗадание 6: вставить 0 после минимального элемента" << endl;
    ViewArray(newArray, count + 1);
    delete[] newArray;
    delete[] array;
}

void SevenTaskFirstLab()
{
    int count = 0;
    cout << "Введите кол-во элементов массива: ";
    cin >> count;
    int* array = new int[count];
    GetArray(array, count);
    ViewArray(array, count);
    
    int max = array[0];
    int maxCount = 0;
    for (int i = 1; i < count; i++)
    {
        if (max < array[i])
        {
            max = array[i];
            maxCount = i + 1;
        }
    }
    
    int* newArray = new int[count + 1];
    for (int i = 0; i < maxCount; i++)
    {
        newArray[i] = array[i];
    }
    newArray[maxCount] = 0;
    maxCount++;
    for (int i = maxCount; i < count + 1; i++)
    {
        newArray[i] = array[i-1];
    }
    
    cout << "\nЗадание 7: вставить 0 после максимального элемента" << endl;
    ViewArray(newArray, count + 1);
    delete[] newArray;
    delete[] array;
}

void EightTaskFirstLab()
{
    int count = 0;
    cout << "Введите кол-во элементов массива: ";
    cin >> count;
    int* array = new int[count];
    GetArray(array, count);
    ViewArray(array, count);
    
    int min = array[0];
    int minCount = 0;
    for (int i = 1; i < count; i++)
    {
        if (min > array[i])
        {
            min = array[i];
            minCount = i;
        }
    }
    
    int* newArray = new int[count-1];
    for (int i = 0; i < minCount; i++)
    {
        newArray[i] = array[i];
    }
    for (int i = minCount + 1; i < count; i++)
    {
        newArray[i - 1] = array[i];
    }
    
    cout << "\nЗадание 8: удалить минимальный элемент" << endl;
    ViewArray(newArray, count - 1);
    delete[] newArray;
    delete[] array;
}

void NineTaskFirstLab()
{
    int count = 0;
    cout << "Введите кол-во элементов массива: ";
    cin >> count;
    int* array = new int[count];
    GetArray(array, count);
    ViewArray(array, count);
    
    int firstItem = array[0];
    int countDuplicate = 0;
    for (int i = 1; i < count; i++) { if (array[i] == firstItem) { countDuplicate++; } }
    
    int* newArray = new int[count - countDuplicate];
    int j = 1;
    newArray[0] = array[0];
    for (int i = 1; i < count; i++)
    {
        if (array[i] != firstItem)
        {
            newArray[j] = array[i];
            j++;
        }
    }
    
    cout << "\nЗадание 9: удалить все элементы, равные первому" << endl;
    ViewArray(newArray, count - countDuplicate);
    delete[] newArray;
    delete[] array;
}

void TenTaskFirstLab()
{
    int count = 0;
    cout << "Введите кол-во элементов массива: ";
    cin >> count;
    int* array = new int[count];
    GetArray(array, count);
    ViewArray(array, count);
    
    int lastItem = array[count - 1];
    int countDuplicate = 0;
    for (int i = 0; i < count - 1; i++) { if (array[i] == lastItem) { countDuplicate++; } }
    
    int* newArray = new int[count - countDuplicate];
    int j = 0;
    for (int i = 0; i < count - 1; i++)
    {
        if (array[i] != lastItem)
        {
            newArray[j] = array[i];
            j++;
        }
    }
    newArray[count - countDuplicate - 1] = lastItem;
    
    cout << "\nЗадание 10: удалить все элементы, равные последнему" << endl;
    ViewArray(newArray, count - countDuplicate);
    delete[] newArray;
    delete[] array;
}

void ElevenTaskFirstLab()
{
    int count = 0;
    cout << "Введите кол-во элементов массива: ";
    cin >> count;
    int* array = new int[count];
    GetArray(array, count);
    ViewArray(array, count);
    
    int max = array[0];
    int maxCount = 0;
    for (int i = 1; i < count; i++)
    {
        if (max < array[i])
        {
            max = array[i];
            maxCount = i;
        }
    }
    
    int* newArray = new int[count-1];
    for (int i = 0; i < maxCount; i++)
    {
        newArray[i] = array[i];
    }
    for (int i = maxCount + 1; i < count; i++)
    {
        newArray[i - 1] = array[i];
    }
    
    cout << "\nЗадание 11: удалить максимальный элемент" << endl;
    ViewArray(newArray, count - 1);
    delete[] newArray;
    delete[] array;
}

void TwelveTaskFirstLab()
{
    int count = 0;
    cout << "Введите кол-во элементов массива: ";
    cin >> count;
    int* array = new int[count];
    GetArray(array, count);
    ViewArray(array, count);
    
    int min = array[0];
    int minCount = 0;
    for (int i = 1; i < count; i++)
    {
        if (min > array[i])
        {
            min = array[i];
            minCount = i;
        }
    }
    array[minCount] = 0;
    
    cout << "\nЗадание 12: найти минимальный элемент и вставит на его место 0" << endl;
    ViewArray(array, count);
    delete[] array;
}

void FirstLaboratoryMenu()
{
    char menu = 'n';
    while (menu != 'e' || menu != 'E')
    {
        system("clear");
        cout << "Лабораторная работа №1\nОбработка массива" << endl;
        cout << "1) Поменять местам первый и последний элементы стека" << endl;
        cout << "2) Развернуть стек, т.е. сделать \"дно\" стека вершиной, а вершину - \"дном\"" << endl;
        cout << "3) Удалить элемент, находящийся в середине стека" << endl;
        cout << "4) Удалить каждый второй элемент стека" << endl;
        cout << "5) Вставить символ ‘*’ в середину стека" << endl;
        cout << "6) Найти минимальный элемент и вставить после него 0" << endl;
        cout << "7) Найти максимальный элемент и вставить после него 0" << endl;
        cout << "8) Удалить минимальный элемент" << endl;
        cout << "9) Удалить все элементы, равные первому" << endl;
        cout << "Q) Удалить все элементы, равные последнему" << endl;
        cout << "A) Удалить максимальный элемент" << endl;
        cout << "Z) Найти минимальный элемент и вставит на его место 0" << endl;
        cout << "E) Выход в главное меню" << endl;
        cin >> menu;
        system("clear");
        cout << endl << endl;
        switch (menu)
        {
            case '1': FirstTaskFirstLab(); break;
            case '2': SecondTaskFirstLab(); break;
            case '3': ThirdTaskFirstLab(); break;
            case '4': FourTaskFirstLab(); break;
            case '5': FiveTaskFirstLab(); break;
            case '6': SixTaskFirstLab(); break;
            case '7': SevenTaskFirstLab(); break;
            case '8': EightTaskFirstLab(); break;
            case '9': NineTaskFirstLab(); break;
            case 'Q': TenTaskFirstLab(); break;
            case 'A': ElevenTaskFirstLab(); break;
            case 'Z': TwelveTaskFirstLab(); break;
        }
    }
}
