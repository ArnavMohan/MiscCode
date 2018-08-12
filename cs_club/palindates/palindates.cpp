#include <fstream>
#include <iostream>
#include <string>

using namespace std;

struct Day {
  int d;
  int m;
  int y;
};
int last[] = {0,31,28,31,30,31,30,31,31,30,31,30,31};

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

bool isPalindrome(string s) {
  int len = s.length();
  int maxcmp = len/2;
  for (int i = 0 ; i < maxcmp; i++)
    if (s[i] != s[len-1-i])
      return false;
  return true;
}

bool isPalindate(const Day& d) {
  string s = to_string(d.m) + to_string(d.d) + to_string(d.y);
  return isPalindrome(s);
}

int main() {

  Day d;
  char sl;
  ifstream ifp;
  ifp.open("palindates.dat");
  while (true) {
    ifp >> d.m >> sl >> d.d >> sl >> d.y;
    if (!d.m && !d.d && !d.y)
      break;
    while (true) {
      if (isPalindate(d)) {
        cout << day2str(d) << endl;
        break;
      }
      nextDay(&d);
    }
  }

  ifp.close();
  return 0;
}
