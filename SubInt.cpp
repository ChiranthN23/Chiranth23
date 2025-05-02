class Solution 
{
public:
    bool checkPerfectNumber(int n) 
    {
        if (n <= 1) 
        return false;
        int sum = 1;

        for (int i = 2; i * i <= n; i++) 
        {
            if (n % i == 0) 
            {
                sum = sum + i;
                int pair = n / i;
                if (i != pair) 
                { 
                    sum += pair;
                }
            }
        }

        return sum == n;
        //Returns the sum and thus gives the final answer.
    }
};