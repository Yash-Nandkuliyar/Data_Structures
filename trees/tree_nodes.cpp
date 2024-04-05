#include <bits/stdc++.h>
using namespace std;
struct Node
{
    int val;
    Node *left=NULL,*right=NULL;

};
void inorder(Node* root)
{
    if(root==NULL)return ;
    cout<<root->val<<" ";
    inorder(root->left);
    cout<<root->val<<" ";
    inorder(root->right);
    cout<<root->val<<" ";

}
int main()
{
    Node* root =new Node;
    root ->val=90;
    Node* node1=new Node;
    node1 ->val=5;
    Node* node2=new Node;
    node2 ->val =10;
    root->left=node1;
    root->right=node2;
    Node* node3=new Node;
    node3 ->val=11;
    Node* node4=new Node;
    node4 ->val =13;
    node1->left=node3;
    node1->right=node3;
    inorder(root);
}