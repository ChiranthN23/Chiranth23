class Solution {
    public:
        int lengthOfLastWord(string s) {
            int n = s.size();
            if(n==1) 
            return 1;
            int ans = 0;
            for(int i=n-1; i>=0; i--){
                if(s[i]!=' ')
                ans++;
    
                if(i!=0)
                {
                if(s[i]!=' ' && s[i-1]==' ') break;
                }
            }
            return ans;
        }
    };