bool canConstruct(char* ransomNote, char* magazine) {
    // Make a table size 26 for the frequency of each letter from ransomNote
    // Make a table size 26 for the frequency of each letter from magazine
    // Compare element wise

    int ransomfreq[26] = {0};
    int magazinefreq[26] = {0};
    for(int i = 0; ransomNote[i] != '\0'; i++){ransomfreq[ransomNote[i] - 'a']++;}
    for(int i = 0; magazine[i] != '\0'; i++){magazinefreq[magazine[i] - 'a']++;}
    for(int i = 0; i < 26; i++){
        if (ransomfreq[i] > magazinefreq[i]) return 0;
    }
    return 1;
}