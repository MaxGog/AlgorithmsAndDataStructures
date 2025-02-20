//
//  Header.h
//  Algorithms&DataStructures
//
//  Created by Максим Гоглов on 20.02.2025.
//

#ifndef Header_h
#define Header_h

#include <stdio.h>
#include <iostream>
#include <string>
#include <map>
#include <fstream>

using namespace std;

class NodeWithMark {
public:
    string data;
    NodeWithMark* next;
    bool mark;
    NodeWithMark(const string& data) : data(data), next(nullptr), mark(false) {}
};

class Node2 {
public:
    map<string, string> data;
    Node2* next;
    bool mark;

    Node2(const string& first, const string& second) : next(nullptr), mark(false) {
        data["first"] = first;
        data["second"] = second;
    }
};

struct Node;
struct CNode;


void ViewArray(int array[], int count);
void GetArray(int* array[], int count);

void FirstLaboratoryMenu();

void FirstTaskFirstLab();
void SecondTaskFirstLab();
void ThirdTaskFirstLab();
void FourTaskFirstLab();
void FiveTaskFirstLab();
void SixTaskFirstLab();
void SevenTaskFirstLab();
void EightTaskFirstLab();
void NineTaskFirstLab();
void TenTaskFirstLab();
void ElevenTaskFirstLab();
void TwelveTaskFirstLab();

void SecondLaboratoryMenu();

void FirstIndividualSecondLab();
void SecondIndividualSecondLab();
void ThirdIndividualSecondLab();
void FourthIndividualSecondLab();
void FivethIndividualSecondLab();
void SixthIndividualSecondLab();

#endif /* Header_h */
