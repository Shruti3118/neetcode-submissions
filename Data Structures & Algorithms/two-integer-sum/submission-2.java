class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hm = new HashMap<Integer, Integer>();
        hm.put(target-nums[0], 0);
        for(int i=1; i<nums.length; i++){
            if(hm.containsKey(nums[i]))
            {
                return new int[] {hm.get(nums[i]), i};
            }
            hm.put(target-nums[i],i);
        }
        return new int[] {0,0};
    }
}
