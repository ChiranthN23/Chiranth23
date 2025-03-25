class Solution 
{
public:
    bool isPalindrome(long long int x) 
    {
       long long int m = x;
       long long int num = 0;
       while(x>0)
       {
            num = (num * 10) + x % 10;
            x = x/10;
       }
       if(m == num)
       {
        return true;
       }
       else
       {
        return false;
       }
    }
};