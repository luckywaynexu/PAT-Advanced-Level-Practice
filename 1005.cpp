/*
Given a non-negative integer N, your task is to compute the sum of all the digits of N, and output every digit of the sum in English.

Input Specification:
Each input file contains one test case. Each case occupies one line which contains an N (≤10
​100
​​ ).

Output Specification:
For each test case, output in one line the digits of the sum in English words. There must be one space between two consecutive words, but no extra space at the end of a line.

Sample Input:
12345
Sample Output:
one five
*/
#include<sstream>
# include <iostream>
using namespace std;
string char2string(char num)
{
	switch (num)
	{
	case '0':
        return "zero";
    case '1':
		return "one";
	case '2':
		return "two";
	case '3':
		return "three";
	case '4':
		return "four";
	case '5':
		return "five";
	case '6':
		return "six";
	case '7':
		return "seven";
	case '8':
		return "eight";
	case '9':
		return "nine";
	default:
		return 0;
	}
}
int main()
{
	char N[10^100];
	cin >> N;
	int sum = 0;
	string Nstr = N;
	for (int i = 0; i<Nstr.length(); i++)
	{
		sum += Nstr[i]-'0';
	}
	//cout << sum;
	string str;
	str = std::to_string(sum);
	for (int i = 0; i < str.length(); i++)
	{
		if (i==str.length()-1)
        {
            cout<<char2string(str[i]);
        }
        else
            cout <<char2string(str[i]) << " ";
	}
    
	return 0;
}
