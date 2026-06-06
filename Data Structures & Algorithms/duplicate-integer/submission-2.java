class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> hashSet = new HashSet<Integer>();
        for(int i=0; i<nums.length; i++){
            if(hashSet.contains(nums[i])==true)
                return true;
            hashSet.add(nums[i]);
        }
        return false;
    }
}
