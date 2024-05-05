class Solution {
    func numRescueBoats(_ people: [Int], _ limit: Int) -> Int {
        var people = people.sorted()
        var numBoats = 0
        var start = 0
        var end = people.count - 1

        while start <= end {
            if people[start] + people[end] <= limit {
                start += 1  // Pair the lightest and the heaviest person if possible
            }
            end -= 1  // Always move the end pointer to account for the heaviest person
            numBoats += 1  // Count this configuration as one boat
        }

        return numBoats
    }
}