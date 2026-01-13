# @param {Integer[]} height
# @return {Integer}
def trap(height)
    l_max, r_max = 0, 0 # the maximum heights left of cur and right of cur, respectively
    n = height.length
    max_l = Array.new(n, 0) # array of maximums left of arr[i]
    max_r = Array.new(n, 0) # array of maximums right of arr[i]

    # craft the array of maximums left of each i pos
    (0...n-1).each do |i|
        max_l[i] = l_max
        l_max = [l_max, height[i]].max
    end

    # craft the array of maximums right of each i pos
    (n-1).downto(0) do |i|
        max_r[i] = r_max
        r_max = [r_max, height[i]].max
    end

    sum = 0

    (0...n-1).each do |i|
        potential = [max_r[i], max_l[i]].min # the potential height of the water is the minimum of the 2
        sum += [0, potential - height[i]].max # if potential is smaller than height[i], its going to be negative
    end

    return sum

end