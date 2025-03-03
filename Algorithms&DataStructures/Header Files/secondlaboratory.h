//
//  secondlaboratory.h
//  Algorithms&DataStructures
//
//  Created by Максим Гоглов on 03.03.2025.
//

#ifndef secondlaboratory_h
#define secondlaboratory_h

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



void SecondLaboratoryMenu();

void FirstIndividualSecondLab();
void SecondIndividualSecondLab();
void ThirdIndividualSecondLab();
void FourthIndividualSecondLab();
void FivethIndividualSecondLab();
void SixthIndividualSecondLab();


#endif /* secondlaboratory_h */
