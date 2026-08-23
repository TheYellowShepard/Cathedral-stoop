#include <iostream>

int main() {
    double tempf;
    double tempc;
    int x;
    std::cout << "What would you like to convert? \n";
    std::cout << "1. F->C   2. C->F \n";
    std::cin >> x;
    if (x == 1) {
        std::cout << "Enter temperature in Fahrenheit: \n";
        std::cin >> tempf;
        tempc = (tempf - 32)/1.8;
        std::cout << "The current temperature in Celsius: " << tempc << "\n";
    }
    else if (x == 2)
    {
        std::cout << "Enter temperature in Celcius: \n";
        std::cin >> tempc;
        tempf = (tempc * 1.8) + 32;
        std::cout << "The current temperature in Fahrenheit: " << tempf << "\n";
    }
    
}