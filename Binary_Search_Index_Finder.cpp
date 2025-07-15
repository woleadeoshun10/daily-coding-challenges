/* 
Given a sorted list of integers and a target value, write a function to perform binary search and return the index of the target value.
If the target does not exist in the list, return -1.

Your implementation should be efficient and should follow the binary search algorithm logic (divide and conquer).


*/


#include <iostream>
#include <vector>
using namespace std;

// Function to perform binary search
int binarySearch(vector<int>& nums, int target){
  int first = 0;
  int last = nums.size() - 1;
  
  while(first <= last){
    int mid = (first + last) / 2;
    if (nums[mid] == target){
      return mid;
    }
    else if (nums[mid] < target){
      first = mid + 1;
    }
    else{
      last = mid - 1;
    }
  }
  return -1;
}

int main() {
    vector<int> nums = {1, 3, 5, 7, 9, 11};
    int target = 7;

    int result = binarySearch(nums, target);
    cout << "Target index: " << result << endl;

    return 0;
}