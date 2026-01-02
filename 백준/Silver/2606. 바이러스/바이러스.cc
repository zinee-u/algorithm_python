#include <stdio.h>
#include <iostream>

using namespace std;

#define MAX (100+10)

int N, E;
int cnt = 0;
int arr[MAX][MAX]={{0,}};
bool visited[MAX] = {false, };

void input(void)
{
  cin >> N >> E;
  for(int i=0; i<E; ++i)
  {
    int n1, n2;
    cin >> n1 >> n2;
    arr[n1][n2] = 1;
    arr[n2][n1] = 1;
  }
}

void printArr(void)
{
  for(int r=1; r<=N; ++r)
  {
    for(int c=1; c<=N; ++c)
    {
      cout << arr[r][c] << " ";
    }
    cout << endl;
  }
}

void DFS(int node)
{
  visited[node] = true;
  for(int i=1; i<=N; ++i)
  {
    if(arr[node][i]==0 || visited[i] == true) continue;
    cnt++;
    DFS(i);
  }
}


int main()
{
  input();
  DFS(1);
  cout << cnt << endl;
  return 0;
}