#include<bits/stdc++.h>
using namespace std;

class Cricketer {
public:
    int jersey_no;
    string country;
};

int main() {
    // Create a dynamic object named dhoni
    Cricketer* dhoni = new Cricketer;
    dhoni->jersey_no = 7;
    dhoni->country = "India";

    // Create another dynamic object named kohli
    Cricketer* kohli = new Cricketer;

    // Copy data from dhoni to kohli
    kohli->jersey_no = dhoni->jersey_no;
    kohli->country = dhoni->country;

    // Delete the dhoni object
    delete dhoni;

    // Print the jersey_no and country of kohli object
    cout << "Kohli's jersey number: " << kohli->jersey_no << endl;
    cout << "Kohli's country: " << kohli->country << endl;

    // Delete the kohli object
    delete kohli;

    return 0;
}
