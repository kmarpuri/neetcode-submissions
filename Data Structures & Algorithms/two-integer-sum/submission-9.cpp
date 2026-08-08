class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // value, index
        unordered_map<int, int> map;
        vector<int> ans;
        for (int i = 0; i < nums.size(); i++) {
            if (map.count(target - nums[i])) {
                ans = {map[target - nums[i]], i};
                return ans;
            }
            if (!map.count(nums[i])) {
                map[nums[i]] = i;
            }
        }
        return ans;
    }
};
