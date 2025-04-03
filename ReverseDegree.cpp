class Solution {
    public:
        int reverseDegree(string s) {
            int count = 0;
            for(int i = 0; i < s.size(); i++) {
                count = count +(i + 1) * (123 - s[i]);
            }
            return count;
        }
    };