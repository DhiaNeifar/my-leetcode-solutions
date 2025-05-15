int climbStairs(int n)
{
    if (n <= 1)
    {
        return 1;
    }
    else
    {
        int ways[n + 1];
        ways[0] = 1;
        ways[1] = 1;
        for (int i = 2; i < n + 1; i++)
        {
            ways[i] = ways[i - 2] + ways[i - 1];
        }
        return ways[n];
    }
    
}