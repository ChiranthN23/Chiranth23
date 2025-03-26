class Solution {
    public:
        void swap(int &a, int &b)
        {
            int temp;
            temp = a;
            a = b;
            b = temp;
        }
        int removeElement(vector<int>& nums, int key)
    
        {
            int count=0;
            int len = nums.size();
            int n = len;
            int a[105] = {0};
            for (int i = 0; i< len ; i++) 
            a[i] = nums[i];
            
            int temp;
            for(int i=0;i<n-1;i++)
            {
                if(key==a[i])
                {
    
                    swap(a[i] , a[i+1]);
                    if(a[i] == a[i+1])
                    {
                        for(int j=i;j<n;j++)
                        {
                            if(a[j]!=key)
                            {
                                swap(a[j],a[i]);
                            }
                        }
                    }
                }
    
            }
            for(int i = 0;i<n;i++)
            {
                if(a[i]!=key)
                {
                    count++;
                }
            }
            for (int i = 0; i<len; i++) 
            {
                nums[i] = a[i];
            }
            return count;
        }
    };