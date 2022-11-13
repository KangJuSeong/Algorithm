#include <iostream>
using namespace std;

struct node {
	int data;
	struct node* left;
	struct node* right;
};

void insert(struct node** root, int data);
void preOrder(struct node* root);
void inOrder(struct node* root);
void postOrder(struct node* root);
int size(struct node* root);
int height(struct node* root);
int sumOfWeight(struct node* root);
int maxPathWeight(struct node* root);
void mirror(struct node** root);
void destruct(struct node** root);


int main() {
	int numTestCases;
	
	cin >> numTestCases;
	while (numTestCases --) {
		int num, i;
		struct node* root = NULL;
		cin >> num;
		for (int i=0; i<num; i++) {
			int data;
			cin >> data;
			insert(&root, data);
		}
		cout << size(root) << endl;
		cout << height(root)-1 << endl;
		cout << sumOfWeight(root) << endl;
		cout << maxPathWeight(root) << endl;
		mirror(&root); 
		preOrder(root); cout << endl;
		inOrder(root); cout << endl;
		postOrder(root); cout << endl;
		destruct(&root);
		if (root == NULL) cout << "0" << endl;
		else cout << "1" << endl;
	}
	return 0;
}

void insert(struct node** root, int data) {
	if (*root == NULL) {
		node *_new = new node();
		_new -> data = data;
		*root = _new;
	} else if ((*root) -> data > data){
		insert(&(*root)->left, data);
	} else {
		insert(&(*root)->right, data);
	}
}

void inOrder(struct node* root) {
	if (root) {
		inOrder(root->left);
		cout << root->data << " ";
		inOrder(root->right);
	}
}

void postOrder(struct node* root) {
	if (root) {
		postOrder(root->left);
		postOrder(root->right);
		cout << root->data << " ";
	}
}

void preOrder(struct node* root) {
	if (root) {
		cout << root->data << " ";
		preOrder(root->left);
		preOrder(root->right);
	}
}

int size(struct node* root) {
	if (root == NULL) return 0;
	return 1 + size(root->left) + size(root->right);
}

int height(struct node* root) {
	if (root == NULL) return 0;
	return 1 + max(height(root->left), height(root->right));
}

int sumOfWeight(struct node* root) {
	if (root == NULL) return 0;
	return root->data + sumOfWeight(root->left) + sumOfWeight(root->right);
}

int maxPathWeight(struct node* root) {
	if (root == NULL) return 0;
	return root->data + max(maxPathWeight(root->left), maxPathWeight(root->right));
}

void mirror(struct node** root) {
	if (*root == NULL) return;
	mirror(&(*root)->left);
	mirror(&(*root)->right);
	swap((*root)->left, (*root)->right);
}

void destruct(struct node** root) {
	if ((*root)->left != NULL) {
		destruct(&(*root)->left);
	} 
	if ((*root)->right != NULL){
		destruct(&(*root)->right);
	}
	if (*root != NULL) {
		*root = NULL;
		delete *root;
	}
}
