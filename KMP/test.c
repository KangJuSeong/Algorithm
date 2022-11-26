/*  
  automata.c --  
    오토마타를 사용한 문자열 검색  
    검색대상 문자열에서 하나의 문자를 검색해 나갈때 마다 미리 만들어진 
    오토마타 테이블의 값을 참조하면서 비교  

  modified by Han donghun . 1997.1.16. 
*/ 

#include <stdio.h> 
#include <string.h> 

#define MAX_LEN  50 
#define NSIGMA  2 

char DELTA[6][NSIGMA]; 
char table[NSIGMA] = {'0','1'}; 

/* p[] 가 s[]의 뒷부분과 일치하면 1을 되돌리고, 아니면 0을 되돌린다.*/ 
int is_suffix(char p[], char s[]) { 
  int pl, sl; 
  int i, j; 

  pl = strlen(p); 
  sl = strlen(s); 
  if (pl > sl) return 0; 
  for (i = pl - 1, j = sl - 1; i >= 0; i--, j--) 
    if (p[i] != s[j]) return 0; 
  return 1; 
} 

/* 문자열 s[]의 처음부터 k개를 t[]로 복사함 */ 
char *substr(char s[], char t[], int k) { 
  int i; 

  for (i = 0; i < k; i++) 
    t[i] = s[i]; 
  t[i] = '\0'; 
  return t; 
} 

/* 전이 함수를 만드는 함수 */ 
void make_transition(char p[], char delta[][NSIGMA]) { 
  int q;  /* 상태 */ 
  int i, j; 
  int pl; /* p 문자열의 길이 */ 
  char pq[MAX_LEN], pj[MAX_LEN]; /* 부분 문자열을 저장할 임시공간 */ 

  pl = strlen(p); 
  for (q = 0; q < pl; q++)  
    for (i = 0; i < NSIGMA; i++) { 
      substr(p, pq, q);   /* p[0..q]a 를 만드는 과정 */ 
      pq[j = strlen(pq)] = table[i]; 
      pq[++j] = '\0'; 
      /* 최대의 접미어가 되는 j+1을 찾음 */ 
      while (!is_suffix(substr(p, pj, j), pq)) j--; 
      delta[q][i] = j; /* 전이 함수 설정 */ 
    } 
} 

int automata_strsch(char s[], char p[]) { 
  int pl, sl; 
  int i; 
  int q = 0; 

  pl = strlen(p); 
  sl = strlen(s); 
  make_transition(p, DELTA); 
  for (i = 0; i < sl; i++) { 
    q = DELTA[q][s[i] - '0']; 
    if (q == pl) return i-pl+1; 
  } 
  return -1; 
} 

void main() { 
  char *search = "110010"; 
  char *src = "11000110011010110010"; 
  int index; 

  index = automata_strsch(src, search); 
  printf("string : %s\nsearch string : %s\nfind index = %d\n",  
            src, search, index); 
  printf("answer string : %s\n", src + index); 
} 
