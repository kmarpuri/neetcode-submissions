class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;
        if (s == "" && t == "") return true;
        unordered_map<char, int> schar;
        unordered_map<char, int> tchar;

        for (int i = 0; i < s.size(); i++) {
            schar[s[i]]++;
            tchar[t[i]]++;
        }
        return schar == tchar;
    }
};
