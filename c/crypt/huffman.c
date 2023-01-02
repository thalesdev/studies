/*
 * Algoritimo de huffman by thales.
 */

/* 
 * File:   main.c
 * Author: Thales
 *
 * Created on 11 de Novembro de 2017, 00:07
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>


typedef struct Node{
    char *node;
    int weight;
    struct Node *left;
    struct Node *right;
} NODE;
typedef struct Three{
    NODE *root;
    int size;
} THREE;
typedef struct NodeList{
    int size;
    int priorityQueue;
    NODE *itens;
    void *append;
    void *remove;
    void *pop;
    void *pull;
    void (*func_ptr)(int); 
} NODELIST;

// # ---------------------



//  # ---- Helpers --------


NODELIST *appendNodeList(NODELIST *list, NODE node){
    int size = list->size;
    NODE *temp = malloc(sizeof(NODE)*(size+1));
    for (int i=0; i<size; i++){
      temp[i] = list->itens[i];  
    };
    temp[size] = node;
    list->size = list->size+1;
    list->itens = temp;
    if(list->priorityQueue){
    	priorityNodeListQueue(list);
    };
    return list;
};
NODE *removeNodeList(NODELIST *list, int index){
    int size = list->size;
	if(index <= list->size && index >= 0){
            NODE *aux;
            aux = malloc((sizeof(NODE))*(list->size-1));
	        NODE aux_= list->itens[list->size-1];
	        list->itens[size-1] = list->itens[index];
            list->itens[index] = aux_;
	    for(int c=0; c<(list->size-1);c++){
	        aux[c]=list->itens[c];
	    }            
		NODE *item = malloc(sizeof(NODE));
		item->left =list->itens[size-1].left;
		item->right =list->itens[size-1].right;
		item->node =list->itens[size-1].node;
		item->weight = list->itens[size-1].weight;
		list->size=list->size-1;
		list->itens = aux;
    		priorityNodeListQueue(list);
		return item;
	};
	NODE *rtr;
	rtr->weight=-999;
	return rtr;
};
NODE *popNodeList(NODELIST *list){
  return removeNodeList(list, list->size);  
};
NODE *pullNodeList(NODELIST *list){
  return removeNodeList(list, 0);  
};
// BUBLE SORT POR HORA
void priorityNodeListQueue(NODELIST *list){
	
	NODE aux;
	for (int i=0; i<list->size;i++){
		for(int k=i+1; k<list->size; k++){
			if(list->itens[i].weight>list->itens[k].weight){
				aux = list->itens[k];
				list->itens[k] = list->itens[i];
				list->itens[i] = aux;
			};
		};
	};
};
void getThreadSimbolsList(NODE *root, char *value){
	if(root != NULL){
		NODE *right = root->right;
		NODE *left = root->left;
		if(isLeaf(*root) == 1){
			printf("Leaf[%c]: new code %s \n", root->node, value);
			return;
		}
		char *leftStr = malloc(sizeof(char)*(strlen(value)+1)); 
		strcpy(leftStr,"");
		strcat(leftStr, value);
		strcat(leftStr,"0");
		getThreadSimbolsList(left, leftStr);
		free(leftStr);
		char *rightStr = malloc(sizeof(char)*(strlen(value)+1)); 
		strcpy(rightStr,"");
		strcat(rightStr, value);
		strcat(rightStr,"1");
		getThreadSimbolsList(right,rightStr);
		free(rightStr);
    	//printf("weigth :%d,%d\n",right->weight, right->weight);
	}
};



// #------------- fim dos helpers -------------------
// #------ Builtins  -----------
// ARRUMAR OS POINTEIROS DE FUNCAO....
NODELIST *NewNodeList(){
	NODELIST *temp = malloc(sizeof(NODELIST));
	temp->priorityQueue = 1;
	temp->size = 0;
	temp->append = &appendNodeList;
        temp->remove = &removeNodeList;
        temp->pop = &popNodeList;
        temp->pull = &pullNodeList;
	return temp;
};

NODE *Node(int weigth){
	NODE *n = malloc(sizeof(NODE));
	n->node = NULL;
	n->weight = weigth;
	n->left = NULL;
	n->right = NULL;
	return n;	
};

NODE *Leaf(char *payload, int weigth ){
	NODE *n = Node(weigth);
	n->node = payload;
	return n;
};

NODE *CreateSubThree(NODE *first, NODE *second){
    int weight = (first->weight)+(second->weight);
    NODE *temp = Node(weight);
    temp->right = first;
    temp->left = second;
    return temp;
};

THREE *mThreeByNodeList(NODELIST *list){
	THREE *three = malloc(sizeof(THREE));
	int size;
	for(;;){
		if (list->size>1){		    
			NODE *node1 = removeNodeList(list,0);
			NODE *node2 = removeNodeList(list,0);
			NODE *newNode = CreateSubThree(node1,node2);
			appendNodeList(list,*newNode);
			size++;
		}
		else{
			three->size = size;
			three->root = &list->itens[0];
			return three;
		}
	};	
    //printf("%c\n", three.root.right->node);
	return three;
	
};


int isLeaf(NODE *p){
	if(p->node == NULL){
		// SE NAO FOR UMA FOLHA
		return 0;
	};
	return 1;	
};
// Gera nodelists pela incidencia de palavras em uma string
NODELIST *nodeListByIncidence(char *string, int size){
	char letters[size]; // vetor pra armazenar as letras j� verificadas.
    NODELIST *list = NewNodeList();
    int	lastadd=0;
	for(int i=0; i<size;i++){
		int k=0;
		for (int z=0;z<size;z++){
			if(letters[z] == string[i]){
					k=1;
					break;
			}	
		}
		if(k == 0){
			letters[lastadd] = string[i];
			int c=0;
			for(int t=0;t<size;t++){
				if(string[t] == string[i]){
					c++;
				}	
			}
			//printf("REPETICOES DA LETRA %c : %d\n", string[i], c);
			NODE *leaf = Leaf(string[i], c);
			appendNodeList(list, *leaf);
			lastadd+=1;	
		}else{
			break;
		}	
	}
	return list;
};




// #------------- fim dos builtins ------------







/*
 * Função principal
 */
int main(int argc, char** argv) {
	printf("\n\n Compactando a palavra Batata \n tamanho original : %d bits \n\n", (sizeof(char)*6)*8 ) ;
    NODELIST *p = nodeListByIncidence(&"Batata",6);
    printf("NodeList(%d):\n", p->size);
	for (int i=0; i<p->size; i++){
    	printf("Leaf[%c](%d) Weight: %d\n",  p->itens[i].node,i+1, p->itens[i].weight);
	}
    printf("\n\n");
    THREE *three = mThreeByNodeList(p);
    getThreadSimbolsList(three->root,"");
  	//printf("XD : %d\n",three.root.left->left);
    //NODE *root = mThreeByNodeList(p);
	//printf("%d\n", root->left->right->weight);
    ;
    
    
    return (0);
}