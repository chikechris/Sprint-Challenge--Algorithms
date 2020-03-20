#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n)

The time complexity for a = 0 is O(1), since it's simply an assignment operator. The while loop has time complexity O(n). This is because the steps needed for a to reach n^3 by adding n^2 each step is n^3 / n^2 = n. We then take O(1) + O(n). Over all, (a) has time complexity O(n) because O(1) is insignificant in comparison.

b) O(n log n)

Taking the two largest time complexities (annotated above), we multiply them because one loop is nested inside the other. Over all, the time complexity is O(n log n).

c) O(n)

This one has time complexity of O(n), because it will take n times to subtract 1 from n until we get to 0 (at which point the function stops recursing).

## Exercise II

Binary serach would be a great strategy. The Binary search inputs a sorted list elements and outputs the position of the elements location if found within the list. The algorithm runs in O(log n) time; upon finding the mid point of the list, a comparison is conducted on the value of the low and high and leaving out the side with the unwanted result.

- I will create a list of floors with range upto n
- Get the midpoint by dividing by 2 and seperate the list in halves.
- Then i will have low to mid and mid to high
- I would conduct a test by dropping an egg or eggs from the midpoint
- I will check to see if they broke
- If so, I try out low to mid. then mid to high
- Then I will be able to find f by notating the floor that the egg broke at.
