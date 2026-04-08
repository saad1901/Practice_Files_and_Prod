#include <bits/stdc++.h>
using namespace std;

class Vehicle{
    // public:
    int id;
    string name;
    bool happy;

    public:
    void setter(int idx, string namex, bool happyx){
        id = idx;
        name = namex;
        happy = happyx;
    }

    pair<string, bool> getter(){
        return {name, happy};       
    }
};

class Bike : public Vehicle{

};


int main(){
    Vehicle car;
    car.setter(1, "Ford", false);
    pair<string, bool> pr = car.getter();
    cout<<pr.first<<" "<<pr.second<<endl;

    Bike rf;
    rf.setter(1, "BMW", true);

    pr = rf.getter();
    cout<<pr.first<<" "<<pr.second<<endl;
}

