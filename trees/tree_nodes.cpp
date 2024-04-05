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
    inorder(root->left);
    cout<<root->val<<" ";
    inorder(root->right);
    cout<<root->val<<" ";

}

int height(Node* root)
{
    if(root==NULL) return 0;
    int heightleft=height(root->left);
    int heightright=height(root->right);
    return max(heightleft,heightright)+1;
}
void invert(Node* root)
{
    if(root==NULL) ;
    invert(root->left);
    invert(root->right);
    swap(root->left,root->right);

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
    cout<<endl;
    cout<<height(root)-1;
    invert(root);
    inorder(root);
}