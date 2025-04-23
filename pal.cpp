class Solution 
{
public:
    bool isPalindrome(long long int x) 
    {
       long long int m = x;
       long long int n = 0;
       while(x>0)
       {
            n = (n* 10) + x % 10;
            x = x/10;
       }
       if(m == n)
       {
        return true;
       }
       else
       {
        return false;
       }
    }
};