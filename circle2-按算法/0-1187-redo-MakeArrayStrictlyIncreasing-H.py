'''
1187. Make Array Strictly Increasing
'''

    int makeArrayIncreasing(vector<int>& arr1, vector<int>& arr2) {
        int n = arr1.size();
        if (n == 1) return 0;
        set<int> st(arr2.begin(), arr2.end());
        vector<vector<int>> dp(n + 1, vector<int>(n + 1, INT_MAX));
        dp[0][0] = INT_MIN;
        for (int j = 1; j <= n; ++j) {
            for (int i = 0; i <= j; ++i) {
                if (arr1[j - 1] > dp[i][j - 1]) {
                    dp[i][j] = arr1[j - 1];
                }
                if (i > 0) {
                    auto it = st.upper_bound(dp[i - 1][j - 1]);
                    if (it != st.end()) dp[i][j] = min(dp[i][j], *it);
                }  
                if (j == n && dp[i][j] != INT_MAX) return i;
            }
        }
        return -1;
    }
 