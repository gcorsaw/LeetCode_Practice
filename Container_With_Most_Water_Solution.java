class Solution {
    public int maxArea(int[] height) {
        int leftZone = 0;
        int rightZone = height.length - 1;
        int maxArea = 0;

        while(leftZone < rightZone){
            int width = rightZone - leftZone;
            int columnHeight = Math.min(height[leftZone], height[rightZone]);
            maxArea = Math.max(maxArea, width * columnHeight);

            if(height[leftZone] < height[rightZone]){
                leftZone++;
            }else{
                rightZone--;
            }
        }
        return maxArea;
    }
}