#include "closestpair.h"
#include <algorithm>
#include <cstdlib>
#include <sys/time.h>  // used to seed srand for extra credit
using namespace std;

  Outcome brute(const vector<Point>& data) {
    Outcome best(data[0], data[1], distSquared(data[0],data[1]));
    for (unsigned int j=1; j < data.size(); j++) {
      for (unsigned int k=0; k < j; k++) {
        long long temp = distSquared(data[j], data[k]);
        if (temp < best.dsq) {
          best = Outcome(data[j], data[k], temp);
        }
      }
    }
    return best;
  }
  
  Outcome recursiveclosest(const vector<Point>& X, int xbegin, int xend, const vector<Point>& Y) {
    if ((xend - xbegin + 1) <= 100) {
      vector<Point> temp(X.begin() + xbegin, X.begin() + xend + 1);
      return brute(temp);
    }

    // find index of last element in Pl
    int middleindex = ((xend - xbegin + 1) % 2 == 1) ? (xbegin + ((xend - xbegin + 1) / 2)) : (xbegin + ((xend - xbegin + 1) / 2) - 1);

    vector<Point> Yl, Yr;

    for (unsigned int i = 0; i < Y.size(); i++) {
      if (Y[i].x <= X[middleindex].x) {
        Yl.push_back(Y[i]);
      } else {
        Yr.push_back(Y[i]);
      }
    }

    Outcome left = recursiveclosest(X, xbegin, middleindex, Yl);
    Outcome right = recursiveclosest(X, middleindex + 1, xend, Yr);
    
    Outcome delta;

    if (min(left.dsq, right.dsq) == left.dsq) {
      delta = left;
    } else {
      delta = right;
    }

    vector<Point> Yprime;

    for (unsigned int i = 0; i < Y.size(); i++) {
      long long xdistsq = pow((abs(Y[i].x - X[middleindex].x)), 2.0);
      if (xdistsq <= delta.dsq) {
        Yprime.push_back(Y[i]);
      }
    }

    Outcome deltaprime = delta;
    for (unsigned int i = 0; i < Yprime.size(); i++) {
      for (int j = 1; j < 8; j++) {
        if ((i + j) > (Yprime.size() - 1)) break;
        if (distSquared(Yprime[i], Yprime[i + j]) < deltaprime.dsq) {
          deltaprime = Outcome(Yprime[i], Yprime[i + j], distSquared(Yprime[i], Yprime[i + j]));
        }
      }
    }

    return deltaprime;
  }
  
  Outcome efficient(const vector<Point>& data) {
    vector<Point> X(data);
    vector<Point> Y(data);
    sort(X.begin(), X.end(), compareByX);
    sort(Y.begin(), Y.end(), compareByY);
    
    return recursiveclosest(X, 0, X.size() - 1, Y);
  }

  Outcome extra(const vector<Point>& data) {
    return Outcome();
  }
