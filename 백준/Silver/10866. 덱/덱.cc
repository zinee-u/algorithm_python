#include <stdio.h>
#include <iostream>

using namespace std;

#define MAX (10000+500)
#define OFFSET (MAX/2)

int N;
int deq[MAX*2];
int front, back;

int myStrCmp(const char *a, const char *b)
{
    while(*a && *a==*b)
    {
        ++a;
        ++b;
    }
    return *a-*b;
}

int main(void)
{
    cin >> N;
    // cout << N << endl;
    front = back = OFFSET;

    char cmd[100];

    for(int i=0;i<N;i++)
    {
        cin >> cmd;
        // cout << "cmd = " << cmd << endl;
        // cout << deq << endl;
        if(!myStrCmp(cmd,"push_back"))
        {
            int val;
            cin >> val;
            deq[back++]=val;
        }
        else if(!myStrCmp(cmd,"push_front"))
        {
            int val;
            cin >> val;
            deq[--front] = val;
        }
        else if(!myStrCmp(cmd,"pop_back"))
        {
            int val = (front == back) ? -1 : deq[--back];
            cout << val << endl;
        }
        else if(!myStrCmp(cmd,"pop_front"))
        {
            int val = (front == back) ? -1 : deq[front++];
            cout << val << endl;
        }
        else if(!myStrCmp(cmd,"empty"))
        {
            int val = (front == back) ? 1:0;
            cout << val << endl;
        }
        else if(!myStrCmp(cmd, "front"))
        {
            int val = (front == back) ? -1 : deq[front];
            cout << val << endl;
        }
        else if(!myStrCmp(cmd, "back"))
        {
            int val = (front == back) ? -1 : deq[back-1];
            cout << val << endl;
        }
        else if(!myStrCmp(cmd, "size"))
        {
            int val = (back-front);
            cout << val << endl;
        }
    }
    return 0;
}