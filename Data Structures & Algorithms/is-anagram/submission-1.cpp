class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;
        if (s == "" && t == "") return true;
        unordered_map<char, int> schar;
        unordered_map<char, int> tchar;

        for (int i = 0; i < s.size(); i++) {
            schar[s[i]] = schar[s[i]] + 1;
            tchar[t[i]] = tchar[t[i]] + 1;
        }

        for (auto c : schar) {
            if (schar[c.first] != tchar[c.first]) return false;
        }
        return true;
    }
};
