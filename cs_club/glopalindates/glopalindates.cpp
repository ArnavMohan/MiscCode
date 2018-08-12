#include <fstream>
#include <iostream>
#include <string>
#include <map>

using namespace std;

struct Day {
  int d;
  int m;
  int y;
};
int last[] = {0,31,28,31,30,31,30,31,31,30,31,30,31};

typedef map <int,string> Romans;
Romans rom;

bool isLeap(int y){
  if (y%4)
    return false;
  if (!(y%100) && (y%400))
    return false;
  return true;
}

void nextDay(Day *day) {
  int lom = last[day->m];
  if (day->m == 2 && isLeap(day->y))
    lom++;
  if (day->d == lom){
    day->d = 1;
    if (day->m == 12) {
      day->m = 1;
      day->y++;
    } else
      day->m++;
  } else
    day->d++;
  return;
  
}

string day2str(const Day& day){
  return to_string(day.m) + '/' + to_string(day.d) + '/' + to_string(day.y);
}


string to_roman (int n) {
  string s = "";
  
  for (Romans::reverse_iterator it = rom.rbegin(); it != rom.rend(); it++) {
    while (n >= it->first) {
      s.append(it->second);
      n -= it->first;
    }
  }
  return s;
}

string day2rom(const Day& day){
  return to_roman(day.m) + '/' + to_roman(day.d) + '/' + to_roman(day.y);
}

bool isPalindrome(string s) {
  int len = s.length();
  int maxcmp = len/2;
  for (int i = 0 ; i < maxcmp; i++)
    if (s[i] != s[len-1-i])
      return false;
  return true;
}

bool isRompalindate(const Day& d) {
  string s = to_roman(d.m) + to_roman(d.d) + to_roman(d.y);
  return isPalindrome(s);
}

bool isPalindate(const Day& d) {
  string s = to_string(d.m) + to_string(d.d) + to_string(d.y);
  return isPalindrome(s);
}

int main() {

  rom[1] = "I";
  rom[4] = "IV";
  rom[5] = "V";
  rom[9] = "IX";
  rom[10] = "X";
  rom[40] = "XL";
  rom[50] = "L";
  rom[90] = "XC";
  rom[100] = "C";
  rom[400] = "CD";
  rom[500] = "D";
  rom[900] = "CM";
  rom[1000] = "M";

  Day d = {1,1,1};

  while (!(d.m==12 && d.d==31 && d.y==4999)) {
    if (isRompalindate(d) && isPalindate(d)) {
      cout << day2str(d) << ' ' << day2rom(d) << endl;
    }
    nextDay(&d);
  }

  return 0;
}
