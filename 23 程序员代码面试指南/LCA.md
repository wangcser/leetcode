# LCA
> Author ID.9276 

**问题关键词：**

- 

## 01 题目

## 题目描述

给定一棵二叉树以及这棵树上的两个节点 o1 和 o2，请找到 o1 和 o2 的最近公共祖先节点。 

## 输入描述:

```
第一行输入两个整数 n 和 root，n 表示二叉树的总节点个数，root 表示二叉树的根节点。以下 n 行每行三个整数 fa，lch，rch，表示 fa 的左儿子为 lch，右儿子为 rch。(如果 lch 为 0 则表示 fa 没有左儿子，rch同理)最后一行为节点 o1 和 o2。
```

## 输出描述:

```
输出一个整数表示答案。
```

示例1

## 输入

[复制](javascript:void(0);)

```
8 1
1 2 3
2 4 5
4 0 0
5 0 0
3 6 7
6 0 0
7 8 0
8 0 0
4 5
```

## 输出

[复制](javascript:void(0);)

```
2
```

## 备注:

```
1 \leq n \leq 5000001≤n≤5000001 \leq fa,lch,rch,root,o_1,o_2\leq n1≤fa,lch,rch,root,o1,o2≤no1 \ne o2o1=o2
```

## 02 分析



## 03 题解

### 基础：递归

```c++
#include <iostream>
#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <climits>

using namespace std;


class TreeNode {
public:
    int val;
    TreeNode *left;
    TreeNode *right;

    TreeNode(int num) : val(num), left(nullptr), right(nullptr) {}
};

void readTree(vector<TreeNode *> &nodes) {
    // read tree
    int n, r;
    map<int, TreeNode *> nodeMap;

    scanf("%d%d", &n, &r);
    //  create node and store it into dict
    for (int i = 1; i <= n; ++i) {
        TreeNode *newNode = new TreeNode(i);
        nodeMap[i] = newNode;
    }

    TreeNode *root = nodeMap[r];

    // build tree:use dict to link node
    int parent, lchild, rchild;
    for (int i = 0; i < n; ++i) {
        scanf("%d%d%d", &parent, &lchild, &rchild); // ctrl + z is EOF
        if (lchild != 0) {
            nodeMap[parent]->left = nodeMap[lchild];
        }
        if (rchild != 0) {
            nodeMap[parent]->right = nodeMap[rchild];
        }
    }

    int node1, node2;
    scanf("%d%d", &node1, &node2);

    nodes[0] = root;
    nodes[1] = nodeMap[node1];
    nodes[2] = nodeMap[node2];
}

class Solver {
public:
    TreeNode *solve(TreeNode *root, TreeNode *node1, TreeNode *node2) {
        if (root == nullptr || root == node1 || root == node2)
            return root;

        TreeNode *left = solve(root->left, node1, node2);
        TreeNode *right = solve(root->right, node1, node2);

        if (left && right)
            return root;

        return left != nullptr ? left : right;
    }

private:

};

int main() {
    vector<TreeNode *> nodes(3);
    readTree(nodes);

    // solver
    Solver solver;
    TreeNode *lcaNode = solver.solve(nodes[0], nodes[1], nodes[2]);
    if (lcaNode == nullptr) cout << 0;
    else cout << lcaNode->val;

    return 0;
}
```



### 优化：



## 04 总结

