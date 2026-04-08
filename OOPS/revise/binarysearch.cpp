#include <bits/stdc++.h>
using namespace std;

int binary(vector<int> vec, int num){
    int low = 0, high = vec.size()-1;
    while(low<high){
        int mid = (low+high)/2;
        if(vec[mid] == num) return mid;
        else if(vec[mid] > num) high = mid;
        else low = mid+1;
    }
    return -1;
}


int main() {

    vector<int> vec {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15};
    cout<<binary(vec, 10)<<endl;
    cout<<binary(vec, 12)<<endl;
    cout<<binary(vec, 1)<<endl;
    cout<<binary(vec, 0)<<endl;
    cout<<binary(vec, 20)<<endl;
    
    return 0;
}