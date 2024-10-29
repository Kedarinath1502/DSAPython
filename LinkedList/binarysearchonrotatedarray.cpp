// // Online C++ compiler to run C++ program online
// #include <iostream>
// #include <vector>
// using namespace std;
// int rotatedBinarySearch(const vector<int>& arr, int key){
//     int low = 0;
//     int high = arr.size() -1;
//     while(low<=high){
//         int mid = (low + high)/2;
//         if ( key == arr[mid]){
//             return mid;
//         }
//         if(arr[low] <= arr[mid]){
//             if(arr[low] <= key && key < arr[mid]){
//                 high = mid -1;
//             }else{
//                 low = mid + 1;
//             }
//         }else{
//             if(arr[mid] < key && key <= arr[high]){
//                 low = mid + 1;
//             }else{
//                 high = mid -1;
//             }
//         }
//     }
//     return -1;
// }
// int main() {
//     vector<int> arr = {15, 18, 2, 6, 12,3};  
//     int key = 3;
//     int index = rotatedBinarySearch(arr, key);
//     cout<< index;
//     return 0;
// }