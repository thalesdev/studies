/* 
 * File:   main.cpp
 * Author: Thales
 *
 * Created on 22 de Maio de 2019, 09:24
 */

#include <cstdlib>
#include <iostream>
#include <bits/stdc++.h> 

using namespace std;

// A C++ program for Bellman-Ford's single source  
// shortest path algorithm. 

  
// a structure to represent a weighted edge in graph 
typedef struct edge 
{ 
    int src, dest, weight; 
} EDGE; 
  
// a structure to represent a connected, directed and  
// weighted graph 
typedef struct graph 
{ 
    int V, E; 
    struct Edge* edge;
    
} GRAPH; 
  
// Creates a graph with V vertices and E edges 
GRAPH* createGraph(int V, int E) 
{ 
    GRAPH graph = new GRAPH; 
    graph->V = V; 
    graph->E = E; 
    graph->edge = new EDGE[E]; 
    return graph; 
} 
  
// A utility function used to print the solution 
void printArr(int dist[], int n) 
{ 
    printf("Vertex   Distance from Source\n"); 
    for (int i = 0; i < n; ++i) 
        printf("%d \t\t %d\n", i, dist[i]); 
} 

void BellmanFord(GRAPH* graph, int src) 
{ 
    int V = graph->V; 
    int E = graph->E; 
    int dist[V]; 

    for (int i = 0; i < V; i++) 
        dist[i]   = INT_MAX; 
    dist[src] = 0; 
  

    for (int i = 1; i <= V-1; i++) 
    { 
        for (int j = 0; j < E; j++) 
        { 
            int u = graph->edge[j].src; 
            int v = graph->edge[j].dest; 
            int weight = graph->edge[j].weight; 
            if (dist[u] != INT_MAX && dist[u] + weight < dist[v]) 
                dist[v] = dist[u] + weight; 
        } 
    } 
    for (int i = 0; i < E; i++) 
    { 
        int u = graph->edge[i].src; 
        int v = graph->edge[i].dest; 
        int weight = graph->edge[i].weight; 
        if (dist[u] != INT_MAX && dist[u] + weight < dist[v]) 
            cout << "Graph contains negative weight cycle" << endl; 
    } 
  
    printArr(dist, V); 
  
    return; 
} 







int main(int argc, char** argv) {

    return 0;
}

