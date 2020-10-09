let arr = [1, 5, 3, 9, 2];
let sortedArray = sort(arr);
console.log(sortedArray);

function sort(arr) {
  for (let i = 1; i < arr.length; i++) {
    let j = i - 1;
    let key = arr[i];

    while (j >= 0 && key < arr[j]) {
      arr[j + 1] = arr[j];
      j--;
    }
    arr[j + 1] = key;
  }
  console.log(arr);
  return arr;
}
