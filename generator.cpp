#include <bits/stdc++.h>
#define VanLoi ""
#define gb(i, j) ((i >> j) & 1)
 
using namespace std;
 
const int N = (int)1e5 + 5, MOD = (int)1e9 + 7, mod = (int)1e9 + 20041203;
 
int n, m, k;

string typeNuc = "ACGTRYSWKMBDHVN-";

struct pii {
    string name = "";
    string nuc = "";
} a[N];

map <string, int> mp;

int getRan(int mi, int ma) {
    return mi + rand() % (ma - mi + 1);
}

void do_cmd(string s) {
    cout << s << "\n";
    system(s.c_str());
}

void do_cmd(char* s) {
    system(s);
}

void printFasta(int val) {
    ofstream out("example.fasta");
    int mi = 1;
    if (val == n + k) mi = 0;
    for (int i = mi; i <= val; i++) {
        out << ">" << a[i].name << '\n';
        out << a[i].nuc << '\n';
    }
    out.close();
}

void printVcf() {
    do_cmd("./faToVcf example.fasta example.vcf");
}

void printTreeFile() {
    do_cmd("../../mpboot/build/mpboot-avx -s example.fasta");
    do_cmd("rm example.fasta.parstree");
    do_cmd("rm example.fasta.log");
}

void checkDNA(int val) {
    int num_nuc = 0;
    int num_ungap = 0;
    for (int i = 1; i <= val; i++) {
        for (int j = 0; j < m; j++) {
            char val = a[i].nuc[j];
            if (val != '?' && val != '-' && val != '.' && val != 'N' && val != 'X')
                num_ungap++;
            if (val == 'A' || val == 'C' || val == 'G' || val == 'T' || val == 'U')
                num_nuc++;
        }
    }
    cout << (double)num_nuc / num_ungap << " ";
    if ((double)num_nuc / num_ungap > 0.9) cout << "OK\n";
    else cout << "WRONG\n";
}
 
int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    srand(time(NULL));
    n = 5;
    k = 5;
    m = 20;
    int minMutation = 3;
    int maxMutation = 5;
    for (int i = 1; i <= m; i++) a[1].nuc += 'A';
    for (int i = 0; i <= n + k; i++) {
        a[i].name = "Trung" + to_string(i);
        a[i].nuc = a[1].nuc;
    }
    /*for (int i = 1; i <= n + k; i++) {
        int val = getRan(minMutation, maxMutation);
        for (int j = 1; j <= val; j++) {
            int pos = getRan(1, m);
            a[i].nuc[pos - 1] = typeNuc[getRan(2, typeNuc.length()) - 1];
        }
    }*/

    for (int i = 1; i <= n + k; i++) {
        int val = getRan(minMutation, maxMutation);
        int pos = getRan(1, m);
        char nuc = typeNuc[getRan(2, typeNuc.length()) - 1];
        for (int j = 1; j <= val; j++) {
            int sample = getRan(1, n + k);
            a[sample].nuc[pos - 1] = nuc;
        }

        pos = getRan(1, m);
        a[i].nuc[pos - 1] = typeNuc[getRan(2, 4) - 1]; // CGT
    }

    printFasta(n + k);
    printVcf();
    printFasta(n);
    printTreeFile();

    checkDNA(n);
    checkDNA(n + k);
    cerr << "\nTime elapsed: " << 1000 * clock() / CLOCKS_PER_SEC << "ms\n";
}