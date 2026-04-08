#include <bits/stdc++.h>
using namespace std;

int get2ndshort(vector<int> vec){ 
        int min = INT_MAX;
        int min2;
        for(int itr : vec){
            if(itr<min){
                min2 = min;
                min = itr;
            } 
            else if(itr>min && itr<min2) min2 = itr;
        }
        return min2;
    }


int main() {

    vector<int> vec = {1,3,5,54,4,34,6,88,565,7};


    cout<<get2ndshort(vec)<<endl;
    return 0;
}