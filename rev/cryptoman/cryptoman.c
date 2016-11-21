#include <stdio.h>
#include <unistd.h>

const int KEY_SIZE = 8;

static inline int swp(const char *n) {
    return (n[3] << 8) | (n[1] << 16) | (n[2]) | (n[0] << 24);
}

#ifdef DEBUG
static inline int dswp(const char *n) {
    return (n[3]) | (n[1] << 24) | (n[2] << 8) | (n[0] << 16);
}
#endif

void encrypt(char *enc, const char *dec, const char *key, size_t n) {
    for (int i = 0; i < n; ++i) {
        enc[i] = dec[i] ^ key[i % KEY_SIZE];
    }

    for (char *p = enc; p < enc + n; p += 4) {
        *((int*)p) = swp((char*)p);
    }
    
    for (int i = 0; i < n; ++i) {
        enc[i] = enc[i] ^ key[i % KEY_SIZE];
    }
}

#ifdef DEBUG
void decrypt(char *enc, const char *dec, const char *key, size_t n) {
    for (int i = 0; i < n; ++i) {
        enc[i] = dec[i] ^ key[i % KEY_SIZE];
    }

    for (char *p = enc; p < enc + n; p += 4) {
        *((int*)p) = dswp(p);
    }
    
    for (int i = 0; i < n; ++i) {
        enc[i] = enc[i] ^ key[i % KEY_SIZE];
    }
}
#endif

int main(int argc, char const *argv[]) {
    FILE *f = fopen("flag", "r");
    fseek(f, 0L, SEEK_END);
    const size_t size = ftell(f);
    rewind(f);

    char str[size];
    fread(str, size, 1, f);
    fclose(f);
    
    f = fopen("key", "r");
    char key[KEY_SIZE];
    fread(key, KEY_SIZE, 1, f);
    fclose(f);

    char enc[size];
    encrypt(enc, str, key, size);

    f = fopen("encrypted", "w");
    fwrite(enc, size, 1, f);
    fclose(f);

#ifdef DEBUG
    decrypt(str, enc, key, size);
    write(1, str, size);
#endif
    return 0;
}
