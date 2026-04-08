#include <bits/stdc++.h>
using namespace std;

void twoSum(vector<int> vec, int s){
    unordered_map<int, int> mpp;
    for(int i=0; i<vec.size(); i++){
        if(mpp.find(s-vec[i]) != mpp.end()) {
            cout<<"INDEX ("<<mpp[s-vec[i]]<<", "<<i<<")"<<endl;
            break;
        }
        mpp[vec[i]] = i;
    }


}


int main() {
    vector<int> v = {1,2,4,65,3,7,5};
    cout<<"ENTER VALUE OF T : ";
    int t = 0;
    cin>>t;
    twoSum(v,t);
    return 0;
}