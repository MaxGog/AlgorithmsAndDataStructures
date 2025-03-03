//
//  thirdlaboratory.cpp
//  Algorithms&DataStructures
//
//  Created by Максим Гоглов on 03.03.2025.
//

#include "thirdlaboratory.h"

// Структура узла дерева
struct NodeThirdLab {
    double data;
    NodeThirdLab* left;
    NodeThirdLab* right;
};

// Класс бинарного дерева
class BinaryTree {
private:
    NodeThirdLab* root;

    // Рекурсивная копия поддерева
    NodeThirdLab* copyTree(NodeThirdLab* node) {
        if (node == nullptr) return nullptr;
        NodeThirdLab* newNode = new NodeThirdLab();
        newNode->data = node->data;
        newNode->left = copyTree(node->left);
        newNode->right = copyTree(node->right);
        return newNode;
    }

    // Рекурсивная проверка равенства деревьев
    bool equalTrees(NodeThirdLab* t1, NodeThirdLab* t2) {
        if (t1 == nullptr && t2 == nullptr) return true;
        if (t1 == nullptr || t2 == nullptr) return false;
        return (t1->data == t2->data &&
                equalTrees(t1->left, t2->left) &&
                equalTrees(t1->right, t2->right));
    }

    // Рекурсивный подсчет количества вхождений значения
    int countOccurrences(NodeThirdLab* node, double value) {
        if (node == nullptr) return 0;
        int count = (node->data == value ? 1 : 0);
        return count + countOccurrences(node->left, value) +
               countOccurrences(node->right, value);
    }

public:
    BinaryTree() : root(nullptr) {}

    ~BinaryTree() {
            if (root != nullptr) {
                deleteTree(root);
            }
        }

    // 1. Получение значения из левого листа и подсчет вхождений
    bool getLeftLeafValue(double& E) {
        NodeThirdLab* leftmost = root;
        while (leftmost && (leftmost->left || leftmost->right)) {
            if (leftmost->left) leftmost = leftmost->left;
            else leftmost = leftmost->right;
        }
        if (!leftmost) return false;
        E = leftmost->data;
        return true;
    }

    int countValueOccurrences(double value) {
        return countOccurrences(root, value);
    }

    // 2. Среднее арифметическое и добавление значения
    double calculateAverage() {
        if (!root) return 0.0;
        double sum = 0.0;
        int count = 0;
        queue<NodeThirdLab*> q;
        q.push(root);
        
        while (!q.empty()) {
            NodeThirdLab* node = q.front();
            q.pop();
            sum += node->data;
            count++;
            
            if (node->left) q.push(node->left);
            if (node->right) q.push(node->right);
        }
        return sum / count;
    }

    void addNode(double value) {
        NodeThirdLab* newNode = new NodeThirdLab();
        newNode->data = value;
        newNode->left = nullptr;
        newNode->right = nullptr;

        if (!root) {
            root = newNode;
            return;
        }

        queue<NodeThirdLab*> q;
        q.push(root);

        while (!q.empty()) {
            NodeThirdLab* current = q.front();
            q.pop();

            if (!current->left) {
                current->left = newNode;
                break;
            } else if (!current->right) {
                current->right = newNode;
                break;
            }

            if (current->left) q.push(current->left);
            if (current->right) q.push(current->right);
        }
    }

    // 3. Создание дерева из отрицательных значений
    BinaryTree* createNegativeTree() {
        BinaryTree* newTree = new BinaryTree();
        queue<NodeThirdLab*> q;
        q.push(root);

        while (!q.empty()) {
            NodeThirdLab* node = q.front();
            q.pop();

            if (node->data < 0) {
                newTree->addNode(node->data);
            }

            if (node->left) q.push(node->left);
            if (node->right) q.push(node->right);
        }
        return newTree;
    }

    // 4. Поиск минимума и печать листьев
    double findMin() {
        if (!root) return 0.0;
        double minVal = root->data;
        queue<NodeThirdLab*> q;
        q.push(root);

        while (!q.empty()) {
            NodeThirdLab* node = q.front();
            q.pop();

            if (node->left) {
                q.push(node->left);
                if (node->left->data < minVal) minVal = node->left->data;
            }
            if (node->right) {
                q.push(node->right);
                if (node->right->data < minVal) minVal = node->right->data;
            }
        }
        return minVal;
    }

    void printLeafNodes() {
        if (!root) return;
        queue<NodeThirdLab*> q;
        q.push(root);

        cout << "Листовые узлы: ";
        while (!q.empty()) {
            NodeThirdLab* node = q.front();
            q.pop();

            if (!node->left && !node->right) {
                cout << node->data << " ";
            }

            if (node->left) q.push(node->left);
            if (node->right) q.push(node->right);
        }
        cout << endl;
    }

    // 5. Проверка существования значения и добавление
    bool containsValue(double value) {
        queue<NodeThirdLab*> q;
        q.push(root);

        while (!q.empty()) {
            NodeThirdLab* node = q.front();
            q.pop();

            if (node->data == value) return true;

            if (node->left) q.push(node->left);
            if (node->right) q.push(node->right);
        }
        return false;
    }

    void insertValue(double value) {
        if (!containsValue(value)) {
            addNode(value);
        }
    }

    // 6. Поиск длины пути и максимальной глубины
    int findPathLength(double E) {
        if (!root) return -1;
        queue<pair<NodeThirdLab*, int>> q;
        q.push({root, 0});

        while (!q.empty()) {
            auto nodePair = q.front();
            NodeThirdLab* node = nodePair.first;
            int depth = nodePair.second;
            q.pop();

            if (node->data == E) return depth;

            if (node->left) q.push({node->left, depth + 1});
            if (node->right) q.push({node->right, depth + 1});
        }
        return -1;
    }

    int getMaxDepth() {
        if (!root) return 0;
        queue<pair<NodeThirdLab*, int>> q;
        q.push({root, 1});
        int maxDepth = 0;

        while (!q.empty()) {
            auto nodePair = q.front();
            NodeThirdLab* node = nodePair.first;
            int depth = nodePair.second;
            maxDepth = max(maxDepth, depth);
            q.pop();

            if (node->left) q.push({node->left, depth + 1});
            if (node->right) q.push({node->right, depth + 1});
        }
        return maxDepth;
    }

    // 7. Копирование дерева
    BinaryTree* copy() {
        BinaryTree* newTree = new BinaryTree();
        newTree->root = copyTree(root);
        return newTree;
    }

    // 8. Проверка равенства деревьев
    bool equals(BinaryTree& other) {
        return equalTrees(root, other.root);
    }

    // 9. Определение типа узла и печать атрибутов
    void printNodeAttributes() {
        if (!root) return;
        queue<NodeThirdLab*> q;
        q.push(root);
        cout << "Атрибуты узлов:" << endl;
        
        // Используем std::string вместо char для русских букв
        string type;
        while (!q.empty()) {
            NodeThirdLab* node = q.front();
            q.pop();
            
            // Присваиваем строку вместо символа
            if (node->left || node->right) {
                type = "П"; // промежуточный узел
                if (node == root) type = "К"; // корень
            } else {
                type = "Л"; // лист
            }
            
            cout << "Значение: " << node->data << ", Тип: " << type << endl;
            
            if (node->left) q.push(node->left);
            if (node->right) q.push(node->right);
        }
    }

    // 10. Поиск минимума листьев и добавление значения
    double findMinLeafValue() {
        if (!root) return 0.0;
        queue<NodeThirdLab*> q;
        q.push(root);
        double minVal = numeric_limits<double>::max();

        while (!q.empty()) {
            NodeThirdLab* node = q.front();
            q.pop();

            if (!node->left && !node->right) {
                minVal = min(minVal, node->data);
            }

            if (node->left) q.push(node->left);
            if (node->right) q.push(node->right);
        }
        return minVal;
    }

    // 11. Подсчет суммы значений при наличии элемента
    double sumValues(double value) {
        if (!containsValue(value)) return 0.0;
        
        double sum = 0.0;
        int count = countOccurrences(root, value);
        queue<NodeThirdLab*> q;
        q.push(root);

        while (!q.empty()) {
            NodeThirdLab* node = q.front();
            q.pop();

            if (node->data == value) {
                sum += node->data;
            }

            if (node->left) q.push(node->left);
            if (node->right) q.push(node->right);
        }
        return sum;
    }

    // 12. Печать уникальных и часто встречающихся значений
    void printUniqueAndMostFrequent() {
        map<double, int> frequency;
        queue<NodeThirdLab*> q;
        q.push(root);

        while (!q.empty()) {
            NodeThirdLab* node = q.front();
            q.pop();

            frequency[node->data]++;

            if (node->left) q.push(node->left);
            if (node->right) q.push(node->right);
        }

        bool foundUnique = false;
        double maxFreq = 0;
        double mostFrequent;

        cout << "Уникальные значения: ";
        for (auto& pair : frequency) {
            if (pair.second == 1) {
                cout << pair.first << " ";
                foundUnique = true;
            } else if (pair.second > maxFreq) {
                maxFreq = pair.second;
                mostFrequent = pair.first;
            }
        }
        if (!foundUnique) cout << "нет";
        cout << endl;

        cout << "Наиболее частое значение: ";
        if (maxFreq > 0) {
            cout << mostFrequent << " (" << maxFreq << " раз)" << endl;
        } else {
            cout << "нет" << endl;
        }
    }
    
    void deleteTree(NodeThirdLab* node) {
        if (node == nullptr) return;
        deleteTree(node->left);
        deleteTree(node->right);
        delete node;
    }
};

void ThirdLaboratoryMenu()
{
    BinaryTree tree;
    
    // Добавляем тестовые данные
    tree.addNode(5.0);
    tree.addNode(3.0);
    tree.addNode(7.0);
    tree.addNode(2.0);
    tree.addNode(4.0);
    tree.addNode(6.0);
    tree.addNode(8.0);
    
    
    tree.addNode(2.0); // дубликат для тестирования
    
    int choice;
    do {
        cout << "\nМеню третьей лабораторной работы:" << endl;
        cout << "1. Получить значение из левого листа и подсчитать вхождения" << endl;
        cout << "2. Вычислить среднее арифметическое и добавить значение" << endl;
        cout << "3. Создать дерево из отрицательных значений" << endl;
        cout << "4. Найти минимум и вывести листья" << endl;
        cout << "5. Проверить наличие значения и добавить его" << endl;
        cout << "6. Найти длину пути и максимальную глубину" << endl;
        cout << "7. Скопировать дерево" << endl;
        cout << "8. Проверить равенство деревьев" << endl;
        cout << "9. Вывести атрибуты узлов" << endl;
        cout << "10. Найти минимум листьев и добавить значение" << endl;
        cout << "11. Посчитать сумму значений при наличии элемента" << endl;
        cout << "12. Вывести уникальные и часто встречающиеся значения" << endl;
        cout << "0. Выход" << endl;
        cout << "Выберите пункт меню: ";
        cin >> choice;

        switch (choice) {
            case 1: {
                double E;
                if (tree.getLeftLeafValue(E)) {
                    cout << "Значение из левого листа: " << E << endl;
                    cout << "Количество вхождений: " << tree.countValueOccurrences(E) << endl;
                } else {
                    cout << "Дерево пусто" << endl;
                }
                break;
            }
            case 2: {
                double avg = tree.calculateAverage();
                cout << "Среднее арифметическое: " << avg << endl;
                tree.addNode(avg);
                break;
            }
            case 3: {
                BinaryTree* negativeTree = tree.createNegativeTree();
                cout << "Создано дерево из отрицательных значений" << endl;
                delete negativeTree;
                break;
            }
            case 4: {
                cout << "Минимальное значение: " << tree.findMin() << endl;
                tree.printLeafNodes();
                break;
            }
            case 5: {
                double value;
                cout << "Введите значение для поиска: ";
                cin >> value;
                if (tree.containsValue(value)) {
                    cout << "Значение найдено" << endl;
                } else {
                    tree.insertValue(value);
                    cout << "Значение добавлено" << endl;
                }
                break;
            }
            case 6: {
                double E;
                cout << "Введите значение для поиска пути: ";
                cin >> E;
                int pathLen = tree.findPathLength(E);
                cout << "Длина пути до значения " << E << ": " << pathLen << endl;
                cout << "Максимальная глубина дерева: " << tree.getMaxDepth() << endl;
                break;
            }
            case 7: {
                BinaryTree* copy = tree.copy();
                cout << "Создана копия дерева" << endl;
                delete copy;
                break;
            }
            case 8: {
                BinaryTree tree2;
                tree2.addNode(5.0);
                tree2.addNode(3.0);
                tree2.addNode(7.0);
                cout << "Равенство деревьев: " << (tree.equals(tree2) ? "да" : "нет") << endl;
                break;
            }
            case 9: {
                tree.printNodeAttributes();
                break;
            }
            case 10: {
                double minLeaf = tree.findMinLeafValue();
                cout << "Минимум листьев: " << minLeaf << endl;
                tree.addNode(minLeaf);
                break;
            }
            case 11: {
                double value;
                cout << "Введите значение для подсчета суммы: ";
                cin >> value;
                double sum = tree.sumValues(value);
                cout << "Сумма значений: " << sum << endl;
                break;
            }
            case 12: {
                tree.printUniqueAndMostFrequent();
                break;
            }
            case 0:
                cout << "Программа завершена" << endl;
                break;
            default:
                cout << "Неверный выбор" << endl;
        }
    } while (choice != 0);
}
