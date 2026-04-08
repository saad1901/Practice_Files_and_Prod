#include <bits/stdc++.h>
using namespace std;

class Vehicle{
    // public:
    int id;
    string name;
    public:
    string horn = "Pop pop";
    // Vehicle(){}
    // Vehicle(int id, string name){
    //     this->id = id;
    //     this->name = name;
    // }
    void test(){
        cout<<"Vehicle class function"<<endl;
    }

};

class Truck : public Vehicle{
    public:
    string horn = "Peep Peep";

    // truck(){}
};

int main(){

    // Vehicle car(1, "Ford");
    // car.name = "Ford";
    // cout<<car.id<<" "<<car.name<<endl;

    Truck mytruck;
    cout<<"TRUCK HORN : "<<mytruck.horn;

    return 0;
}