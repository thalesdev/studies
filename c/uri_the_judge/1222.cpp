#include <cstdio>
#include <cmath>
#include <cstring>

int main () {
  int charsPerLine, linesPerPage, nWords;
  float nChars, nLines, nPages;
  char c;
  char word[70];

  while (scanf("%d %d %d", &nWords, &linesPerPage, &charsPerLine) != EOF) {

    nChars = 0;
    nLines = 1;

    while (nWords--) {
      scanf("%s", word);

      if (nChars > 0) nChars++;
      nChars += strlen(word);

      if (nChars == charsPerLine) {
        nChars = 0;
        if (nWords > 0)
          nLines++;
      }

      if (nChars > charsPerLine) {
        nChars = strlen(word);
        nLines++;
      }
    }

    nPages = std::ceil(nLines/linesPerPage);

    printf("%d\n", (int)nPages);
  }

  return 0;
}