#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

// Globos
int main(void) {
  unsigned int N;
  cin >> N;

  vector<unsigned> globos = vector<unsigned>();

  map<unsigned, set<unsigned>> novisit;
  set<unsigned> novisitgen;

  for (unsigned i = 0; i < N; ++i) {
    set<unsigned> nvaux;
    novisit[i] = nvaux;
  }

  for (unsigned i = 0; i < N; ++i) {
    unsigned w;
    cin >> w;
    novisitgen.insert(i);
    novisit[w].insert(i);
    globos.push_back(w);
  };

  unsigned sum = 0;
  unsigned i = 0;
  unsigned h = globos[i];

  for (;;) {
    novisit[h].erase(i); // Pintamos como visitado
    novisitgen.erase(i); // Pintamos como visitado

    --h;                 // Pasamos a romper globos una altura mas abajo
    auto iaux = novisit[h].lower_bound(i);
    if (iaux != novisit[h].end()) {
      i = *iaux; // Proximo en esta altura
    } else {
      iaux = novisitgen.begin(); // Proximo indice
      ++sum;
      if (iaux != novisitgen.end()) {
        i = *iaux;
        h = globos[i];
      } else {
        break;
      }
    }
  }

  cout << sum << "\n";
}
