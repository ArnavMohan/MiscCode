#include <fstream>
#include <iostream>
#include <string>

using namespace std;


int main() {

  ifstream ifp;
  ifp.open("codex.dat");
  int n;
  long long k;
  string s;
  ifp >> n;
  for (int i = 0; i <n; i++) {
    ifp >> s >> k;
    int j=0;
    int l = s.length();
    long long db;
    while (true) {
      db= (long long)1<<j;
      if ((long long)l*db >= k)
        break;
      j++;
    }
    long long prevl;
    while (j>0) {
      prevl = (long long)1<<(j-1);
      prevl *= l;
      if (k > prevl) {
        k = 2*prevl - k + 1;
      }
      j--;
    }
    cout << s[k-1] << endl;
  }

  return 0;
}
